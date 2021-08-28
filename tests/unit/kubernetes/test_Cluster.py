import inspect
import os
from unittest import TestCase
import pytest
from osbot_utils.utils.Misc import obj_dict, list_set, obj_list_set, class_functions, class_functions_names, \
    list_index_by, list_group_by

from osbot_utils.utils.Dev import pprint
from pytest import skip

from osbot_k8s.kubernetes.Cluster import Cluster
from osbot_utils.utils.Files import path_combine, file_exists
from osbot_utils.utils.Yaml import yaml_load

DEFAULT_DOCKER_DESKTOP_NAME = 'docker-desktop'
DEFAULT_DOCKER_DESKTOP_HOST = 'https://kubernetes.docker.internal:6443'

class test_Cluster(TestCase):

    def setUp(self):
        self.cluster = Cluster(config_context=DEFAULT_DOCKER_DESKTOP_NAME)
        if self.cluster.load_config() is False:
            skip('no K8 clusters available in current environment')
        print()

    def test_api_apps_v1(self):
        apps_api      = self.cluster.api_apps_v1()
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


    def test_api_resources(self):
        resources = self.cluster.api_resources()
        for resource in resources:
            assert list_set(resource) == ['categories','group','kind','name','namespaced','short_names',
                                          'singular_name','storage_version_hash','verbs','version']

        assert list_set(list_index_by(resources, 'name')) == ['controllerrevisions', 'daemonsets', 'daemonsets/status',
                                                              'deployments', 'deployments/scale', 'deployments/status',
                                                              'replicasets', 'replicasets/scale', 'replicasets/status',
                                                              'statefulsets', 'statefulsets/scale', 'statefulsets/status']

    @pytest.mark.skip('refactor into a new Deployment class')
    def test_deployment(self):
        deployment_file = path_combine('../../test_files/deployment','nginx-deployment.yaml')
        assert file_exists(deployment_file)
        deployment = yaml_load(deployment_file)
        resp = self.cluster.api_apps_v1().create_namespaced_deployment(body=deployment, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)

    def test_info(self):
        info = self.cluster.info()
        for item in info:
            assert list_set(item) == ['api_version', 'binary_data', 'data', 'immutable', 'kind', 'metadata']

    def test_namespaces(self):
        assert len(self.cluster.namespaces()) > 0

    def test_namespaces_infos(self):
        namespaces = self.cluster.namespaces_infos(index_by='name')
        assert 'default' in namespaces
        assert namespaces.get('default').get('name'  )       == 'default'
        assert namespaces.get('default').get('status').phase == 'Active'

    def test_pods(self):
        assert type(self.cluster.pods()) is list

    def test_pods_all(self):
        assert len(self.cluster.pods_all()) > 0
