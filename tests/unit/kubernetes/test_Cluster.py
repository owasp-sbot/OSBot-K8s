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
from osbot_utils.utils.Yaml import yaml_load, yaml_parse

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

    def test_config_maps(self):
        for item in self.cluster.config_maps():
            assert list_set(item) == ['api_version', 'binary_data', 'data', 'immutable', 'kind', 'metadata']
            assert item.get('api_version') == None
            assert item.get('binary_data') == None
            assert item.get('immutable'  ) == None
            assert item.get('kind'       ) == None
            #assert item.get('metadata'   ) == None

            assert list_set(item.get('data')) in [['ca.crt'                                                                         ],
                                                  ['jws-kubeconfig-abcdef', 'kubeconfig'                                            ],
                                                  ['Corefile'                                                                       ],
                                                  ['client-ca-file', 'requestheader-allowed-names', 'requestheader-client-ca-file',
                                                   'requestheader-extra-headers-prefix', 'requestheader-group-headers',
                                                   'requestheader-username-headers'                                                 ],
                                                  ['config.conf', 'kubeconfig.conf'                                                 ],
                                                  ['ClusterConfiguration', 'ClusterStatus'                                          ],
                                                  ['kubelet'                                                                        ],
                                                  ['prometheus.yaml'                                                                ],
                                                  ['alertmanager.rules.yaml', 'etcd3.rules.yaml', 'general.rules.yaml',
                                                   'kube-state-metrics.rules.yaml', 'kubelet.rules.yaml',
                                                   'kubernetes.rules.yaml', 'node.rules.yaml', 'prometheus.rules.yaml'              ]]

        # confirm that every entry in config_map.ata is the same
        config_maps_data = {}
        for config_map in self.cluster.config_maps():
            for data_name, data_value in config_map.get('data').items():
                if config_maps_data.get(data_name) is None:                    # only add if it doesn't exist
                    config_maps_data[data_name] = data_value
                else:
                    assert config_maps_data[data_name] == data_value           # if it exists, it should be the same

    def test_config_maps_data(self):
        data = self.cluster.config_maps_data()
        assert list_set(data) == [ 'ClusterConfiguration',  'ClusterStatus',  'Corefile',
                                   'alertmanager.rules.yaml',  'ca.crt',  'client-ca-file',  'config.conf',
                                   'etcd3.rules.yaml',  'general.rules.yaml',  'jws-kubeconfig-abcdef',
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
                                                                       'labels': {'severity': 'warning'}},
                                                                      {'alert': 'HighCommitDurations',
                                                                       'annotations': {'description': 'etcd instance {{ $labels.instance }} commit durations are high',
                                                                                       'summary': 'high commit '
                                                                                                  'durations'},
                                                                       'expr': 'histogram_quantile(0.99, rate(etcd_disk_backend_commit_duration_seconds_bucket[5m])) > 0.25',
                                                                       'for': '10m',
                                                                       'labels': {'severity': 'warning'}}]}]}
        pprint(yaml_parse(data.get('etcd3.rules.yaml')))
        #pprint(yaml_parse(data.get('alertmanager.rules.yaml')))
        #pprint(yaml_parse(data.get('Corefile')))

    @pytest.mark.skip('refactor into a new Deployment class')
    def test_deployment(self):
        deployment_file = path_combine('../../test_files/deployment','nginx-deployment.yaml')
        assert file_exists(deployment_file)
        deployment = yaml_load(deployment_file)
        resp = self.cluster.api_apps_v1().create_namespaced_deployment(body=deployment, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)

    def test_info(self):            #
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
