import kubernetes
from kubernetes.client.exceptions import ApiException
from kubernetes import config, client
from urllib.parse import urljoin

from kubernetes.client import AppsV1Api, CoreV1Api
from osbot_utils.utils.Status import status_error

from osbot_utils.utils.Json import json_parse

from osbot_utils.decorators.methods.cache_on_self import cache_on_self


class K8s_Rest_API:

    def __init__(self,config_file=None, config_context=None):
        self.config_file    = config_file
        self.config_context = config_context


    @cache_on_self
    def api_core_v1(self) -> CoreV1Api:                     # todo refactor into base class shared with Cluster_Info
        self.load_config()
        return client.CoreV1Api()

    def request_GET(self, path, headers=None):
        core_api       = self.api_core_v1()
        target_server = core_api.api_client.configuration.host
        url           = urljoin(target_server, path)
        try:
            response      = core_api.api_client.request(url=url, method='GET', headers=headers)
            data_raw      = response.data
            if response.getheader('content-type') == 'application/json':
                return json_parse(data_raw)
            return data_raw
        except ApiException as api_exception:
            return status_error(message=f"API exception: {api_exception.status}:{api_exception.reason}: for {path}", error=api_exception.body)

    def proxy_pod_request_GET(self, pod_name, namespace, pod_port, pod_path='', headers=None):
        proxy_path = f'/api/v1/namespaces/{namespace}/pods/{pod_name}:{pod_port}/proxy/{pod_path}'
        return self.request_GET(proxy_path, headers=headers)

    def proxy_service_request_GET(self, service_name, namespace, service_port, pod_path):
        proxy_path = f'/api/v1/namespaces/{namespace}/services/{service_name}:{service_port}/proxy/{pod_path}'
        return self.request_GET(proxy_path)

    def load_config(self):                                  # todo refactor into base class shared with Cluster_Info
        try:
            config.load_kube_config(config_file=self.config_file, context=self.config_context)
            return True
        except Exception as error:
            print(error)
            return False

    def index_by_metadata_name(self, target):
        indexed_by_name = {}
        for item in target:
            item_name = item.get('metadata').get('name')
            indexed_by_name[item_name] = item
        return indexed_by_name

    def group_by_metadata_namespace_and_index_by_metadata_name(self, target):
        by_namespace = {}
        for item in target:
            namespace = item.get('metadata').get('namespace')
            pod_name  = item.get('metadata').get('name')
            if by_namespace.get(namespace) is None:
                by_namespace[namespace] = {}
            by_namespace[namespace][pod_name] = item

        return by_namespace

    # methods

    def api(self):
        return self.request_GET('/api')

    def api_v1(self):
        return self.request_GET('/api/v1')

    def api_v1_pods(self):
        return self.request_GET('/api/v1/pods')


    # def api_v1_pods_log(self):
    #     return self.request_GET('/api/v1/pods/log/*')

    def api_v1_services(self):
        return self.request_GET('/api/v1/services')


    def apis(self):
        return self.request_GET('/apis')

    def version(self):
        return self.request_GET('/version')

    def root_paths(self):
        return self.request_GET('/').get('paths')