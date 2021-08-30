from unittest import TestCase

from osbot_utils.utils.Dev import pprint

from osbot_k8s.kubernetes.Cluster import Cluster
from osbot_k8s.kubernetes.Pod import Pod
from osbot_k8s.manifests.Pod_Manifest import Pod_Manifest
from osbot_utils.utils.Misc import random_string, lower, list_set

class test_Pod(TestCase):

    pod             : Pod
    wait_for_delete : bool

    @classmethod
    def setUpClass(cls) -> None:
        cls.wait_for_delete = False
        cls.pod_name        = random_string(prefix='temp-pod-')
        cls.image_name      = 'nginx'
        cls.pod_manifest    = Pod_Manifest().pod_simple(cls.pod_name, cls.image_name)
        cls.cluster         = Cluster()
        cls.namespace       = cls.cluster.default_namespace
        cls.pod             = Pod(name=cls.pod_name, cluster=cls.cluster)
        cls.pod_info        = cls.pod.create(cls.pod_manifest)

    @classmethod
    def tearDownClass(cls) -> None:
        assert cls.pod.delete().get('message')         == "pod deleted"
        if cls.wait_for_delete:
            assert cls.pod.event_wait_for_pod_deleted() is not None
            assert cls.pod.exists                    () is False

            print()
            events = cls.pod.events()
            for event in events:
                when    = event.get('metadata').get('creation_timestamp')
                message = event.get('message')
                print(f'{when} {message}')

    def setUp(self) -> None:
        pass

    def test_create(self):
        assert self.pod.event_wait_for_pod_running() is not None

    def test_delete(self):
        pass                # todo: add tests for bad deletion params

    def test_exists(self):
        assert self.pod.exists()                          is True
        assert Pod(lower(random_string()), None).exists() is False

    def test_events(self):
        assert self.pod.event_wait_for_pod_running() is not None
        print()
        events = self.pod.events()
        for event in events:
            when    = event.get('metadata').get('creation_timestamp')
            message = event.get('message')
            print(f'{when} {message}')
        #pprint(events)

    def test_info(self):
        pod_info = self.pod.info()
        del pod_info['id']
        del pod_info['start_time']
        assert list_set(pod_info) == ['image', 'ip', 'name', 'namespace', 'phase']
        assert pod_info['name'  ] == self.pod_name

    def test_logs(self):
        #assert self.pod.event_wait_for_pod_running() is not None       # todo , need to find a better way to do this, namely to take into account the current state of the pod
        logs = self.pod.logs()
        assert "nginx/1.21.1\n" in logs