from osbot_utils.utils.Misc import random_string


class Pod_Manifest:

    def __init__(self):
        self.manifest   = self.manifest_base(kind='Pod' )
        self.metadata   = self.manifest.get('metadata'  )
        self.spec       = self.manifest.get('spec'      )
        self.labels     = self.metadata.get('labels'    )
        self.containers = self.spec    .get('containers')

    def manifest_base(self, kind):
        return { 'apiVersion' : 'v1'                  ,      # todo refactor into base class (since this common
                 'kind'      : kind                   ,
                 'metadata'  : { 'labels'     : {}}   ,
                 'spec'      : { 'containers' : []   }}

    def pod_simple(self, pod_name, image_name):
        return  { 'apiVersion': 'v1'                                       ,
                  'kind'      : 'Pod'                                      ,
                  'metadata'  : { 'name'      : pod_name                } ,
                  'spec'      : { 'containers': [{ 'image': image_name ,
                                                   'name' : pod_name   }] } }

    def render(self):
        return self.manifest
        #return self.pod_simple('pod_name', 'image_name')

    def add_container(self, image, name=None):
        container = { 'image': image ,
                      'name' : name or image }
        self.containers.append(container)
        return self

    def add_label(self, key, value):
        self.labels[key] = value
        return self

    def set_name(self, name, add_random_id=True):
        if add_random_id:
            name = random_string(prefix=f'{name}-')
        self.metadata['name'] = name
        return self