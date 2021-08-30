from unittest import TestCase

import pytest

from osbot_k8s.utils.Docker_Desktop_Cluster import DEFAULT_DOCKER_DESKTOP_NAME, DEFAULT_DOCKER_DESKTOP_HOST
from osbot_utils.utils.Dev import pprint
from osbot_utils.utils.Yaml import yaml_parse
from osbot_utils.utils.Files import file_exists
from osbot_utils.utils.Misc import obj_dict, obj_list_set, class_functions_names, list_get_field, list_set, list_index_by
from osbot_k8s.kubernetes.Cluster_Info import Cluster_Info



class test_Cluster_Info(TestCase):

    def setUp(self):
        self.cluster_info = Cluster_Info(config_context=DEFAULT_DOCKER_DESKTOP_NAME)

    def test_api_apps_v1(self):
        apps_api      = self.cluster_info.api_apps_v1()
        api_client    = apps_api.api_client
        configuration = api_client.configuration

        assert class_functions_names(apps_api) == [ '__init__', 'create_namespaced_controller_revision', 'create_namespaced_controller_revision_with_http_info', 'create_namespaced_daemon_set',
                                                    'create_namespaced_daemon_set_with_http_info', 'create_namespaced_deployment', 'create_namespaced_deployment_with_http_info', 'create_namespaced_replica_set',
                                                    'create_namespaced_replica_set_with_http_info', 'create_namespaced_stateful_set', 'create_namespaced_stateful_set_with_http_info',

                                                    'delete_collection_namespaced_controller_revision', 'delete_collection_namespaced_controller_revision_with_http_info', 'delete_collection_namespaced_daemon_set',
                                                    'delete_collection_namespaced_daemon_set_with_http_info', 'delete_collection_namespaced_deployment', 'delete_collection_namespaced_deployment_with_http_info',
                                                    'delete_collection_namespaced_replica_set', 'delete_collection_namespaced_replica_set_with_http_info', 'delete_collection_namespaced_stateful_set', 'delete_collection_namespaced_stateful_set_with_http_info',
                                                    'delete_namespaced_controller_revision', 'delete_namespaced_controller_revision_with_http_info', 'delete_namespaced_daemon_set', 'delete_namespaced_daemon_set_with_http_info', 'delete_namespaced_deployment',
                                                    'delete_namespaced_deployment_with_http_info', 'delete_namespaced_replica_set', 'delete_namespaced_replica_set_with_http_info', 'delete_namespaced_stateful_set', 'delete_namespaced_stateful_set_with_http_info',

                                                    'get_api_resources', 'get_api_resources_with_http_info',

                                                    'list_controller_revision_for_all_namespaces', 'list_controller_revision_for_all_namespaces_with_http_info', 'list_daemon_set_for_all_namespaces', 'list_daemon_set_for_all_namespaces_with_http_info',
                                                    'list_deployment_for_all_namespaces', 'list_deployment_for_all_namespaces_with_http_info', 'list_namespaced_controller_revision', 'list_namespaced_controller_revision_with_http_info', 'list_namespaced_daemon_set',
                                                    'list_namespaced_daemon_set_with_http_info', 'list_namespaced_deployment', 'list_namespaced_deployment_with_http_info', 'list_namespaced_replica_set', 'list_namespaced_replica_set_with_http_info',
                                                    'list_namespaced_stateful_set', 'list_namespaced_stateful_set_with_http_info', 'list_replica_set_for_all_namespaces', 'list_replica_set_for_all_namespaces_with_http_info', 'list_stateful_set_for_all_namespaces',
                                                    'list_stateful_set_for_all_namespaces_with_http_info',

                                                    'patch_namespaced_controller_revision', 'patch_namespaced_controller_revision_with_http_info', 'patch_namespaced_daemon_set', 'patch_namespaced_daemon_set_status', 'patch_namespaced_daemon_set_status_with_http_info',
                                                    'patch_namespaced_daemon_set_with_http_info', 'patch_namespaced_deployment', 'patch_namespaced_deployment_scale', 'patch_namespaced_deployment_scale_with_http_info', 'patch_namespaced_deployment_status',
                                                    'patch_namespaced_deployment_status_with_http_info', 'patch_namespaced_deployment_with_http_info', 'patch_namespaced_replica_set', 'patch_namespaced_replica_set_scale', 'patch_namespaced_replica_set_scale_with_http_info',
                                                    'patch_namespaced_replica_set_status', 'patch_namespaced_replica_set_status_with_http_info', 'patch_namespaced_replica_set_with_http_info', 'patch_namespaced_stateful_set', 'patch_namespaced_stateful_set_scale',
                                                    'patch_namespaced_stateful_set_scale_with_http_info', 'patch_namespaced_stateful_set_status', 'patch_namespaced_stateful_set_status_with_http_info', 'patch_namespaced_stateful_set_with_http_info',

                                                    'read_namespaced_controller_revision', 'read_namespaced_controller_revision_with_http_info', 'read_namespaced_daemon_set', 'read_namespaced_daemon_set_status', 'read_namespaced_daemon_set_status_with_http_info',
                                                    'read_namespaced_daemon_set_with_http_info', 'read_namespaced_deployment', 'read_namespaced_deployment_scale', 'read_namespaced_deployment_scale_with_http_info', 'read_namespaced_deployment_status',
                                                    'read_namespaced_deployment_status_with_http_info', 'read_namespaced_deployment_with_http_info', 'read_namespaced_replica_set', 'read_namespaced_replica_set_scale', 'read_namespaced_replica_set_scale_with_http_info',
                                                    'read_namespaced_replica_set_status', 'read_namespaced_replica_set_status_with_http_info', 'read_namespaced_replica_set_with_http_info', 'read_namespaced_stateful_set', 'read_namespaced_stateful_set_scale',
                                                    'read_namespaced_stateful_set_scale_with_http_info', 'read_namespaced_stateful_set_status', 'read_namespaced_stateful_set_status_with_http_info', 'read_namespaced_stateful_set_with_http_info',

                                                    'replace_namespaced_controller_revision', 'replace_namespaced_controller_revision_with_http_info', 'replace_namespaced_daemon_set', 'replace_namespaced_daemon_set_status', 'replace_namespaced_daemon_set_status_with_http_info',
                                                    'replace_namespaced_daemon_set_with_http_info', 'replace_namespaced_deployment', 'replace_namespaced_deployment_scale', 'replace_namespaced_deployment_scale_with_http_info', 'replace_namespaced_deployment_status',
                                                    'replace_namespaced_deployment_status_with_http_info', 'replace_namespaced_deployment_with_http_info', 'replace_namespaced_replica_set', 'replace_namespaced_replica_set_scale', 'replace_namespaced_replica_set_scale_with_http_info',
                                                    'replace_namespaced_replica_set_status', 'replace_namespaced_replica_set_status_with_http_info', 'replace_namespaced_replica_set_with_http_info', 'replace_namespaced_stateful_set', 'replace_namespaced_stateful_set_scale',
                                                    'replace_namespaced_stateful_set_scale_with_http_info', 'replace_namespaced_stateful_set_status', 'replace_namespaced_stateful_set_status_with_http_info', 'replace_namespaced_stateful_set_with_http_info']

        assert class_functions_names(api_client)  == ['_ApiClient__call_api', '_ApiClient__deserialize', '_ApiClient__deserialize_date', '_ApiClient__deserialize_datetime', '_ApiClient__deserialize_file', '_ApiClient__deserialize_model', '_ApiClient__deserialize_object', '_ApiClient__deserialize_primitive',
                                                      '__enter__', '__exit__', '__init__',
                                                      'call_api', 'close', 'deserialize', 'files_parameters', 'parameters_to_tuples', 'request',
                                                      'sanitize_for_serialization', 'select_header_accept', 'select_header_content_type', 'set_default_header', 'update_params_for_auth']

        assert class_functions_names(configuration) == ['__deepcopy__', '__init__', 'auth_settings', 'get_api_key_with_prefix', 'get_basic_auth_token',
                                                        'get_host_from_settings', 'get_host_settings', 'to_debug_report']

        assert obj_list_set(apps_api     ) == ['api_client']
        assert obj_list_set(api_client   ) == ['client_side_validation', 'configuration', 'cookie', 'default_headers', 'pool_threads', 'rest_client']
        assert obj_list_set(configuration) == ['_Configuration__debug', '_Configuration__logger_file', '_Configuration__logger_format', 'api_key', 'api_key_prefix',
                                               'assert_hostname', 'cert_file', 'client_side_validation', 'connection_pool_maxsize', 'discard_unknown_keys',
                                               'host', 'key_file', 'logger', 'logger_formatter', 'logger_stream_handler', 'password', 'proxy', 'proxy_headers',
                                               'refresh_api_key_hook', 'retries', 'safe_chars_for_path_param', 'ssl_ca_cert', 'temp_folder_path', 'username', 'verify_ssl']

        assert obj_dict(api_client       ) == {'configuration'          : api_client.configuration                          ,
                                               'pool_threads'           : 1                                                 ,
                                               'rest_client'            : api_client.rest_client                            ,
                                               'default_headers'        : {'User-Agent': 'OpenAPI-Generator/18.20.0/python'},
                                               'cookie'                 : None                                              ,
                                               'client_side_validation' : True                                              ,
                                               '_pool'                  : api_client.pool                                   }


        assert file_exists(configuration.cert_file  )
        assert file_exists(configuration.key_file   )
        assert file_exists(configuration.ssl_ca_cert)

        del configuration.cert_file
        del configuration.key_file
        del configuration.ssl_ca_cert

        assert obj_dict(configuration) == {  'host'                         : DEFAULT_DOCKER_DESKTOP_HOST,
                                             'temp_folder_path'             : None,
                                             'api_key'                      : {},
                                             'api_key_prefix'               : {},
                                             'refresh_api_key_hook'         : None,
                                             'username'                     : None, 'password': None,
                                             'discard_unknown_keys'         : False,
                                             '_Configuration__logger_format': '%(asctime)s %(levelname)s %(message)s',
                                             'logger_formatter'             : configuration.logger_formatter,
                                             'logger_stream_handler'        : None,
                                             '_Configuration__logger_file': None,
                                             '_Configuration__debug'        : False,
                                             'verify_ssl'                   : True,
                                             'assert_hostname'              : None,
                                             'connection_pool_maxsize'      : 40,
                                             'proxy'                        : None,
                                             'proxy_headers'                : None,
                                             'safe_chars_for_path_param'    : '',
                                             'retries'                      : None,
                                             'client_side_validation'       : True,
                                             'logger'                       : {'package_logger': configuration.logger.get('package_logger'), 'urllib3_logger': configuration.logger.get('urllib3_logger')}}

    def test_api_core_v1(self):
        core_api      = self.cluster_info.api_core_v1()
        api_client    = core_api.api_client

        assert class_functions_names(core_api) == ['__init__',
                                                   'connect_delete_namespaced_pod_proxy', 'connect_delete_namespaced_pod_proxy_with_http_info', 'connect_delete_namespaced_pod_proxy_with_path',
                                                   'connect_delete_namespaced_pod_proxy_with_path_with_http_info', 'connect_delete_namespaced_service_proxy', 'connect_delete_namespaced_service_proxy_with_http_info',
                                                   'connect_delete_namespaced_service_proxy_with_path', 'connect_delete_namespaced_service_proxy_with_path_with_http_info', 'connect_delete_node_proxy',
                                                   'connect_delete_node_proxy_with_http_info', 'connect_delete_node_proxy_with_path', 'connect_delete_node_proxy_with_path_with_http_info',
                                                   'connect_get_namespaced_pod_attach', 'connect_get_namespaced_pod_attach_with_http_info', 'connect_get_namespaced_pod_exec',
                                                   'connect_get_namespaced_pod_exec_with_http_info', 'connect_get_namespaced_pod_portforward', 'connect_get_namespaced_pod_portforward_with_http_info',
                                                   'connect_get_namespaced_pod_proxy', 'connect_get_namespaced_pod_proxy_with_http_info', 'connect_get_namespaced_pod_proxy_with_path',
                                                   'connect_get_namespaced_pod_proxy_with_path_with_http_info', 'connect_get_namespaced_service_proxy', 'connect_get_namespaced_service_proxy_with_http_info',
                                                   'connect_get_namespaced_service_proxy_with_path', 'connect_get_namespaced_service_proxy_with_path_with_http_info', 'connect_get_node_proxy',
                                                   'connect_get_node_proxy_with_http_info', 'connect_get_node_proxy_with_path', 'connect_get_node_proxy_with_path_with_http_info',
                                                   'connect_head_namespaced_pod_proxy', 'connect_head_namespaced_pod_proxy_with_http_info', 'connect_head_namespaced_pod_proxy_with_path',
                                                   'connect_head_namespaced_pod_proxy_with_path_with_http_info', 'connect_head_namespaced_service_proxy',
                                                   'connect_head_namespaced_service_proxy_with_http_info', 'connect_head_namespaced_service_proxy_with_path', 'connect_head_namespaced_service_proxy_with_path_with_http_info',
                                                   'connect_head_node_proxy', 'connect_head_node_proxy_with_http_info', 'connect_head_node_proxy_with_path', 'connect_head_node_proxy_with_path_with_http_info',
                                                   'connect_options_namespaced_pod_proxy', 'connect_options_namespaced_pod_proxy_with_http_info', 'connect_options_namespaced_pod_proxy_with_path',
                                                   'connect_options_namespaced_pod_proxy_with_path_with_http_info', 'connect_options_namespaced_service_proxy', 'connect_options_namespaced_service_proxy_with_http_info',
                                                   'connect_options_namespaced_service_proxy_with_path', 'connect_options_namespaced_service_proxy_with_path_with_http_info', 'connect_options_node_proxy',
                                                   'connect_options_node_proxy_with_http_info', 'connect_options_node_proxy_with_path', 'connect_options_node_proxy_with_path_with_http_info',
                                                   'connect_patch_namespaced_pod_proxy', 'connect_patch_namespaced_pod_proxy_with_http_info', 'connect_patch_namespaced_pod_proxy_with_path',
                                                   'connect_patch_namespaced_pod_proxy_with_path_with_http_info', 'connect_patch_namespaced_service_proxy', 'connect_patch_namespaced_service_proxy_with_http_info',
                                                   'connect_patch_namespaced_service_proxy_with_path', 'connect_patch_namespaced_service_proxy_with_path_with_http_info', 'connect_patch_node_proxy',
                                                   'connect_patch_node_proxy_with_http_info', 'connect_patch_node_proxy_with_path', 'connect_patch_node_proxy_with_path_with_http_info',
                                                   'connect_post_namespaced_pod_attach', 'connect_post_namespaced_pod_attach_with_http_info', 'connect_post_namespaced_pod_exec',
                                                   'connect_post_namespaced_pod_exec_with_http_info', 'connect_post_namespaced_pod_portforward', 'connect_post_namespaced_pod_portforward_with_http_info',
                                                   'connect_post_namespaced_pod_proxy', 'connect_post_namespaced_pod_proxy_with_http_info', 'connect_post_namespaced_pod_proxy_with_path',
                                                   'connect_post_namespaced_pod_proxy_with_path_with_http_info', 'connect_post_namespaced_service_proxy', 'connect_post_namespaced_service_proxy_with_http_info',
                                                   'connect_post_namespaced_service_proxy_with_path', 'connect_post_namespaced_service_proxy_with_path_with_http_info', 'connect_post_node_proxy',
                                                   'connect_post_node_proxy_with_http_info', 'connect_post_node_proxy_with_path', 'connect_post_node_proxy_with_path_with_http_info',
                                                   'connect_put_namespaced_pod_proxy', 'connect_put_namespaced_pod_proxy_with_http_info', 'connect_put_namespaced_pod_proxy_with_path',
                                                   'connect_put_namespaced_pod_proxy_with_path_with_http_info', 'connect_put_namespaced_service_proxy', 'connect_put_namespaced_service_proxy_with_http_info',
                                                   'connect_put_namespaced_service_proxy_with_path', 'connect_put_namespaced_service_proxy_with_path_with_http_info', 'connect_put_node_proxy',
                                                   'connect_put_node_proxy_with_http_info', 'connect_put_node_proxy_with_path', 'connect_put_node_proxy_with_path_with_http_info',

                                                   'create_namespace', 'create_namespace_with_http_info', 'create_namespaced_binding', 'create_namespaced_binding_with_http_info',
                                                   'create_namespaced_config_map', 'create_namespaced_config_map_with_http_info', 'create_namespaced_endpoints', 'create_namespaced_endpoints_with_http_info',
                                                   'create_namespaced_event', 'create_namespaced_event_with_http_info', 'create_namespaced_limit_range', 'create_namespaced_limit_range_with_http_info',
                                                   'create_namespaced_persistent_volume_claim', 'create_namespaced_persistent_volume_claim_with_http_info', 'create_namespaced_pod',
                                                   'create_namespaced_pod_binding', 'create_namespaced_pod_binding_with_http_info', 'create_namespaced_pod_eviction',
                                                   'create_namespaced_pod_eviction_with_http_info', 'create_namespaced_pod_template', 'create_namespaced_pod_template_with_http_info',
                                                   'create_namespaced_pod_with_http_info', 'create_namespaced_replication_controller', 'create_namespaced_replication_controller_with_http_info',
                                                   'create_namespaced_resource_quota', 'create_namespaced_resource_quota_with_http_info', 'create_namespaced_secret',
                                                   'create_namespaced_secret_with_http_info', 'create_namespaced_service', 'create_namespaced_service_account', 'create_namespaced_service_account_token',
                                                   'create_namespaced_service_account_token_with_http_info', 'create_namespaced_service_account_with_http_info', 'create_namespaced_service_with_http_info',
                                                   'create_node', 'create_node_with_http_info', 'create_persistent_volume', 'create_persistent_volume_with_http_info',

                                                   'delete_collection_namespaced_config_map', 'delete_collection_namespaced_config_map_with_http_info', 'delete_collection_namespaced_endpoints',
                                                   'delete_collection_namespaced_endpoints_with_http_info', 'delete_collection_namespaced_event', 'delete_collection_namespaced_event_with_http_info',
                                                   'delete_collection_namespaced_limit_range', 'delete_collection_namespaced_limit_range_with_http_info', 'delete_collection_namespaced_persistent_volume_claim',
                                                   'delete_collection_namespaced_persistent_volume_claim_with_http_info', 'delete_collection_namespaced_pod', 'delete_collection_namespaced_pod_template',
                                                   'delete_collection_namespaced_pod_template_with_http_info', 'delete_collection_namespaced_pod_with_http_info', 'delete_collection_namespaced_replication_controller',
                                                   'delete_collection_namespaced_replication_controller_with_http_info', 'delete_collection_namespaced_resource_quota',
                                                   'delete_collection_namespaced_resource_quota_with_http_info', 'delete_collection_namespaced_secret', 'delete_collection_namespaced_secret_with_http_info',
                                                   'delete_collection_namespaced_service_account', 'delete_collection_namespaced_service_account_with_http_info', 'delete_collection_node',
                                                   'delete_collection_node_with_http_info', 'delete_collection_persistent_volume', 'delete_collection_persistent_volume_with_http_info',
                                                   'delete_namespace', 'delete_namespace_with_http_info', 'delete_namespaced_config_map', 'delete_namespaced_config_map_with_http_info',
                                                   'delete_namespaced_endpoints', 'delete_namespaced_endpoints_with_http_info', 'delete_namespaced_event', 'delete_namespaced_event_with_http_info',
                                                   'delete_namespaced_limit_range', 'delete_namespaced_limit_range_with_http_info', 'delete_namespaced_persistent_volume_claim',
                                                   'delete_namespaced_persistent_volume_claim_with_http_info', 'delete_namespaced_pod', 'delete_namespaced_pod_template',
                                                   'delete_namespaced_pod_template_with_http_info', 'delete_namespaced_pod_with_http_info', 'delete_namespaced_replication_controller',
                                                   'delete_namespaced_replication_controller_with_http_info', 'delete_namespaced_resource_quota', 'delete_namespaced_resource_quota_with_http_info',
                                                   'delete_namespaced_secret', 'delete_namespaced_secret_with_http_info', 'delete_namespaced_service', 'delete_namespaced_service_account',
                                                   'delete_namespaced_service_account_with_http_info', 'delete_namespaced_service_with_http_info', 'delete_node', 'delete_node_with_http_info',
                                                   'delete_persistent_volume', 'delete_persistent_volume_with_http_info',

                                                   'get_api_resources', 'get_api_resources_with_http_info',

                                                   'list_component_status', 'list_component_status_with_http_info', 'list_config_map_for_all_namespaces', 'list_config_map_for_all_namespaces_with_http_info',
                                                   'list_endpoints_for_all_namespaces', 'list_endpoints_for_all_namespaces_with_http_info', 'list_event_for_all_namespaces', 'list_event_for_all_namespaces_with_http_info',
                                                   'list_limit_range_for_all_namespaces', 'list_limit_range_for_all_namespaces_with_http_info', 'list_namespace', 'list_namespace_with_http_info',
                                                   'list_namespaced_config_map', 'list_namespaced_config_map_with_http_info', 'list_namespaced_endpoints', 'list_namespaced_endpoints_with_http_info',
                                                   'list_namespaced_event', 'list_namespaced_event_with_http_info', 'list_namespaced_limit_range', 'list_namespaced_limit_range_with_http_info',
                                                   'list_namespaced_persistent_volume_claim', 'list_namespaced_persistent_volume_claim_with_http_info', 'list_namespaced_pod',
                                                   'list_namespaced_pod_template', 'list_namespaced_pod_template_with_http_info', 'list_namespaced_pod_with_http_info',
                                                   'list_namespaced_replication_controller', 'list_namespaced_replication_controller_with_http_info', 'list_namespaced_resource_quota',
                                                   'list_namespaced_resource_quota_with_http_info', 'list_namespaced_secret', 'list_namespaced_secret_with_http_info', 'list_namespaced_service',
                                                   'list_namespaced_service_account', 'list_namespaced_service_account_with_http_info', 'list_namespaced_service_with_http_info', 'list_node',
                                                   'list_node_with_http_info', 'list_persistent_volume', 'list_persistent_volume_claim_for_all_namespaces', 'list_persistent_volume_claim_for_all_namespaces_with_http_info',
                                                   'list_persistent_volume_with_http_info', 'list_pod_for_all_namespaces', 'list_pod_for_all_namespaces_with_http_info', 'list_pod_template_for_all_namespaces',
                                                   'list_pod_template_for_all_namespaces_with_http_info', 'list_replication_controller_for_all_namespaces', 'list_replication_controller_for_all_namespaces_with_http_info',
                                                   'list_resource_quota_for_all_namespaces', 'list_resource_quota_for_all_namespaces_with_http_info', 'list_secret_for_all_namespaces',
                                                   'list_secret_for_all_namespaces_with_http_info', 'list_service_account_for_all_namespaces', 'list_service_account_for_all_namespaces_with_http_info',
                                                   'list_service_for_all_namespaces', 'list_service_for_all_namespaces_with_http_info',

                                                   'patch_namespace', 'patch_namespace_status', 'patch_namespace_status_with_http_info', 'patch_namespace_with_http_info', 'patch_namespaced_config_map',
                                                   'patch_namespaced_config_map_with_http_info', 'patch_namespaced_endpoints', 'patch_namespaced_endpoints_with_http_info', 'patch_namespaced_event',
                                                   'patch_namespaced_event_with_http_info', 'patch_namespaced_limit_range', 'patch_namespaced_limit_range_with_http_info', 'patch_namespaced_persistent_volume_claim',
                                                   'patch_namespaced_persistent_volume_claim_status', 'patch_namespaced_persistent_volume_claim_status_with_http_info', 'patch_namespaced_persistent_volume_claim_with_http_info',
                                                   'patch_namespaced_pod', 'patch_namespaced_pod_status', 'patch_namespaced_pod_status_with_http_info', 'patch_namespaced_pod_template', 'patch_namespaced_pod_template_with_http_info',
                                                   'patch_namespaced_pod_with_http_info', 'patch_namespaced_replication_controller', 'patch_namespaced_replication_controller_scale', 'patch_namespaced_replication_controller_scale_with_http_info',
                                                   'patch_namespaced_replication_controller_status', 'patch_namespaced_replication_controller_status_with_http_info', 'patch_namespaced_replication_controller_with_http_info',
                                                   'patch_namespaced_resource_quota', 'patch_namespaced_resource_quota_status', 'patch_namespaced_resource_quota_status_with_http_info', 'patch_namespaced_resource_quota_with_http_info',
                                                   'patch_namespaced_secret', 'patch_namespaced_secret_with_http_info', 'patch_namespaced_service', 'patch_namespaced_service_account', 'patch_namespaced_service_account_with_http_info',
                                                   'patch_namespaced_service_status', 'patch_namespaced_service_status_with_http_info', 'patch_namespaced_service_with_http_info', 'patch_node',
                                                   'patch_node_status', 'patch_node_status_with_http_info', 'patch_node_with_http_info', 'patch_persistent_volume', 'patch_persistent_volume_status',
                                                   'patch_persistent_volume_status_with_http_info', 'patch_persistent_volume_with_http_info',

                                                   'read_component_status', 'read_component_status_with_http_info', 'read_namespace', 'read_namespace_status', 'read_namespace_status_with_http_info',
                                                   'read_namespace_with_http_info', 'read_namespaced_config_map', 'read_namespaced_config_map_with_http_info', 'read_namespaced_endpoints',
                                                   'read_namespaced_endpoints_with_http_info', 'read_namespaced_event', 'read_namespaced_event_with_http_info', 'read_namespaced_limit_range',
                                                   'read_namespaced_limit_range_with_http_info', 'read_namespaced_persistent_volume_claim', 'read_namespaced_persistent_volume_claim_status',
                                                   'read_namespaced_persistent_volume_claim_status_with_http_info', 'read_namespaced_persistent_volume_claim_with_http_info',
                                                   'read_namespaced_pod', 'read_namespaced_pod_log', 'read_namespaced_pod_log_with_http_info', 'read_namespaced_pod_status',
                                                   'read_namespaced_pod_status_with_http_info', 'read_namespaced_pod_template', 'read_namespaced_pod_template_with_http_info',
                                                   'read_namespaced_pod_with_http_info', 'read_namespaced_replication_controller', 'read_namespaced_replication_controller_scale',
                                                   'read_namespaced_replication_controller_scale_with_http_info', 'read_namespaced_replication_controller_status',
                                                   'read_namespaced_replication_controller_status_with_http_info', 'read_namespaced_replication_controller_with_http_info',
                                                   'read_namespaced_resource_quota', 'read_namespaced_resource_quota_status', 'read_namespaced_resource_quota_status_with_http_info',
                                                   'read_namespaced_resource_quota_with_http_info', 'read_namespaced_secret', 'read_namespaced_secret_with_http_info', 'read_namespaced_service',
                                                   'read_namespaced_service_account', 'read_namespaced_service_account_with_http_info', 'read_namespaced_service_status',
                                                   'read_namespaced_service_status_with_http_info', 'read_namespaced_service_with_http_info', 'read_node', 'read_node_status',
                                                   'read_node_status_with_http_info', 'read_node_with_http_info', 'read_persistent_volume', 'read_persistent_volume_status',
                                                   'read_persistent_volume_status_with_http_info', 'read_persistent_volume_with_http_info',

                                                   'replace_namespace', 'replace_namespace_finalize', 'replace_namespace_finalize_with_http_info', 'replace_namespace_status',
                                                   'replace_namespace_status_with_http_info', 'replace_namespace_with_http_info', 'replace_namespaced_config_map', 'replace_namespaced_config_map_with_http_info',
                                                   'replace_namespaced_endpoints', 'replace_namespaced_endpoints_with_http_info', 'replace_namespaced_event', 'replace_namespaced_event_with_http_info',
                                                   'replace_namespaced_limit_range', 'replace_namespaced_limit_range_with_http_info', 'replace_namespaced_persistent_volume_claim',
                                                   'replace_namespaced_persistent_volume_claim_status', 'replace_namespaced_persistent_volume_claim_status_with_http_info',
                                                   'replace_namespaced_persistent_volume_claim_with_http_info', 'replace_namespaced_pod', 'replace_namespaced_pod_status',
                                                   'replace_namespaced_pod_status_with_http_info', 'replace_namespaced_pod_template', 'replace_namespaced_pod_template_with_http_info',
                                                   'replace_namespaced_pod_with_http_info', 'replace_namespaced_replication_controller', 'replace_namespaced_replication_controller_scale',
                                                   'replace_namespaced_replication_controller_scale_with_http_info', 'replace_namespaced_replication_controller_status',
                                                   'replace_namespaced_replication_controller_status_with_http_info', 'replace_namespaced_replication_controller_with_http_info',
                                                   'replace_namespaced_resource_quota', 'replace_namespaced_resource_quota_status', 'replace_namespaced_resource_quota_status_with_http_info',
                                                   'replace_namespaced_resource_quota_with_http_info', 'replace_namespaced_secret', 'replace_namespaced_secret_with_http_info',
                                                   'replace_namespaced_service', 'replace_namespaced_service_account', 'replace_namespaced_service_account_with_http_info',
                                                   'replace_namespaced_service_status', 'replace_namespaced_service_status_with_http_info', 'replace_namespaced_service_with_http_info',
                                                   'replace_node', 'replace_node_status', 'replace_node_status_with_http_info', 'replace_node_with_http_info', 'replace_persistent_volume',
                                                   'replace_persistent_volume_status', 'replace_persistent_volume_status_with_http_info', 'replace_persistent_volume_with_http_info']

        assert obj_list_set(api_client) == [ 'client_side_validation', 'configuration', 'cookie', 'default_headers', 'pool_threads', 'rest_client']
        assert api_client.client_side_validation is True

        core_api_configuration = obj_dict(api_client.configuration)
        apps_api_configuration = obj_dict(self.cluster_info.api_apps_v1().api_client.configuration)
        del core_api_configuration['logger_formatter']                  # apart from this field
        del apps_api_configuration['logger_formatter']                  # the configuration values are the same
        assert core_api_configuration == apps_api_configuration         # and the values of apps_api_configuration are tested by test_api_apps_v1

    def test_api_v1_resources(self):
        resources = self.cluster_info.api_v1_resources()
        for resource in resources:
            assert list_set(resource) == ['categories','group','kind','name','namespaced','short_names',
                                          'singular_name','storage_version_hash','verbs','version']

        assert list_set(list_index_by(resources, 'name')) == ['controllerrevisions', 'daemonsets', 'daemonsets/status',
                                                              'deployments', 'deployments/scale', 'deployments/status',
                                                              'replicasets', 'replicasets/scale', 'replicasets/status',
                                                              'statefulsets', 'statefulsets/scale', 'statefulsets/status']

    def test_component_status(self):
        components_status = self.cluster_info.components_status()
        for component_status in components_status.values():
             assert list_set(component_status) == ['api_version', 'conditions', 'kind', 'metadata']
        assert list_set(components_status) == ['controller-manager', 'etcd-0', 'scheduler']

    def test_config_maps(self):
        for item in self.cluster_info.config_maps():
            assert list_set(item) == ['api_version', 'binary_data', 'data', 'immutable', 'kind', 'metadata']
            assert item.get('api_version') is None
            assert item.get('binary_data') is None
            assert item.get('immutable'  ) is None
            assert item.get('kind'       ) is None

            # data
            # assert list_set(item.get('data')) in [['ca.crt'                                                                         ],
            #                                       ['jws-kubeconfig-abcdef', 'kubeconfig'                                            ],
            #                                       ['Corefile'                                                                       ],
            #                                       ['client-ca-file', 'requestheader-allowed-names', 'requestheader-client-ca-file',
            #                                        'requestheader-extra-headers-prefix', 'requestheader-group-headers',
            #                                        'requestheader-username-headers'                                                 ],
            #                                       ['config.conf', 'kubeconfig.conf'                                                 ],
            #                                       ['ClusterConfiguration', 'ClusterStatus'                                          ],
            #                                       ['kubelet'                                                                        ],
            #                                       ['prometheus.yaml'                                                                ],
            #                                       ['alertmanager.rules.yaml', 'etcd3.rules.yaml', 'general.rules.yaml',
            #                                        'kube-state-metrics.rules.yaml', 'kubelet.rules.yaml',
            #                                        'kubernetes.rules.yaml', 'node.rules.yaml', 'prometheus.rules.yaml'              ]]
            # metadata
            assert list_set(item.get('metadata')) == [ 'annotations', 'cluster_name', 'creation_timestamp',
                                                       'deletion_grace_period_seconds', 'deletion_timestamp',
                                                       'finalizers', 'generate_name', 'generation', 'labels',
                                                       'managed_fields', 'name', 'namespace', 'owner_references',
                                                       'resource_version', 'self_link', 'uid']
        # confirm that every entry in config_map.ata is the same
        config_maps_data = {}
        for config_map in self.cluster_info.config_maps():
            for data_name, data_value in config_map.get('data').items():
                if config_maps_data.get(data_name) is None:                    # only add if it doesn't exist
                    config_maps_data[data_name] = data_value
                else:
                    assert config_maps_data[data_name] == data_value           # if it exists, it should be the same


        # assert item.get('metadata'   ) == None
        # pprint(yaml_parse(data.get('requestheader-username-headers')))
        # pprint(yaml_parse(data.get('alertmanager.rules.yaml')))
        # pprint(yaml_parse(data.get('Corefile')))

    def test_config_maps_data(self):
        data = self.cluster_info.config_maps_data()
        assert list_set(data) == [ 'ClusterConfiguration',  'ClusterStatus',  'Corefile',
                                   'alertmanager.rules.yaml',  'ca.crt',  'client-ca-file',  'config.conf',
                                   'etcd3.rules.yaml',  'general.rules.yaml',
                                   'kube-state-metrics.rules.yaml',  'kubeconfig',  'kubeconfig.conf',
                                   'kubelet',  'kubelet.rules.yaml',  'kubernetes.rules.yaml',  'node.rules.yaml',
                                   'prometheus.rules.yaml',  'prometheus.yaml',  'requestheader-allowed-names',
                                   'requestheader-client-ca-file',  'requestheader-extra-headers-prefix',
                                   'requestheader-group-headers',  'requestheader-username-headers']

        assert yaml_parse(data.get('ClusterConfiguration')) == {  'apiServer'           : { 'extraArgs'             : { 'authorization-mode'      : 'Node,RBAC'      ,
                                                                                                                        'enable-admission-plugins': 'NodeRestriction',
                                                                                                                        'watch-cache'             : 'false'         },
                                                                                            'timeoutForControlPlane': '4m0s'},
                                                                  'apiVersion'          : 'kubeadm.k8s.io/v1beta2',
                                                                  'certificatesDir'     : '/run/config/pki',
                                                                  'clusterName'         : 'kubernetes',
                                                                  'controlPlaneEndpoint': 'vm.docker.internal:6443',
                                                                  'controllerManager'   : { 'extraArgs': {  'horizontal-pod-autoscaler-sync-period' : '60s'     ,
                                                                                                            'leader-elect'                          : 'false'   ,
                                                                                                            'node-monitor-grace-period'             : '180s'    ,
                                                                                                            'node-monitor-period'                   : '30s'     ,
                                                                                                            'pvclaimbinder-sync-period'             : '60s'     }},
                                                                  'dns'                 : {'type': 'CoreDNS'                    },
                                                                  'etcd'                : {'local': {'dataDir': '/var/lib/etcd'}},
                                                                  'imageRepository'     : 'k8s.gcr.io'                           ,
                                                                  'kind'                : 'ClusterConfiguration'                 ,
                                                                  'kubernetesVersion'   : 'v1.21.2'                              ,
                                                                  'networking'          : {'dnsDomain': 'cluster.local', 'serviceSubnet': '10.96.0.0/12'},
                                                                  'scheduler'           : {}}

        assert list_set(yaml_parse(data.get('ClusterStatus'))) == ['apiEndpoints', 'apiVersion', 'kind']
        assert data.get('Corefile')  == ('.:53 {\n'             # this is in a weird non-json or non-yaml core-dns format https://coredns.io/2017/07/23/corefile-explained/
                                         '    errors\n'
                                         '    health {\n'
                                         '       lameduck 5s\n'
                                         '    }\n'
                                         '    ready\n'
                                         '    kubernetes cluster.local in-addr.arpa ip6.arpa {\n'
                                         '       pods insecure\n'
                                         '       fallthrough in-addr.arpa ip6.arpa\n'
                                         '       ttl 30\n'
                                         '    }\n'
                                         '    prometheus :9153\n'
                                         '    forward . /etc/resolv.conf {\n'
                                         '       max_concurrent 1000\n'
                                         '    }\n'
                                         '    cache 30\n'
                                         '    loop\n'
                                         '    reload\n'
                                         '    loadbalance\n'
                                         '}\n')
        assert yaml_parse(data.get('alertmanager.rules.yaml')) == { 'groups': [ { 'name': 'alertmanager.rules',
                'rules': [ { 'alert'        : 'AlertmanagerConfigInconsistent',
                             'annotations'  : { 'description': 'The configuration of the instances of the Alertmanager cluster `{{$labels.service}}` are out of sync.'},
                             'expr'         : 'count_values("config_hash", alertmanager_config_hash) BY (service) / ON(service) GROUP_LEFT() label_replace(prometheus_operator_alertmanager_spec_replicas, "service", "alertmanager-$1", "alertmanager", "(.*)") != 1',
                             'for'          : '5m',
                             'labels'       : {'severity': 'critical'}},
                           { 'alert'        : 'AlertmanagerDownOrMissing',
                             'annotations'  : { 'description': 'An unexpected number of Alertmanagers are scraped or Alertmanagers disappeared from discovery.'},
                             'expr'         : 'label_replace(prometheus_operator_alertmanager_spec_replicas, "job", "alertmanager-$1", "alertmanager", "(.*)") / ON(job) GROUP_RIGHT() sum(up) BY (job) != 1',
                             'for'          : '5m',
                             'labels'       : {'severity': 'warning'}},
                           { 'alert'        : 'AlertmanagerFailedReload',
                             'annotations'  : { 'description': "Reloading Alertmanager's configuration has failed for {{ $labels.namespace }}/{{ $labels.pod}}."},
                             'expr'         : 'alertmanager_config_last_reload_successful == 0',
                             'for'          : '10m',
                             'labels'       : {'severity': 'warning'}}]}]}

        assert data.get('ca.crt'        ).startswith('-----BEGIN CERTIFICATE-----\n')
        assert data.get('client-ca-file').startswith('-----BEGIN CERTIFICATE-----\n')
        assert data.get('ca.crt'        ) == data.get('client-ca-file')                 # interesting that these values are the same

        assert yaml_parse(data.get('config.conf')) == { 'apiVersion'            : 'kubeproxy.config.k8s.io/v1alpha1',
                                                        'bindAddress'           : '0.0.0.0' ,
                                                        'bindAddressHardFail'   : False     ,
                                                        'clientConnection'      : {'acceptContentTypes' : ''                                    ,
                                                                                   'burst'              : 10                                    ,
                                                                                   'contentType'        : 'application/vnd.kubernetes.protobuf' ,
                                                                                   'kubeconfig'         : '/var/lib/kube-proxy/kubeconfig.conf' ,
                                                                                   'qps': 5},
                                                        'clusterCIDR'           : '',
                                                        'configSyncPeriod'      : '15m0s',
                                                        'conntrack'             : {'maxPerCore'             : 0         ,
                                                                                   'min'                    : 0         ,
                                                                                   'tcpCloseWaitTimeout'    : '1h0m0s'  ,
                                                                                   'tcpEstablishedTimeout'  : '24h0m0s' },
                                                        'detectLocalMode'       : ''             ,
                                                        'enableProfiling'       : False          ,
                                                        'healthzBindAddress'    : '0.0.0.0:10256',
                                                        'hostnameOverride'      : ''             ,
                                                        'iptables'              : {'masqueradeAll'  : False ,
                                                                                   'masqueradeBit'  : 14    ,
                                                                                   'minSyncPeriod'  : '0s'  ,
                                                                                   'syncPeriod'     : '30s' },
                                                        'ipvs'                  : {'excludeCIDRs'   : None  ,
                                                                                   'minSyncPeriod'  : '0s'  ,
                                                                                   'scheduler'      : ''    ,
                                                                                   'strictARP'      : False ,
                                                                                   'syncPeriod'     : '30s' ,
                                                                                   'tcpFinTimeout'  : '0s'  ,
                                                                                   'tcpTimeout'     : '0s'  ,
                                                                                   'udpTimeout'     : '0s'  },
                                                        'kind'                  : 'KubeProxyConfiguration',
                                                        'metricsBindAddress'    : '127.0.0.1:10249',
                                                        'mode'                  : '',
                                                        'nodePortAddresses'     : None,
                                                        'oomScoreAdj'           : -999,
                                                        'portRange'             : '',
                                                        'showHiddenMetricsForVersion': '',
                                                        'udpIdleTimeout'        : '250ms',
                                                        'winkernel'             : {'enableDSR': False, 'networkName': '', 'sourceVip': ''}}
        assert yaml_parse(data.get('etcd3.rules.yaml')) == {'groups': [{'name': './etcd3.rules',
                                                            'rules': [{'alert'      : 'InsufficientMembers',
                                                                       'annotations': {'description': 'If one more etcd member goes down the cluster will be unavailable',
                                                                                       'summary'    : 'etcd cluster insufficient members'},
                                                                       'expr'       : 'count(up{job="etcd"} == 0) > (count(up{job="etcd"}) / 2 - 1)',
                                                                       'for'        : '3m',
                                                                       'labels'     : {'severity': 'critical'}},
                                                                      {'alert'      : 'NoLeader',
                                                                       'annotations': {'description': 'etcd member {{ $labels.instance }} has no leader',
                                                                                       'summary'    : 'etcd member has no leader'},
                                                                       'expr'       : 'etcd_server_has_leader{job="etcd"} == 0',
                                                                       'for'        : '1m',
                                                                       'labels'     : {'severity': 'critical'}},
                                                                      {'alert'      : 'HighNumberOfLeaderChanges',
                                                                       'annotations': {'description': 'etcd instance {{ $labels.instance }} has seen {{ $value }} leader changes within the last hour',
                                                                                       'summary'    : 'a high number of leader changes within the etcd cluster are happening'},
                                                                       'expr'       : 'increase(etcd_server_leader_changes_seen_total{job="etcd"}[1h]) > 3',
                                                                       'labels'     : {'severity': 'warning'}},
                                                                      {'alert'      : 'GRPCRequestsSlow',
                                                                       'annotations': {'description': 'on etcd instance {{ $labels.instance }} gRPC requests to {{ $labels.grpc_method }} are slow',
                                                                                       'summary'    : 'slow gRPC requests'},
                                                                       'expr'       : 'histogram_quantile(0.99, sum(rate(grpc_server_handling_seconds_bucket{job="etcd",grpc_type="unary"}[5m])) by (grpc_service, grpc_method, le)) > 0.15',
                                                                       'for'        : '10m',
                                                                       'labels'     : {'severity': 'critical'}},
                                                                      {'alert'      : 'HighNumberOfFailedHTTPRequests',
                                                                       'annotations': {'description': '{{ $value }}% of requests for {{ $labels.method }} failed on etcd instance {{ $labels.instance }}',
                                                                                       'summary'    : 'a high number of HTTP requests are failing'},
                                                                       'expr'       : 'sum(rate(etcd_http_failed_total{job="etcd"}[5m])) BY (method) / sum(rate(etcd_http_received_total{job="etcd"}[5m])) BY (method) > 0.01',
                                                                       'for'        : '10m',
                                                                       'labels'     : {'severity': 'warning'}},
                                                                      {'alert'      : 'HighNumberOfFailedHTTPRequests',
                                                                       'annotations': {'description': '{{ $value }}% of requests for {{ $labels.method }} failed on etcd instance {{ $labels.instance }}',
                                                                                       'summary'    : 'a high number of HTTP requests are failing'},
                                                                       'expr'       : 'sum(rate(etcd_http_failed_total{job="etcd"}[5m])) BY (method) / sum(rate(etcd_http_received_total{job="etcd"}[5m])) BY (method) > 0.05',
                                                                       'for'        : '5m',
                                                                       'labels' : {'severity': 'critical'}},
                                                                      {'alert'      : 'HTTPRequestsSlow',
                                                                       'annotations': {'description': 'on etcd instance {{ $labels.instance }} HTTP requests to {{ $labels.method }} are slow',
                                                                                       'summary'    : 'slow HTTP requests'},
                                                                       'expr'       : 'histogram_quantile(0.99, rate(etcd_http_successful_duration_seconds_bucket[5m])) > 0.15',
                                                                       'for'        : '10m',
                                                                       'labels'     : {'severity': 'warning'}},
                                                                      {'alert'      : 'EtcdMemberCommunicationSlow',
                                                                       'annotations': {'description': 'etcd instance {{ $labels.instance }} member communication with {{ $labels.To }} is slow',
                                                                                       'summary'    : 'etcd member communication is slow'},
                                                                       'expr'       : 'histogram_quantile(0.99, rate(etcd_network_peer_round_trip_time_seconds_bucket[5m])) > 0.15',
                                                                       'for'        : '10m',
                                                                       'labels'     : {'severity': 'warning'}},
                                                                      {'alert'      : 'HighNumberOfFailedProposals',
                                                                       'annotations': {'description': 'etcd instance {{ $labels.instance }} has seen {{ $value }} proposal failures within the last hour',
                                                                                       'summary'    : 'a high number of proposals within the etcd cluster are failing'},
                                                                       'expr'       : 'increase(etcd_server_proposals_failed_total{job="etcd"}[1h]) > 5',
                                                                       'labels'     : {'severity': 'warning'}},
                                                                      {'alert'      : 'HighFsyncDurations',
                                                                       'annotations': {'description': 'etcd instance {{ $labels.instance }} fync durations are high',
                                                                                       'summary': 'high fsync durations'},
                                                                       'expr'       : 'histogram_quantile(0.99, rate(etcd_disk_wal_fsync_duration_seconds_bucket[5m])) > 0.5',
                                                                       'for'        : '10m',
                                                                       'labels'     : {'severity': 'warning'}},
                                                                      {'alert'      : 'HighCommitDurations',
                                                                       'annotations': {'description': 'etcd instance {{ $labels.instance }} commit durations are high',
                                                                                       'summary': 'high commit durations'},
                                                                       'expr': 'histogram_quantile(0.99, rate(etcd_disk_backend_commit_duration_seconds_bucket[5m])) > 0.25',
                                                                       'for': '10m',
                                                                       'labels': {'severity': 'warning'}}]}]}
        # note skipping the other prometheus rules files: 'general.rules.yaml',  'jws-kubeconfig-abcdef', 'kube-state-metrics.rules.yaml' , 'kubelet.rules.yaml'. 'kubernetes.rules.yaml',  'node.rules.yaml', 'prometheus.rules.yaml'

        assert list_set(yaml_parse(data.get('kubeconfig'))) == ['apiVersion', 'clusters', 'contexts', 'current-context', 'kind', 'preferences', 'users']
        assert yaml_parse(data.get('kubeconfig.conf'))      == { 'apiVersion'       : 'v1',
                                                                 'clusters'         : [ { 'cluster': { 'certificate-authority': '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt',
                                                                                                        'server': 'https://vm.docker.internal:6443'},
                                                                                           'name'  : 'default'}],
                                                                 'contexts'         : [ { 'context': { 'cluster': 'default',
                                                                                                       'namespace': 'default',
                                                                                                       'user': 'default'},
                                                                                          'name': 'default'}],
                                                                 'current-context'  : 'default',
                                                                 'kind'             : 'Config',
                                                                 'users'            : [ { 'name': 'default',
                                                                                          'user': { 'tokenFile': '/var/run/secrets/kubernetes.io/serviceaccount/token'}}]}
        assert yaml_parse(data.get('kubelet')) == {  'apiVersion'                       : 'kubelet.config.k8s.io/v1beta1',
                                                     'authentication'                   : { 'anonymous' : {'enabled': False},
                                                                                            'webhook'   : {'cacheTTL': '0s', 'enabled': True},
                                                                                            'x509'      : {'clientCAFile': '/run/config/pki/ca.crt'}},
                                                     'authorization'                    : { 'mode': 'Webhook',
                                                                                            'webhook'   : { 'cacheAuthorizedTTL': '0s',
                                                                                                            'cacheUnauthorizedTTL': '0s'}},
                                                     'cgroupDriver'                     : 'cgroupfs',
                                                     'clusterDNS'                       : ['10.96.0.10'],
                                                     'clusterDomain'                    : 'cluster.local',
                                                     'cpuManagerReconcilePeriod'        : '0s',
                                                     'evictionPressureTransitionPeriod' : '0s',
                                                     'fileCheckFrequency'               : '0s',
                                                     'healthzBindAddress'               : '127.0.0.1',
                                                     'healthzPort'                      : 10248,
                                                     'httpCheckFrequency'               : '0s',
                                                     'imageMinimumGCAge'                : '0s',
                                                     'kind'                             : 'KubeletConfiguration',
                                                     'logging'                          : {},
                                                     'nodeStatusReportFrequency'        : '0s',
                                                     'nodeStatusUpdateFrequency'        : '0s',
                                                     'rotateCertificates'               : True,
                                                     'runtimeRequestTimeout'            : '0s',
                                                     'shutdownGracePeriod'              : '0s',
                                                     'shutdownGracePeriodCriticalPods'  : '0s',
                                                     'staticPodPath'                    : '/etc/kubernetes/manifests',
                                                     'streamingConnectionIdleTimeout'   : '0s',
                                                     'syncFrequency'                    : '0s',
                                                     'volumeStatsAggPeriod'             : '0s'}
        # note skipping 'prometheus.yaml'
        assert yaml_parse(data.get('requestheader-allowed-names')) == ['front-proxy-client']
        assert data.get('requestheader-client-ca-file').startswith('-----BEGIN CERTIFICATE-----\n')
        assert yaml_parse(data.get('requestheader-extra-headers-prefix')) == ['X-Remote-Extra-']
        assert yaml_parse(data.get('requestheader-group-headers'       )) == ['X-Remote-Group']
        assert yaml_parse(data.get('requestheader-username-headers'    )) == ['X-Remote-User']

    def test_config_maps_metadata(self):
        for config_map_metadata in self.cluster_info.config_maps_metadata():
            assert list_set(config_map_metadata) == [ 'annotations', 'cluster_name', 'creation_timestamp', 'deletion_grace_period_seconds', 'deletion_timestamp', 'finalizers', 'generate_name', 'generation', 'labels', 'managed_fields', 'name', 'namespace', 'owner_references', 'resource_version', 'self_link', 'uid']

        config_maps_metadata = self.cluster_info.config_maps_metadata(index_by='name')
        assert list_set(config_maps_metadata) == [ 'cluster-info', 'coredns', 'extension-apiserver-authentication',
                                                   'kube-proxy', 'kube-root-ca.crt', 'kubeadm-config',
                                                   'kubelet-config-1.21', 'prometheus-config', 'prometheus-rules']

    def test_core_v1_resources(self):
        resources = self.cluster_info.core_v1_resources()
        for resource in resources:
            assert list_set(resource) == ['categories','group','kind','name','namespaced','short_names',
                                          'singular_name','storage_version_hash','verbs','version']

        assert list_set(list_index_by(resources, 'name')) == ['bindings', 'componentstatuses', 'configmaps', 'endpoints',
                                                              'events', 'limitranges', 'namespaces', 'namespaces/finalize',
                                                              'namespaces/status', 'nodes', 'nodes/proxy', 'nodes/status',
                                                              'persistentvolumeclaims', 'persistentvolumeclaims/status',
                                                              'persistentvolumes', 'persistentvolumes/status', 'pods',
                                                              'pods/attach', 'pods/binding', 'pods/eviction', 'pods/exec',
                                                              'pods/log', 'pods/portforward', 'pods/proxy', 'pods/status',
                                                              'podtemplates', 'replicationcontrollers', 'replicationcontrollers/scale',
                                                              'replicationcontrollers/status', 'resourcequotas', 'resourcequotas/status',
                                                              'secrets', 'serviceaccounts', 'serviceaccounts/token',
                                                              'services', 'services/proxy', 'services/status']

    def test_daemon_sets(self):
        daemon_sets = self.cluster_info.daemon_sets()
        for daemon_set_name, daemon_set in daemon_sets.items():
            metadata = daemon_set.get('metadata')
            spec     = daemon_set.get('spec')
            assert daemon_set_name      == metadata.get('name')
            assert list_set(daemon_set) == ['api_version', 'kind', 'metadata', 'spec', 'status']
            assert list_set(metadata  ) == ['annotations', 'cluster_name', 'creation_timestamp', 'deletion_grace_period_seconds', 'deletion_timestamp', 'finalizers', 'generate_name', 'generation', 'labels', 'managed_fields', 'name', 'namespace', 'owner_references', 'resource_version', 'self_link', 'uid']
            assert list_set(spec      ) == ['min_ready_seconds', 'revision_history_limit', 'selector', 'template', 'update_strategy']

        kube_proxy     = daemon_sets.get('kube-proxy'    )

        # metadata
        metadata       = kube_proxy .get('metadata'      )
        labels         = metadata   .get('labels'        )
        managed_fields = metadata   .get('managed_fields')

        assert labels == {'k8s-app': 'kube-proxy'}

        managed_fields__by_manager = list_index_by(managed_fields, "manager")
        kubeadm__managed_fields    = managed_fields__by_manager.get('kubeadm')
        kubeadm__template_spec     = kubeadm__managed_fields.get('fields_v1').get('f:spec').get('f:template').get('f:spec')
        kubeadm__containers        = kubeadm__template_spec.get('f:containers')
        kubeadm__volumes           = kubeadm__template_spec.get('f:volumes'   )
        kubeadm__volume_mounts     = kubeadm__containers.get('k:{"name":"kube-proxy"}').get('f:volumeMounts')

        assert kubeadm__volume_mounts == { '.'                                   : {                                                            },
                                          'k:{"mountPath":"/lib/modules"}'       : { '.': {}, 'f:mountPath': {}, 'f:name': {}, 'f:readOnly': {} },
                                          'k:{"mountPath":"/run/xtables.lock"}'  : { '.': {}, 'f:mountPath': {}, 'f:name': {}                   },
                                          'k:{"mountPath":"/var/lib/kube-proxy"}': { '.': {}, 'f:mountPath': {}, 'f:name': {}                   }}

        assert kubeadm__volumes       == { '.'                          : {},
                                           'k:{"name":"kube-proxy"}'    : { '.'          : {},
                                                                            'f:configMap': { '.': {}, 'f:defaultMode': {}, 'f:name': {}},
                                                                            'f:name'     : {}},
                                           'k:{"name":"lib-modules"}'   : { '.'          : {},
                                                                            'f:hostPath' : { '.': {}, 'f:path': {}, 'f:type': {}},
                                                                            'f:name'     : {}},
                                           'k:{"name":"xtables-lock"}'  : { '.'          : {},
                                                                            'f:hostPath' : { '.': {}, 'f:path': {}, 'f:type': {}},
                                                                            'f:name'     : {}}}

        spec                     = kube_proxy.get('spec')
        spec_containers          = spec.get('template').get('spec').get('containers')
        spec_containers__by_name = list_index_by(spec_containers, 'name')
        spec_kube_proxy          = spec_containers__by_name.get('kube-proxy')
        assert spec_kube_proxy == { 'args'              : None,
                                    'command'           : [ '/usr/local/bin/kube-proxy',
                                                            '--config=/var/lib/kube-proxy/config.conf',
                                                            '--hostname-override=$(NODE_NAME)'],
                                    'env'               : [ { 'name': 'NODE_NAME',
                                                              'value': None,
                                                              'value_from': { 'config_map_key_ref': None,
                                                                              'field_ref': { 'api_version': 'v1',
                                                                                             'field_path': 'spec.nodeName'},
                                                                              'resource_field_ref': None,
                                                                              'secret_key_ref': None}}],
                                    'env_from'          : None,
                                    'image'             : 'k8s.gcr.io/kube-proxy:v1.21.2',
                                    'image_pull_policy' : 'IfNotPresent',
                                    'lifecycle'         : None,
                                    'liveness_probe'    : None,
                                    'name'              : 'kube-proxy',
                                    'ports'             : None,
                                    'readiness_probe'   : None,
                                    'resources'         : { 'limits': None, 'requests': None},
                                    'security_context'  : { 'allow_privilege_escalation'  : None,
                                                            'capabilities'                : None,
                                                            'privileged'                  : True,
                                                            'proc_mount'                  : None,
                                                            'read_only_root_filesystem'   : None,
                                                            'run_as_group'                : None,
                                                            'run_as_non_root'             : None,
                                                            'run_as_user'                 : None,
                                                            'se_linux_options'            : None,
                                                            'windows_options'             : None},
                                    'startup_probe'     : None,
                                    'stdin'             : None,
                                    'stdin_once'        : None,
                                    'termination_message_path'  : '/dev/termination-log',
                                    'termination_message_policy': 'File',
                                    'tty'               : None,
                                    'volume_devices'    : None,
                                    'volume_mounts'     : [ { 'mount_path'          : '/var/lib/kube-proxy',
                                                              'mount_propagation'   : None,
                                                              'name'                : 'kube-proxy',
                                                              'read_only'           : None,
                                                              'sub_path'            : None,
                                                              'sub_path_expr'       : None},
                                                            { 'mount_path'          : '/run/xtables.lock',
                                                              'mount_propagation'   : None,
                                                              'name'                : 'xtables-lock',
                                                              'read_only'           : None,
                                                              'sub_path'            : None,
                                                              'sub_path_expr'       : None},
                                                            { 'mount_path'          : '/lib/modules',
                                                              'mount_propagation'   : None,
                                                              'name'                : 'lib-modules',
                                                              'read_only'           : True,
                                                              'sub_path'            : None,
                                                              'sub_path_expr'       : None}],
                                    'working_dir': None}

    def test_deployments(self):
        deployments                 = self.cluster_info.deployments()
        coredns_deployment          = deployments.get('coredns')
        coredns_spec                = coredns_deployment.get('spec').get('template').get('spec')
        coredns_containers          = coredns_spec.get('containers')
        coredns_containers_by_name  = list_index_by(coredns_containers, 'name')
        coredns_container           = coredns_containers_by_name.get('coredns')
        coredns_tolerations         = coredns_spec.get('tolerations')

        assert list_set(coredns_containers_by_name) == ['coredns']
        assert list_set(coredns_container         ) == [ 'args', 'command', 'env', 'env_from', 'image', 'image_pull_policy',
                                                         'lifecycle', 'liveness_probe', 'name', 'ports', 'readiness_probe',
                                                         'resources', 'security_context', 'startup_probe', 'stdin', 'stdin_once',
                                                         'termination_message_path', 'termination_message_policy', 'tty',
                                                         'volume_devices', 'volume_mounts', 'working_dir']

        assert coredns_container == { 'args'                : ['-conf', '/etc/coredns/Corefile'],
                                      'command'             : None,
                                      'env'                 : None,
                                      'env_from'            : None,
                                      'image'               : 'k8s.gcr.io/coredns/coredns:v1.8.0',
                                      'image_pull_policy'   : 'IfNotPresent',
                                      'lifecycle'           : None,
                                      'liveness_probe'      : { '_exec'                 : None  ,
                                                                'failure_threshold'     : 5     ,
                                                                'http_get'              : { 'host'          : None,
                                                                                            'http_headers'  : None,
                                                                                            'path'          : '/health',
                                                                                            'port'          : 8080,
                                                                                            'scheme'        : 'HTTP'},
                                                                'initial_delay_seconds' : 60    ,
                                                                'period_seconds'        : 10    ,
                                                                'success_threshold'     : 1     ,
                                                                'tcp_socket'            : None  ,
                                                                'timeout_seconds'       : 5     },
                                      'name'                : 'coredns',
                                      'ports'               : [ { 'container_port' : 53        ,
                                                                  'host_ip'        : None      ,
                                                                  'host_port'      : None      ,
                                                                  'name'           : 'dns'     ,
                                                                  'protocol'       : 'UDP'     },
                                                                { 'container_port' : 53        ,
                                                                  'host_ip'        : None      ,
                                                                  'host_port'      : None      ,
                                                                  'name'           : 'dns-tcp' ,
                                                                  'protocol'       : 'TCP'     },
                                                                { 'container_port' : 9153      ,
                                                                  'host_ip'        : None      ,
                                                                  'host_port'      : None      ,
                                                                  'name'           : 'metrics' ,
                                                                  'protocol'       : 'TCP'     }],
                                      'readiness_probe'     : { '_exec'                 : None  ,
                                                                'failure_threshold'     : 3     ,
                                                                'http_get'              : { 'host'          : None      ,
                                                                                        'http_headers'  : None      ,
                                                                                        'path'          : '/ready'  ,
                                                                                        'port'          : 8181      ,
                                                                                        'scheme'        : 'HTTP'    },
                                                                'initial_delay_seconds' : None  ,
                                                                'period_seconds'        : 10    ,
                                                                'success_threshold'     : 1     ,
                                                                'tcp_socket'            : None  ,
                                                                'timeout_seconds'       : 1     },
                                      'resources'           : { 'limits'   : {'memory': '170Mi'},
                                                                'requests' : {'cpu': '100m', 'memory': '70Mi'}},
                                      'security_context'    : { 'allow_privilege_escalation': False,
                                                                'capabilities': { 'add': ['NET_BIND_SERVICE'], 'drop': ['all']},
                                                                'privileged'                : None,
                                                                'proc_mount'                : None,
                                                                'read_only_root_filesystem' : True,
                                                                'run_as_group'              : None,
                                                                'run_as_non_root'           : None,
                                                                'run_as_user'               : None,
                                                                'se_linux_options'          : None,
                                                                'windows_options'           : None},
                                      'startup_probe'       : None,
                                      'stdin'               : None,
                                      'stdin_once'          : None,
                                      'termination_message_path': '/dev/termination-log',
                                      'termination_message_policy': 'File',
                                      'tty'                 : None,
                                      'volume_devices'      : None,
                                      'volume_mounts'       : [ { 'mount_path'       : '/etc/coredns',
                                                                  'mount_propagation': None,
                                                                  'name'             : 'config-volume',
                                                                  'read_only'        : True,
                                                                  'sub_path'         : None,
                                                                  'sub_path_expr'   : None}],
                                      'working_dir'         : None}
        assert coredns_tolerations == [  { 'effect'             : None,
                                           'key'                : 'CriticalAddonsOnly',
                                           'operator'           : 'Exists',
                                           'toleration_seconds' : None,
                                           'value'              : None},
                                         { 'effect'             : 'NoSchedule',
                                           'key'                : 'node-role.kubernetes.io/master',
                                           'operator'           : None,
                                           'toleration_seconds' : None,
                                           'value'              : None},
                                         { 'effect'             : 'NoSchedule',
                                           'key'                : 'node-role.kubernetes.io/control-plane',
                                           'operator'           : None,
                                           'toleration_seconds' : None,
                                           'value'              : None}]

    def test_endpoints(self):
        endpoints = self.cluster_info.endpoints()
        for endpoint in endpoints.values():
             assert list_set(endpoint) == ['api_version', 'kind', 'metadata', 'subsets']
        assert 'docker.io-hostpath' in list_set(endpoints)
        #assert list_set(endpoints)     == ['docker.io-hostpath', 'kube-dns', 'kube-state-metrics', 'kubernetes', 'node-exporter', 'prometheus']

        kube_dns            = endpoints.get('kube-dns')
        kube_dns_metadata   = kube_dns.get('metadata')
        kube_dns_subsets    = kube_dns.get('subsets')
        kube_dns_subset     = kube_dns.get('subsets')[0]
        kube_addresses      = kube_dns_subset.get('addresses')
        kube_ports          = kube_dns_subset.get('ports')

        for kube_address in kube_addresses:
            assert list_set(kube_address) == ['hostname', 'ip', 'node_name', 'target_ref']

        assert len(kube_dns_subsets) == 1
        assert kube_dns_metadata.get('labels') == { 'k8s-app'                      : 'kube-dns' ,
                                                    'kubernetes.io/cluster-service': 'true'     ,
                                                    'kubernetes.io/name'           : 'CoreDNS'  }

        assert kube_ports == [ { 'app_protocol' : None,
                                 'name'         : 'dns-tcp',
                                 'port'         : 53,
                                 'protocol'     : 'TCP'},
                               { 'app_protocol' : None,
                                 'name'         : 'dns',
                                 'port'         : 53,
                                 'protocol'     : 'UDP'},
                               { 'app_protocol': None,
                                 'name'         : 'metrics',
                                 'port'         : 9153,
                                 'protocol'     : 'TCP'}]
    
    def test_events(self):
        events   = self.cluster_info.events()
        messages = list_get_field(events, "message")
        for event in events:
            assert list_set(event) == ['action', 'api_version', 'count', 'event_time', 'first_timestamp', 'involved_object', 'kind', 'last_timestamp', 'message', 'metadata', 'reason', 'related', 'reporting_component', 'reporting_instance', 'series', 'source', 'type']
        assert 'Created container vpnkit-controller' in messages


        event = events.pop()                                # get one pod to test the field selector
        event_pod_name = event.get('metadata').get('name')
        #event_pod_name = 'hello-world-dpbcjgnl'
        events_for_pod = self.cluster_info.events(field_selector=f'involvedObject.name={event_pod_name}')

        for event in events_for_pod:
            involved_object = event.get('involved_object').get('name')
            assert involved_object == event_pod_name

            #code below was testing the sort and sequence of events. todo: figure out the best way to get the correct order events
            #when     = event.get('event_time') or event.get('last_timestamp')
            #when     = event.get('metadata').get('creation_timestamp')
            #event_id = event.get('metadata').get('name')
            #message  = event.get('message')
            #print(when, '  ', message )
        #    pprint(event)

        # events_for_pod.sort(key = lambda x:x['metadata']['creation_timestamp'])
        # print('-------')
        # for event in events_for_pod:
        #     #when     = event.get('event_time') or event.get('last_timestamp')
        #     when     = event.get('metadata').get('creation_timestamp')
        #     event_id = event.get('metadata').get('name')
        #     message  = event.get('message')
        #     print(when, '  ', message )


        #pprint(events_for_pod)

    def test_limit_range(self):
        limit_range =  self.cluster_info.limit_range()
        assert limit_range == {'api_version' : 'v1',
                               'items'       : []  ,
                               'kind'        : 'LimitRangeList',
                               'metadata'    : { '_continue'           : None                                               ,
                                                 'remaining_item_count': None                                               ,
                                                 'resource_version'    : limit_range.get('metadata').get('resource_version'),
                                                 'self_link'           : None                                              }}

    def test_namespaces(self):
        namespaces = self.cluster_info.namespaces()
        pprint(namespaces)

    def test_pod_events(self):
        events     = self.cluster_info.events()
        event      = events.pop()
        pod_name   = event.get('involved_object').get('name')
        pod_events = self.cluster_info.pod_events(pod_name=pod_name)
        for pod_event in pod_events:
            assert pod_event.get('involved_object').get('name') == pod_name
            assert pod_event.get('metadata').get('name').startswith(pod_name)

    def test_pod_logs(self):
        pods      = list(self.cluster_info.pods().values())
        pod       = pods.pop(0)
        pod_name  = pod.get('metadata').get('name'     )
        namespace = pod.get('metadata').get('namespace')
        logs      = self.cluster_info.pod_logs(pod_name=pod_name, namespace=namespace)
        assert type(logs) is str
        assert len(logs) > 0                # todo add a better test with a pod that we know what it is

    def test_pods(self):
        pods = self.cluster_info.pods()
        pprint(pods)
    #@pytest.mark.skip

    # def test__(self):
    #     core_api = self.cluster_info.api_core_v1()
    #     #data = core_api.list_limit_range_for_all_namespaces()
    #     #pprint(data)
    #     #response = json_parse(core_api.api_client.request(url=url, method='GET').data)




    def test_stateful_sets(self):
        stateful_sets = self.cluster_info.stateful_sets()
        for stateful_set_name, stateful_set in stateful_sets.items():
            assert list_set(stateful_set) == ['api_version', 'kind', 'metadata', 'spec', 'status']

        prometheus          = stateful_sets.get('prometheus')
        prometheus_spec     = prometheus.get('spec').get('template').get('spec')
        containers          = prometheus_spec.get('containers')
        containers_by_name  = list_index_by(containers, 'name')
        container           = containers_by_name.get('prometheus')
        init_containers     = prometheus_spec.get('init_containers')
        volumes             = prometheus_spec.get('volumes')
        volumes_by_name     = list_index_by(volumes, 'name')

        assert container == { 'args'                : [ '--web.listen-address=0.0.0.0:9090',
                                                        '--config.file=/etc/prometheus/prometheus.yaml',
                                                        '--storage.tsdb.path=/var/lib/prometheus',
                                                        '--storage.tsdb.retention.time=2d',
                                                        '--storage.tsdb.retention.size=5GB',
                                                        '--storage.tsdb.min-block-duration=2h',
                                                        '--storage.tsdb.max-block-duration=2h'],
                              'command'             : None,
                              'env'                 : None,
                              'env_from'            : None,
                              'image'               : 'quay.io/prometheus/prometheus:v2.27.1',
                              'image_pull_policy'   : 'IfNotPresent',
                              'lifecycle'           : None,
                              'liveness_probe'      : { '_exec'             : None,
                                                        'failure_threshold' : 3,
                                                        'http_get'          : { 'host'          : None,
                                                                                'http_headers'  : None,
                                                                                'path'          : '/-/healthy',
                                                                                'port'          : 9090,
                                                                                'scheme'        : 'HTTP'},
                                                        'initial_delay_seconds': 10,
                                                        'period_seconds'    : 10,
                                                        'success_threshold' : 1,
                                                        'tcp_socket'        : None,
                                                        'timeout_seconds'   : 10},
                              'name'                : 'prometheus',
                              'ports'               : [ { 'container_port'  : 9090,
                                                          'host_ip'         : None,
                                                          'host_port'       : None,
                                                          'name'            : 'web',
                                                          'protocol'        : 'TCP'}],
                              'readiness_probe'     : { '_exec'             : None,
                                                        'failure_threshold': 3,
                                                        'http_get'          : { 'host'          : None,
                                                                                'http_headers'  : None,
                                                                                'path'          : '/-/ready',
                                                                                'port'          : 9090,
                                                                                'scheme'        : 'HTTP'},
                                                        'initial_delay_seconds' : 10,
                                                        'period_seconds'    : 10,
                                                        'success_threshold' : 1,
                                                        'tcp_socket'        : None,
                                                        'timeout_seconds'   : 10},
                              'resources'           : {'limits': None, 'requests': {'cpu': '100m', 'memory': '512Mi'}},
                              'security_context'    : None,
                              'startup_probe'       : None,
                              'stdin'               : None,
                              'stdin_once'          : None,
                              'termination_message_path'    : '/dev/termination-log',
                              'termination_message_policy'  : 'File',
                              'tty'                 : None,
                              'volume_devices'      : None,
                              'volume_mounts'       : [ { 'mount_path'          : '/etc/prometheus',
                                                          'mount_propagation'   : None,
                                                          'name'                : 'config',
                                                          'read_only'           : None,
                                                          'sub_path'            : None,
                                                          'sub_path_expr'       : None},
                                                        { 'mount_path'          : '/etc/prometheus/rules',
                                                          'mount_propagation'   : None,
                                                          'name'                : 'rules',
                                                          'read_only'           : None,
                                                          'sub_path'            : None,
                                                          'sub_path_expr'       : None},
                                                        { 'mount_path'          : '/var/lib/prometheus',
                                                          'mount_propagation'   : None,
                                                          'name'                : 'data',
                                                          'read_only'           : None,
                                                          'sub_path'            : None,
                                                          'sub_path_expr'       : None}],
                              'working_dir'          : None}

        assert volumes_by_name.get('config').get('config_map') ==  { 'default_mode' : 420                ,
                                                                     'items'        : None               ,
                                                                     'name'         : 'prometheus-config',
                                                                     'optional'     : None               }
        assert volumes_by_name.get('rules').get('config_map') ==  { 'default_mode'  : 420                ,
                                                                     'items'        : None               ,
                                                                     'name'         : 'prometheus-rules' ,
                                                                     'optional'     : None               }

        assert init_containers == [ { 'args'             : None,
                                      'command'          : ['chown', '-R', '65534:65534', '/var/lib/prometheus'],
                                      'env'              : None,
                                      'env_from'         : None,
                                      'image'            : 'docker.io/alpine:3.12',
                                      'image_pull_policy': 'IfNotPresent',
                                      'lifecycle'        : None,
                                      'liveness_probe'   : None,
                                      'name'             : 'chown',
                                      'ports'            : None,
                                      'readiness_probe'  : None,
                                      'resources'        : {'limits': None, 'requests': None},
                                      'security_context' : None,
                                      'startup_probe'    : None,
                                      'stdin'            : None,
                                      'stdin_once'       : None,
                                      'termination_message_path': '/dev/termination-log',
                                      'termination_message_policy': 'File',
                                      'tty'              : None,
                                      'volume_devices'   : None,
                                      'volume_mounts'    : [ { 'mount_path'       : '/var/lib/prometheus',
                                                               'mount_propagation': None    ,
                                                               'name'             : 'data'  ,
                                                               'read_only'        : None    ,
                                                               'sub_path'         : None    ,
                                                               'sub_path_expr'    : None    }],
                                      'working_dir'      : None }]

    def test_replica_sets(self):
        replica_sets = self.cluster_info.replica_sets()
        for replica_set_name, replica_set in replica_sets.items():
            assert list_set(replica_set) == ['api_version', 'kind', 'metadata', 'spec', 'status']
