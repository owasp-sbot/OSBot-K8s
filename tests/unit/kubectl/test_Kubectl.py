from unittest import TestCase

from osbot_k8s.utils.Docker_Desktop_Cluster import DEFAULT_DOCKER_DESKTOP_NAME
from osbot_utils.utils.Misc import list_set
from osbot_utils.utils.Dev import pprint
from osbot_k8s.kubectl.Kubectl import Kubectl


class test_Kubectl(TestCase):

    def setUp(self) -> None:
        self.kubectl = Kubectl()


    def test_kubectl_exec(self):
        assert  self.kubectl.kubectl_exec().startswith('kubectl controls the Kubernetes cluster manager.\n')

    def test_kubectl_exec_raw(self):
        result = self.kubectl.kubectl_exec_raw()
        assert result.get('stdout').startswith('kubectl controls the Kubernetes cluster manager.\n')
        del result['stdout']
        assert result == { 'cwd'        : '.'           ,
                           'error'      : None          ,
                           'kwargs'     : {'cwd': '.', 'stderr': -1, 'stdout': -1, 'timeout': None},
                           'runParams'  : ['kubectl']   ,
                           'status'     : 'ok'          ,
                           'stderr'     : ''            }

    # config methods

    def test_clusters(self):
        clusters = self.kubectl.clusters()
        assert DEFAULT_DOCKER_DESKTOP_NAME in clusters
        assert list_set(clusters.get(DEFAULT_DOCKER_DESKTOP_NAME)) == ['certificate-authority-data', 'server']

    def test_config(self):
        result = self.kubectl.config()
        assert list_set(result) == ['apiVersion', 'clusters', 'contexts', 'current-context', 'kind', 'preferences', 'users']
        pprint(result)

    def test_context_set_current(self):
        assert self.kubectl.context_set_current('aaa') == 'error: no context exists with the name: "aaa"\n'
        assert self.kubectl.context_set_current(DEFAULT_DOCKER_DESKTOP_NAME) == f'Switched to context "{DEFAULT_DOCKER_DESKTOP_NAME}".\n'
        assert self.kubectl.context_current() == DEFAULT_DOCKER_DESKTOP_NAME

    def test_contexts(self):
        contexts = self.kubectl.contexts()
        assert DEFAULT_DOCKER_DESKTOP_NAME in contexts
        assert list_set(contexts.get(DEFAULT_DOCKER_DESKTOP_NAME)) == ['client-certificate-data', 'client-key-data']

    def test_contexts(self):
        contexts = self.kubectl.contexts()
        assert DEFAULT_DOCKER_DESKTOP_NAME in contexts
        assert list_set(contexts.get(DEFAULT_DOCKER_DESKTOP_NAME)) == ['cluster', 'user']

    def test_users(self):
        users = self.kubectl.users()
        assert DEFAULT_DOCKER_DESKTOP_NAME in users
        assert list_set(users.get(DEFAULT_DOCKER_DESKTOP_NAME)) == ['client-certificate-data', 'client-key-data']

    # kubectl functions



    def test_deployments(self):
        result = self.kubectl.deployments()
        pprint(result)