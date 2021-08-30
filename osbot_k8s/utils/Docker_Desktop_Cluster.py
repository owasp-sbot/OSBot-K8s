from osbot_k8s.kubernetes.Cluster import Cluster

DEFAULT_DOCKER_DESKTOP_NAME = 'docker-desktop'
DEFAULT_DOCKER_DESKTOP_HOST = 'https://kubernetes.docker.internal:6443'


class Docker_Desktop_Cluster(Cluster):
    def __init__(self):
        super().__init__(config_context=DEFAULT_DOCKER_DESKTOP_NAME)


#### notes for Docker-Desktop
#
# editing the manifests "etcd.yaml  kube-apiserver.yaml  kube-controller-manager.yaml  kube-scheduler.yaml"
# in /host/etc/kubernetes/manifests are applied on save and allow setting startup values like
# the verbosity (add - -v1 to -v5 to the args)