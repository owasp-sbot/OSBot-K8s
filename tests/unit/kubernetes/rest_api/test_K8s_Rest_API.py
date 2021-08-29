from unittest import TestCase

from osbot_utils.utils.Misc import list_set, list_index_by, str_to_base64

from osbot_utils.utils.Dev import pprint

from osbot_k8s.kubernetes.rest_api.K8s_Rest_API import K8s_Rest_API
from tests.unit.kubernetes.test_Cluster_Info import DEFAULT_DOCKER_DESKTOP_NAME


class test_K8s_Rest_API(TestCase):

    def setUp(self):
        self.k8s_rest_api = K8s_Rest_API(config_context=DEFAULT_DOCKER_DESKTOP_NAME)

    # helpers
    def test_request_GET(self):
        result = self.k8s_rest_api.request_GET('/')
        assert len(result.get('paths')) > 50

    def test_proxy_pod_request_GET(self):
        pods          = self.k8s_rest_api.api_v1_pods()
        pod_port      = '9153'
        pod_name      = None
        namespace     = None
        for pod in pods.get('items'):
            pod_name  = pod.get('metadata').get('name')
            namespace = pod.get('metadata').get('namespace')
            if pod_name.split('-')[0] == 'coredns':
                break

        assert pod_name  is not None
        assert namespace is not None
        kwargs = {'pod_name'      : pod_name   ,
                  'pod_namespace' : namespace  ,
                  'pod_port'      : pod_port   ,
                  'pod_path'      : 'metrics'  }

        data_ok = self.k8s_rest_api.proxy_pod_request_GET(**kwargs)
        assert data_ok.startswith('# HELP coredns_build_info A metric with a constant ')

        path_404           = 'aaaaaa'
        kwargs['pod_path'] = path_404
        data_404 = self.k8s_rest_api.proxy_pod_request_GET(**kwargs)
        assert data_404 == {  'data'   : None                                                                                                           ,
                              'error'  : '404 page not found\n'                                                                                         ,
                              'message': f'API exception: 404:Not Found: for /api/v1/namespaces/{namespace}/pods/{pod_name}:{pod_port}/proxy/{path_404}',
                              'status' : 'error'                                                                                                        }



    # methods

    def test_proxy_service_request_GET(self):
        service_port = '9153'
        service_name = 'kube-dns'
        namespace    = 'kube-system'

        kwargs = {'service_name'  : service_name ,
                  'pod_namespace' : namespace    ,
                  'service_port'  : service_port ,
                  'pod_path'      : 'metrics'    }

        data_ok = self.k8s_rest_api.proxy_service_request_GET(**kwargs)

        assert data_ok.startswith('# HELP coredns_build_info A metric with a constant ')

        path_404           = 'aaaaaa'
        kwargs['pod_path'] = path_404
        data_404 = self.k8s_rest_api.proxy_service_request_GET(**kwargs)
        assert data_404 == {  'data'   : None                                                                                                           ,
                              'error'  : '404 page not found\n'                                                                                         ,
                              'message': f'API exception: 404:Not Found: for /api/v1/namespaces/{namespace}/services/{service_name}:{service_port}/proxy/{path_404}',
                              'status' : 'error'                                                                                                        }

    # methods
    def test_api(self):
        assert self.k8s_rest_api.api() == { 'kind'                      : 'APIVersions',
                                            'serverAddressByClientCIDRs': [{'clientCIDR': '0.0.0.0/0',
                                            'serverAddress'             : '192.168.65.4:6443'}],
                                            'versions'                  : ['v1']}


    def test_api_v1(self):
        api_v1 =  self.k8s_rest_api.api_v1()
        assert list_set(api_v1) == ['groupVersion', 'kind', 'resources']
        assert api_v1.get('groupVersion') == 'v1'
        assert api_v1.get('kind'        ) == 'APIResourceList'
        resources_by_name = list_index_by(api_v1.get('resources'), 'name')
        assert list_set(resources_by_name) == ['bindings', 'componentstatuses', 'configmaps', 'endpoints', 'events', 'limitranges', 'namespaces',
                                               'namespaces/finalize', 'namespaces/status', 'nodes', 'nodes/proxy', 'nodes/status',
                                               'persistentvolumeclaims', 'persistentvolumeclaims/status', 'persistentvolumes',
                                               'persistentvolumes/status', 'pods', 'pods/attach', 'pods/binding', 'pods/eviction', 'pods/exec',
                                               'pods/log', 'pods/portforward', 'pods/proxy', 'pods/status', 'podtemplates', 'replicationcontrollers',
                                               'replicationcontrollers/scale', 'replicationcontrollers/status', 'resourcequotas',
                                               'resourcequotas/status', 'secrets', 'serviceaccounts', 'serviceaccounts/token', 'services',
                                               'services/proxy', 'services/status']

    def test_api_v1_pods(self):
        api_v1_pods = self.k8s_rest_api.api_v1_pods()
        assert list_set(api_v1_pods) == ['apiVersion', 'items', 'kind', 'metadata']
        assert api_v1_pods.get('apiVersion') == 'v1'
        assert api_v1_pods.get('kind'      ) == 'PodList'
        assert list_set(api_v1_pods.get('metadata')) == ['resourceVersion']
        pods = self.k8s_rest_api.index_by_metadata_name(api_v1_pods.get('items'))
        assert 'etcd-docker-desktop'  in pods
        pod_etcd = pods.get('etcd-docker-desktop')
        assert pod_etcd.get('spec').get('containers').pop().get('volumeMounts') == [ {'mountPath': '/var/lib/etcd', 'name': 'etcd-data'},
                                                                                     { 'mountPath': '/run/config/pki/etcd',




                                                                                       'name': 'etcd-certs'}]
    # def test_api_v1_pods_proxy(self):       #todo: not working
    #     #api_v1_pods_proxy = self.k8s_rest_api.api_v1_pods_proxy()
    #     #pprint(api_v1_pods_proxy)
    #     namespace    = 'kube-system'
    #     service_name = 'kube-dns'
    #     pod_name     = 'coredns-558bd4d5db-75vk8'
    #     port         = '9153'
    #     pod_path = 'metrics'
    #             #"/api/v1/namespaces/{namespace}/pods/{name}/proxy"
    #     #path = f'/api/v1/namespaces/{namespace}/pods/{pod_name}:{port}/proxy/{pod_path}'
    #     path = f'/api/v1/namespaces/{namespace}/services/{service_name}:{port}/proxy/{pod_path}'
    #     data = self.k8s_rest_api.request_GET(path)
    #     print(data)


    def test_api_v1_services(self):
        api_v1_pods_services = self.k8s_rest_api.api_v1_services()
        assert len(api_v1_pods_services.get('items')) >0

    def test_apis(self):
        apis =  self.k8s_rest_api.apis()
        assert list_set(apis) == ['apiVersion', 'groups', 'kind']
        assert apis.get('apiVersion') == 'v1'
        assert apis.get('kind'      ) == 'APIGroupList'
        groups_by_name = list_index_by(apis.get('groups'), 'name')
        assert list_set(groups_by_name) == [ 'admissionregistration.k8s.io', 'apiextensions.k8s.io', 'apiregistration.k8s.io', 'apps',
                                             'authentication.k8s.io', 'authorization.k8s.io', 'autoscaling', 'batch', 'certificates.k8s.io',
                                             'coordination.k8s.io', 'discovery.k8s.io', 'events.k8s.io', 'extensions',
                                             'flowcontrol.apiserver.k8s.io', 'networking.k8s.io', 'node.k8s.io', 'policy',
                                             'rbac.authorization.k8s.io', 'scheduling.k8s.io', 'storage.k8s.io']


    def test_version(self):
        assert self.k8s_rest_api.version() == {'buildDate'   : '2021-06-16T12:53:14Z'                    ,
                                               'compiler'    : 'gc'                                      ,
                                               'gitCommit'   : '092fbfbf53427de67cac1e9fa54aaa09a28371d7',
                                               'gitTreeState': 'clean'                                   ,
                                               'gitVersion'  : 'v1.21.2'                                 ,
                                               'goVersion'   : 'go1.16.5'                                ,
                                               'major'       : '1'                                       ,
                                               'minor'       : '21'                                      ,
                                               'platform'    : 'linux/amd64'                             }

    def test_root_paths(self):
        assert self.k8s_rest_api.root_paths() == ['/.well-known/openid-configuration',
                                                  '/api', '/api/v1', '/apis', '/apis/',
                                                  '/apis/admissionregistration.k8s.io', '/apis/admissionregistration.k8s.io/v1', '/apis/admissionregistration.k8s.io/v1beta1',
                                                  '/apis/apiextensions.k8s.io', '/apis/apiextensions.k8s.io/v1', '/apis/apiextensions.k8s.io/v1beta1', '/apis/apiregistration.k8s.io',
                                                  '/apis/apiregistration.k8s.io/v1', '/apis/apiregistration.k8s.io/v1beta1', '/apis/apps', '/apis/apps/v1', '/apis/authentication.k8s.io',
                                                  '/apis/authentication.k8s.io/v1', '/apis/authentication.k8s.io/v1beta1', '/apis/authorization.k8s.io', '/apis/authorization.k8s.io/v1',
                                                  '/apis/authorization.k8s.io/v1beta1', '/apis/autoscaling', '/apis/autoscaling/v1', '/apis/autoscaling/v2beta1', '/apis/autoscaling/v2beta2',
                                                  '/apis/batch', '/apis/batch/v1', '/apis/batch/v1beta1', '/apis/certificates.k8s.io', '/apis/certificates.k8s.io/v1', '/apis/certificates.k8s.io/v1beta1',
                                                  '/apis/coordination.k8s.io', '/apis/coordination.k8s.io/v1', '/apis/coordination.k8s.io/v1beta1', '/apis/discovery.k8s.io', '/apis/discovery.k8s.io/v1',
                                                  '/apis/discovery.k8s.io/v1beta1', '/apis/events.k8s.io', '/apis/events.k8s.io/v1', '/apis/events.k8s.io/v1beta1', '/apis/extensions',
                                                  '/apis/extensions/v1beta1', '/apis/flowcontrol.apiserver.k8s.io', '/apis/flowcontrol.apiserver.k8s.io/v1beta1', '/apis/networking.k8s.io',
                                                  '/apis/networking.k8s.io/v1', '/apis/networking.k8s.io/v1beta1', '/apis/node.k8s.io', '/apis/node.k8s.io/v1', '/apis/node.k8s.io/v1beta1',
                                                  '/apis/policy', '/apis/policy/v1', '/apis/policy/v1beta1', '/apis/rbac.authorization.k8s.io', '/apis/rbac.authorization.k8s.io/v1',
                                                  '/apis/rbac.authorization.k8s.io/v1beta1', '/apis/scheduling.k8s.io', '/apis/scheduling.k8s.io/v1', '/apis/scheduling.k8s.io/v1beta1',
                                                  '/apis/storage.k8s.io', '/apis/storage.k8s.io/v1', '/apis/storage.k8s.io/v1beta1',

                                                  '/healthz', '/healthz/autoregister-completion', '/healthz/etcd', '/healthz/log', '/healthz/ping', '/healthz/poststarthook/aggregator-reload-proxy-client-cert',
                                                  '/healthz/poststarthook/apiservice-openapi-controller', '/healthz/poststarthook/apiservice-registration-controller',
                                                  '/healthz/poststarthook/apiservice-status-available-controller', '/healthz/poststarthook/bootstrap-controller', '/healthz/poststarthook/crd-informer-synced',
                                                  '/healthz/poststarthook/generic-apiserver-start-informers', '/healthz/poststarthook/kube-apiserver-autoregistration',
                                                  '/healthz/poststarthook/priority-and-fairness-config-consumer', '/healthz/poststarthook/priority-and-fairness-config-producer',
                                                  '/healthz/poststarthook/priority-and-fairness-filter', '/healthz/poststarthook/rbac/bootstrap-roles', '/healthz/poststarthook/scheduling/bootstrap-system-priority-classes',
                                                  '/healthz/poststarthook/start-apiextensions-controllers', '/healthz/poststarthook/start-apiextensions-informers', '/healthz/poststarthook/start-cluster-authentication-info-controller',
                                                  '/healthz/poststarthook/start-kube-aggregator-informers', '/healthz/poststarthook/start-kube-apiserver-admission-initializer',

                                                  '/livez', '/livez/autoregister-completion', '/livez/etcd', '/livez/log', '/livez/ping', '/livez/poststarthook/aggregator-reload-proxy-client-cert',
                                                  '/livez/poststarthook/apiservice-openapi-controller', '/livez/poststarthook/apiservice-registration-controller', '/livez/poststarthook/apiservice-status-available-controller',
                                                  '/livez/poststarthook/bootstrap-controller', '/livez/poststarthook/crd-informer-synced', '/livez/poststarthook/generic-apiserver-start-informers',
                                                  '/livez/poststarthook/kube-apiserver-autoregistration', '/livez/poststarthook/priority-and-fairness-config-consumer', '/livez/poststarthook/priority-and-fairness-config-producer',
                                                  '/livez/poststarthook/priority-and-fairness-filter', '/livez/poststarthook/rbac/bootstrap-roles', '/livez/poststarthook/scheduling/bootstrap-system-priority-classes',
                                                  '/livez/poststarthook/start-apiextensions-controllers', '/livez/poststarthook/start-apiextensions-informers', '/livez/poststarthook/start-cluster-authentication-info-controller',
                                                  '/livez/poststarthook/start-kube-aggregator-informers', '/livez/poststarthook/start-kube-apiserver-admission-initializer',

                                                  '/logs', '/metrics', '/openapi/v2', '/openid/v1/jwks',

                                                  '/readyz', '/readyz/autoregister-completion', '/readyz/etcd', '/readyz/informer-sync', '/readyz/log', '/readyz/ping', '/readyz/poststarthook/aggregator-reload-proxy-client-cert',
                                                  '/readyz/poststarthook/apiservice-openapi-controller', '/readyz/poststarthook/apiservice-registration-controller', '/readyz/poststarthook/apiservice-status-available-controller',
                                                  '/readyz/poststarthook/bootstrap-controller', '/readyz/poststarthook/crd-informer-synced', '/readyz/poststarthook/generic-apiserver-start-informers',
                                                  '/readyz/poststarthook/kube-apiserver-autoregistration', '/readyz/poststarthook/priority-and-fairness-config-consumer', '/readyz/poststarthook/priority-and-fairness-config-producer',
                                                  '/readyz/poststarthook/priority-and-fairness-filter', '/readyz/poststarthook/rbac/bootstrap-roles', '/readyz/poststarthook/scheduling/bootstrap-system-priority-classes',
                                                  '/readyz/poststarthook/start-apiextensions-controllers', '/readyz/poststarthook/start-apiextensions-informers', '/readyz/poststarthook/start-cluster-authentication-info-controller',
                                                  '/readyz/poststarthook/start-kube-aggregator-informers', '/readyz/poststarthook/start-kube-apiserver-admission-initializer', '/readyz/shutdown',

                                                  '/version']


    # this doesn't work because k8s proxy is striping the authentication token (using a locally deployed copy of rabbitmq for testing)
    # curl -v -u guest:guest \
    #   --cacert '/var/folders/_j/frqs70d93l328f307rw2jx5h0000gn/T/tmpne9wj7uo' \
    #   --cert '/var/folders/_j/frqs70d93l328f307rw2jx5h0000gn/T/tmp60q858kb' \
    #   --key '/var/folders/_j/frqs70d93l328f307rw2jx5h0000gn/T/tmp0wjg403x' \
    #   'https://kubernetes.docker.internal:6443/api/v1/namespaces/default/pods/rabbitmq:15672/proxy/api/whoami'
    # def test_rabbitmq(self):
    #     kwargs = {'pod_name'        : 'rabbitmq',
    #               'pod_namespace'   : 'default',
    #               'pod_port'        : '15672',
    #               'pod_path'        : ''}
    #
    #     data_ok = self.k8s_rest_api.proxy_pod_request_GET(**kwargs)
    #     assert '<title>RabbitMQ Management</title>' in data_ok
    #
    #     kwargs['pod_path'] = 'api/whoami'
    #     kwargs['headers' ] = {'authorization': f'Basic {str_to_base64("guest:guest")}'}
    #     #pprint(kwargs)
    #
    #     data_401 = self.k8s_rest_api.proxy_pod_request_GET(**kwargs)
    #     assert data_401 == { 'data': None                                                                   ,
    #                          'error': ''                                                                    ,
    #                          'message': 'API exception: 401:Unauthorized: for '
    #                                      '/api/v1/namespaces/default/pods/rabbitmq:15672/proxy/api/whoami'  ,
    #                          'status': 'error'                                                              }




