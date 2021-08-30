from kubernetes.client import AppsV1Api, CoreV1Api
from osbot_utils.utils.Misc import ignore_warning__unclosed_ssl

from osbot_utils.decorators.lists.group_by import group_by

from osbot_utils.decorators.lists.index_by import index_by

from osbot_utils.decorators.methods.cache_on_self import cache_on_self

from kubernetes import config, client

class Cluster_Info:

    def __init__(self, config_file=None, config_context=None):
        self.config_file    = config_file
        self.config_context = config_context
        ignore_warning__unclosed_ssl()

    @cache_on_self
    def api_apps_v1(self) -> AppsV1Api:
        self.load_config()
        return client.AppsV1Api()

    @cache_on_self
    def api_core_v1(self) -> CoreV1Api:
        self.load_config()
        return client.CoreV1Api()

    def load_config(self):
        try:
            config.load_kube_config(config_file=self.config_file, context=self.config_context)
            return True
        except Exception as error:
            print(error)
            return False

    # data load helper methods

    def call_and_index__api__list__by_metadata_name(self, api_function, function_name, **kwargs):
        function      = getattr(api_function(), function_name)
        function_data = function(**kwargs)
        indexed_by_name = {}
        for item in self.convert_k8s_list_to_dict(function_data.items):
            item_name = item.get('metadata').get('name')
            indexed_by_name[item_name] = item
        return indexed_by_name

    def call_and_index__apps_v1__list__by_metadata_name(self, function_name, **kwargs):
        return self.call_and_index__api__list__by_metadata_name(self.api_apps_v1, function_name, **kwargs)

    def call_and_index__core_v1__list__by_metadata_name(self, function_name, **kwargs):
        return self.call_and_index__api__list__by_metadata_name(self.api_core_v1, function_name, **kwargs)

    def convert_k8s_list_to_dict(self, target):
        items = []                                                      # do this so that we have easy to manipulate python objects
        for item in target:   # and there doesn't seem to be any advantage of actually using the kubernetes API Resource class (for example methods to use those resources)
            items.append(item.to_dict())
        return items

    # cluster methods

    @index_by
    @group_by
    def api_v1_resources(self):
        return self.convert_k8s_list_to_dict(self.api_apps_v1().get_api_resources().resources)

    @index_by
    @group_by
    def components_status(self):
        return self.call_and_index__core_v1__list__by_metadata_name("list_component_status") #(self.api_core_v1().list_component_status().items)

    def config_maps(self):
        return self.convert_k8s_list_to_dict(self.api_core_v1().list_config_map_for_all_namespaces().items)

    def config_maps_data(self):
        config_maps_data = {}
        for config_map in self.config_maps():
            for data_name, data_value in config_map.get('data').items():
                config_maps_data[data_name] = data_value                     # ok to override since all values are the same
        return config_maps_data

    @index_by
    @group_by
    def config_maps_metadata(self):
        config_maps_metadata = []
        for config_map in self.config_maps():
            config_maps_metadata.append(config_map.get('metadata'))
        return config_maps_metadata

    @index_by
    @group_by
    def core_v1_resources(self):
        return self.convert_k8s_list_to_dict(self.api_core_v1().get_api_resources().resources)

    def daemon_sets(self):
        return self.call_and_index__apps_v1__list__by_metadata_name("list_daemon_set_for_all_namespaces")

    def deployments(self):
        return self.call_and_index__apps_v1__list__by_metadata_name("list_deployment_for_all_namespaces")

    def endpoints(self):
        return self.call_and_index__core_v1__list__by_metadata_name("list_endpoints_for_all_namespaces")

    def events(self, field_selector=None, label_selector=None):
        kwargs = {}
        if field_selector:
            kwargs['field_selector'] = field_selector
        if label_selector:
            kwargs['label_selector'] = label_selector
        result = self.api_core_v1().list_event_for_all_namespaces(**kwargs)
        return self.convert_k8s_list_to_dict(result.items)

    def events_for_namespace(self, namespace):
        return self.api_core_v1().list_namespaced_event()

    def limit_range(self):
        return self.api_core_v1().list_limit_range_for_all_namespaces().to_dict()

    def namespaces(self):
        return self.api_core_v1().list_namespace()

    def pod_events(self, pod_name):
        return self.events(field_selector=f'involvedObject.name={pod_name}')

    def pod_logs(self, pod_name, namespace):
        return self.api_core_v1().read_namespaced_pod_log(name=pod_name, namespace=namespace)

    def pods(self):
        return self.call_and_index__core_v1__list__by_metadata_name("list_pod_for_all_namespaces")

    def pods_in_namespace(self, namespace):
        return self.call_and_index__core_v1__list__by_metadata_name("list_namespaced_pod", namespace=namespace)

    def stateful_sets(self):
        return self.call_and_index__apps_v1__list__by_metadata_name("list_stateful_set_for_all_namespaces")

    def replica_sets(self):
        return self.call_and_index__apps_v1__list__by_metadata_name("list_replica_set_for_all_namespaces")
