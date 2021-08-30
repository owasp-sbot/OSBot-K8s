from unittest import TestCase

from osbot_utils.utils.Dev import pprint

from tests.integration.Create_Multiple_Pods import Create_Multiple_Pods


class test_Create_Multiple_Pods(TestCase):

    def setUp(self):
        self.create_pods = Create_Multiple_Pods()
        self.cluster = self.create_pods.cluster

    def test_create_pod(self):
        #pprint(self.pod_manifest)
        result = self.create_pods.create_pod()
        pprint(result)

    def test_create_pod__hello_world(self):
        #pprint(self.pod_manifest)
        pod_image = "hello-world"
        result = self.create_pods.create_pod(pod_image=pod_image)
        pprint(result)

    def test_create_pods(self):
        self.create_pods.create_pods(count=10)

    def test_delete_pods(self):
        self.create_pods.delete_pods()


    def test_create_pod_grafana(self):
        result = self.create_pods.create_pod_grafana()
        pprint(result)
