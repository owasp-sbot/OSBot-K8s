from osbot_utils.utils.Dev import pprint

from osbot_utils.utils.Misc import random_string

from osbot_k8s.kubernetes.Cluster import Cluster
from osbot_k8s.manifests.Pod_Manifest import Pod_Manifest


class Create_Multiple_Pods:

    def __init__(self):
        self.cluster        = Cluster()
        self.namespace      = 'default'
        self.default_image  = 'nginx'

    def pod_manifest(self, pod_name, pod_image):
        return Pod_Manifest().set_name(pod_name).add_container(self.default_image).render()

    def create_pod(self, name_prefix=None, pod_image=None):
        if pod_image is None:
            pod_image = self.default_image
        if name_prefix is None:
            name_prefix = pod_image
        pod_name     = random_string(prefix=f"{name_prefix}-")
        pod_manifest = self.pod_manifest(pod_name=pod_name, pod_image=pod_image)
        return self.cluster.pod_create(manifest=pod_manifest)

    def create_pods(self,count=1,  name_prefix=None, pod_image=None):
        for i in range(0, count):
            print(self.create_pod(name_prefix=name_prefix, pod_image=pod_image))

    def create_pod_grafana(self):
        pod_name     = 'grafana'
        pod_image    = 'docker.io/grafana/grafana:v7.0.0-beta3'
        pod_manifest = self.pod_manifest(pod_name=pod_name, pod_image=pod_image)
        return self.cluster.pod_create(manifest=pod_manifest)

    def delete_pods(self):
        pods = self.cluster.pods()
        for pod in pods:
            print(pod.delete())
