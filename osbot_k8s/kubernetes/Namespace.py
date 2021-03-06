from kubernetes import client
from osbot_utils.utils.Status import status_ok, status_error, status_warning


class Namespace:
    def __init__(self, name, cluster):
        self.cluster   = cluster
        self.name      = name

    def create(self):
        if self.exists():
            return status_error(message=f"namespace already existed: {self.name}")
        try:
            manifest = client.V1Namespace(metadata=client.V1ObjectMeta(name=self.name))
            result = self.cluster.api_core_v1().create_namespace(manifest)
        except Exception as exception:
            return status_error(data=exception)

        return status_ok(message="namespace created", data=result)

    def delete(self):
        if self.exists():
            result = self.cluster.api_core_v1().delete_namespace(name=self.name)
            return status_ok(message="namespace deleted", data=result)
        return status_warning(message="namespace already existed")

    def exists(self):
        return self.info() != {}

    def format_namespace(self, item):
        data = {}
        if item:
            metadata = item.metadata
            data = {  'annotations': metadata.annotations        ,
                      'label'      : metadata.labels             ,
                      'created_at' : metadata.creation_timestamp ,
                      'name'       : metadata.name               ,
                      'spec'       : item.spec                   ,
                      'status'     : item.status                 }
        return data

    def info(self):
        return self.format_namespace(self.info_raw())

    def info_raw(self):
        try:
            return self.cluster.api_core_v1().read_namespace(name=self.name)
        except:
            return None

    def not_exists(self):
        return self.info() == {}

    def __repr__(self):
        return f"Namespace: {self.name}"
