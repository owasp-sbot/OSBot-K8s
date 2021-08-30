import inspect
import os
from unittest import TestCase
import pytest

from osbot_k8s.utils.Docker_Desktop_Cluster import DEFAULT_DOCKER_DESKTOP_NAME
from osbot_utils.utils.Misc import obj_dict, list_set, obj_list_set, class_functions, class_functions_names, \
    list_index_by, list_group_by, obj_data, list_get_field

from osbot_utils.utils.Dev import pprint
from pytest import skip

from osbot_k8s.kubernetes.Cluster import Cluster
from osbot_utils.utils.Files import path_combine, file_exists
from osbot_utils.utils.Yaml import yaml_load, yaml_parse


class test_Cluster(TestCase):

    def setUp(self):
        self.cluster = Cluster(config_context=DEFAULT_DOCKER_DESKTOP_NAME)
        if self.cluster.load_config() is False:
            skip('no K8 clusters available in current environment')
        print()


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


    @pytest.mark.skip('refactor into a new Deployment class')
    def test_deployment(self):
        deployment_file = path_combine('../../test_files/deployment','nginx-deployment.yaml')
        assert file_exists(deployment_file)
        deployment = yaml_load(deployment_file)
        resp = self.cluster.api_apps_v1().create_namespaced_deployment(body=deployment, namespace="default")
        print("Deployment created. status='%s'" % resp.metadata.name)