from unittest import TestCase

from osbot_utils.utils.Misc import wait

from osbot_k8s.kubernetes.Cluster import Cluster
from osbot_k8s.utils.Docker_Desktop_Cluster import Docker_Desktop_Cluster
from osbot_utils.utils.Dev import pprint

from osbot_k8s.manifests.Pod_Manifest import Pod_Manifest


class test_Pod_Manifest(TestCase):

    def setUp(self):
        self.pod_manifest = Pod_Manifest()
        self.manifest     = self.pod_manifest.manifest
        self.metadata     = self.pod_manifest.metadata
        self.spec         = self.pod_manifest.spec

    def test_setup(self):
        assert self.pod_manifest.manifest   == { 'apiVersion' : 'v1'                         ,
                                                 'kind'       : 'Pod'                        ,
                                                 'metadata'   : self.pod_manifest.metadata   ,
                                                 'spec'       : self.pod_manifest.spec       }
        assert self.pod_manifest.metadata   == { 'labels'     : self.pod_manifest.labels     }
        assert self.pod_manifest.labels     == {}
        assert self.pod_manifest.spec       == { 'containers' : self.pod_manifest.containers }
        assert self.pod_manifest.containers == []

    def test_add_container(self):
        image = 'an-image'
        name  = 'an-name'
        assert self.pod_manifest.containers == []
        self.pod_manifest.add_container(image=image, name=name)
        assert self.pod_manifest.containers == [{'image': 'an-image', 'name': 'an-name'}]

    def test_render(self):
        (self.pod_manifest.set_name('pod_name', add_random_id=False)
                          .add_container(image='image_name',name='container_name'))
        manifest = self.pod_manifest.render()
        assert manifest == { 'apiVersion': 'v1',
                              'kind'     : 'Pod',
                              'metadata' : { 'labels':{} , 'name': 'pod_name'},
                              'spec'     : { 'containers': [{'image': 'image_name', 'name': 'container_name'}]}}


    def test_set__metadata_values(self):
        pod_name  = 'pod_name'
        assert self.metadata == { 'labels': {}}
        (self.pod_manifest.set_name(pod_name,add_random_id=False)
                          .add_label('an','label'))
        assert self.metadata == { 'labels'  : {'an':'label' },
                                  'name'    : pod_name      }

class test_Pod_Manifest__Create_in_K8s(TestCase):

    def setUp(self) -> None:
        self.cluster = Docker_Desktop_Cluster()

    def test_create_pod_hello_world(self):
        name = 'hello-world'
        pod_manifest = (Pod_Manifest().set_name(name)
                                      .add_container('hello-world')
                                      .add_label('type', name))

        manifest = pod_manifest.render()
        pprint(manifest)
        data   = self.cluster.pod_create(manifest)
        pod    = data.get('pod')
        result = data.get('result')
        message = result.get('message')
        status = result.get('status')
        assert message == 'pod created'
        assert status  == 'ok'
        wait(5)
        assert pod.delete().get('message') == 'pod deleted'



