from osbot_k8s.kubernetes.Cluster_Info      import Cluster_Info
from osbot_k8s.kubernetes.Namespace         import Namespace
from osbot_k8s.kubernetes.Pod import Pod
from osbot_utils.decorators.lists.group_by  import group_by
from osbot_utils.decorators.lists.index_by  import index_by


class Cluster(Cluster_Info):            # todo: refactor this class to not use Cluster_Info as base class since there will be conflicting methods

    def __init__(self, default_namespace='default', config_file=None, config_context=None):
        super().__init__(config_file=config_file, config_context=config_context)
        self.default_namespace   = Namespace(name=default_namespace, cluster=self)

    def info(self):
        return self.config_maps()      # todo, refactor into a method that feel more like info

    def namespace(self, name=None) -> Namespace:
        if name:
            return Namespace(name=name, cluster=self)
        return self.default_namespace

    def namespaces(self):
        return [self.namespace(name) for name in self.namespaces_names()]

    @index_by
    @group_by
    def namespaces_infos(self):
        return [self.namespace(name).info() for name in self.namespaces_names()]

    def namespaces_names(self):
        return [item.metadata.name for item in self.namespaces_raw()]

    def namespaces_raw(self):
        return self.api_core_v1().list_namespace().items

    def pod(self, name=None):
        from osbot_k8s.kubernetes.Pod import Pod            # todo - refactor to remove circular reference issue
        return Pod(name=name, cluster=self)

    def pod_create(self, manifest):
        name   = manifest.get('metadata',{}).get('name')
        pod    = self.pod(name=name)
        result = pod.create(manifest)
        return { 'pod': pod, 'result':result }

    #@index_by
    #@group_by
    def pods(self):
        pods = []
        for pod_name in self.pods_in_namespace(namespace=self.default_namespace.name).keys():
            pod = Pod(pod_name, cluster=self)
            pods.append(pod)
        return pods

    def pods_all(self):
        from osbot_k8s.kubernetes.Pod import Pod  # todo - refactor to remove circular reference issue
        pods = []
        pods_data = self.api_core_v1().list_pod_for_all_namespaces(watch=False)
        for item in pods_data.items:
            pods.append(Pod(item.metadata.name, cluster=self))
        return pods

    def pods_in_phase(self, phase):
        return self.pods(group_by='phase').get(phase)

    def pods_names(self):
        return [item.metadata.name for item in self.pods_raw()]

    def pods_pending(self):
        return self.pods_in_phase('Pending')

    def pods_raw(self):
        return self.api_core_v1().list_namespaced_pod(namespace=self.namespace().name).items

    def set_default_namespace(self, name):
        self.default_namespace = Namespace(name)

