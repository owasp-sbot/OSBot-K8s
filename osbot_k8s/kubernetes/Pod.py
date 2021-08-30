from kubernetes.client                              import ApiException
from kubernetes.watch                               import Watch

from osbot_k8s.kubernetes.Namespace import Namespace
from osbot_utils.utils.Dev import pprint

from osbot_utils.utils.Json                         import json_loads

from osbot_utils.decorators.methods.cache_on_self import cache_on_self
from osbot_utils.utils.Status                     import status_ok, status_error

class Pod:

    def __init__(self, name=None, cluster=None):
        self.name      = name
        self.cluster   = cluster


    @cache_on_self
    def api_core(self):
        return self.cluster.api_core_v1()

    def create(self, manifest):
        try:
            pod_info = self.api_core().create_namespaced_pod(body=manifest, namespace=self.namespace_name())
            return status_ok(message="pod created", data=pod_info)
        except ApiException as exception:
            exception_body = json_loads(exception.body)
            return status_error(message=exception_body.get('message'), error=exception)
        except Exception as exception:
            return status_error(error=exception)

    def delete(self):
        if self.exists():       # todo: check for other states of pod that could affect this deletion action
            data = self.api_core().delete_namespaced_pod(name=self.name, namespace=self.namespace_name())
            return status_ok(message="pod deleted", data=data)

        return status_ok(message="pod not deleted (since it didn't exist)")

    def exists(self):
        return self.info() != {}

    def format_pod(self, item):
        data = {}
        if item:
            data = { "id"        : item.metadata.uid             ,
                     "ip"        : item.status.pod_ip            ,
                     "image"     : item.spec.containers[0].image ,
                     "phase"     : item.status.phase             ,
                     "name"      : item.metadata.name            ,
                     "namespace" : item.metadata.namespace       ,
                     "start_time": item.status.start_time        }
        return data


    def event_wait_for(self,  wait_for_name=None, wait_for_type=None, wait_for_phase=None, **kwargs): # todo improve logic to take into account the use of labels to select the target
        for event in Watch().stream(**kwargs):
            event_type  = event.get('type')
            event_phase = event.get('object').status.phase
            name        = event.get('object').metadata.name
            #print(event_type, event_phase)             # todo: capture in log
            if name == wait_for_name:
                if wait_for_type is None:               # if we have a name but not wait_for_type return event
                    return event
                if event_type == wait_for_type:
                    if wait_for_phase is None:          # if we have a name, event_type but no wait_for_phase return event
                        return event
                    if event_phase == wait_for_phase:   # if we have a name, event_type and wait_for_phase return event
                        return event
        return None                                     # None value represents no match or timeout

    def event_wait_for__pod_in_namespace(self, pod_name, namespace, wait_for_type=None, wait_for_phase=None, label='', timeout=10):
        kwargs = {'func'           : self.api_core().list_namespaced_pod ,
                  'namespace'      : namespace                           ,
                  'label_selector' : label                               ,
                  'timeout_seconds': timeout                             }
        return self.event_wait_for(wait_for_name=pod_name, wait_for_type=wait_for_type, wait_for_phase=wait_for_phase, **kwargs)

    def event_wait_for_pod_deleted(self, timeout=40):
        return self.event_wait_for__pod_in_namespace(pod_name=self.name, namespace=self.namespace_name(), wait_for_type='DELETED', timeout=timeout)

    def event_wait_for_pod_running(self, timeout=10):
        return self.event_wait_for__pod_in_namespace(pod_name=self.name, namespace=self.namespace_name(), wait_for_type='MODIFIED', wait_for_phase='Running', timeout=timeout)

    def info(self):
        return self.format_pod(self.info_raw().get('data'))

    def info_raw(self):
        try:
            data = self.api_core().read_namespaced_pod(name=self.name, namespace=self.namespace_name())
            return status_ok(data=data)
        except Exception as exception:
            return status_error(error=exception)

    def namespace_name(self):
        return self.cluster.namespace().name

    def __repr__(self):
        return f'Pod: {self.name}'