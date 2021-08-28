import warnings

from kubernetes import config, client
from kubernetes.client import ApiClient, CoreV1Api, AppsV1Api
from osbot_utils.utils.Dev import pprint

from osbot_k8s.kubernetes.Namespace import Namespace
from osbot_utils.decorators.lists.group_by          import group_by
from osbot_utils.decorators.lists.index_by          import index_by
from osbot_utils.decorators.methods.cache_on_self   import cache_on_self
from osbot_utils.utils.Misc                         import ignore_warning__unclosed_ssl


class Cluster:

    def __init__(self, default_namespace='default', config_file=None, config_context=None):
        ignore_warning__unclosed_ssl()
        self.default_namespace   = Namespace(name=default_namespace, cluster=self)
        self.config_file         = config_file
        self.config_context      = config_context

    @cache_on_self
    def api_apps_v1(self) -> AppsV1Api:
        self.load_config()
        return client.AppsV1Api()

    @cache_on_self
    def api_core_v1(self) -> CoreV1Api:
        self.load_config()
        return client.CoreV1Api()

    def convert_k8s_list_to_dict(self, target):
        items = []                                                      # do this so that we have easy to manipulate python objects
        for item in target:   # and there doesn't seem to be any advantage of actually using the kubernetes API Resource class (for example methods to use those resources)
            items.append(item.to_dict())
        return items

    @index_by
    @group_by
    def api_resources(self):
        return self.convert_k8s_list_to_dict(self.api_apps_v1().get_api_resources().resources)

    def config_maps(self):
        data = self.api_core_v1().list_config_map_for_all_namespaces()
        return self.convert_k8s_list_to_dict(data.items)

    def config_maps_data(self):
        config_maps_data = {}
        for config_map in self.config_maps():
            for data_name, data_value in config_map.get('data').items():
                config_maps_data[data_name] = data_value                     # ok to override since all values are the same
        return config_maps_data

    def info(self):
        return self.config_maps()      # todo, refactor into a method that feel more like info

    def load_config(self):
        try:
            config.load_kube_config(config_file=self.config_file, context=self.config_context)
            return True
        except Exception as error:
            print(error)
            return False

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

    def pod(self, name):
        from osbot_k8s.kubernetes.Pod import Pod            # todo - refactor to remove circular reference issue
        return Pod(name=name, cluster=self)

    def pod_create(self, name, manifest):
        pod    = self.pod(name)
        result = pod.create(manifest)
        return { 'pod': pod, 'result':result }

    @index_by
    @group_by
    def pods(self):
        from osbot_k8s.kubernetes.Pod import Pod  # todo - refactor to remove circular reference issue
        pods = []
        for item in self.pods_raw():
            pod = Pod(item.metadata.name, cluster=self)
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

