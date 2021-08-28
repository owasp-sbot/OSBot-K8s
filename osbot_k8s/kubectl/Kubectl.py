from osbot_utils.utils.Misc import split_lines

from osbot_utils.utils.Json import json_parse

from osbot_utils.utils.Process import start_process


class Kubectl:

    # base functions
    def kubectl_exec_raw(self, params=None):
        return start_process("kubectl", params=params)

    def kubectl_exec(self, params=None):
        result = self.kubectl_exec_raw(params=params)
        if result.get('stderr'):
            return result.get('stderr')
        return result.get('stdout')


    # config methods

    def clusters(self):
        clusters = {}
        for cluster in self.config().get('clusters'):
            clusters[cluster.get('name')] = cluster.get('cluster')
        return clusters

    def config(self):
        return json_parse(self.kubectl_exec(['config', 'view', '-o', 'json']))

    def context_current(self):
        return self.config().get('current-context')

    def context_set_current(self, context):
        return self.kubectl_exec(['config','use-context', context])

    def contexts(self):
        contexts = {}
        for context in self.config().get('contexts'):
            contexts[context.get('name')] = context.get('context')
        return contexts

    def users(self):
        users = {}
        for user in self.config().get('users'):
            users[user.get('name')] = user.get('user')
        return users

    # kubectl functions

    def deployments(self):
        return self.kubectl_exec_raw(['get', 'deployments','-A','-o','json'])

    def events(self):
        return json_parse(self.kubectl('get events -A -o json'))

    def nodes(self):
        return json_parse(self.kubectl('get nodes -A -o json'))

    def persistent_volumes(self):
        return json_parse(self.kubectl('get pv -A -o json'))

    def pod_logs(self, pod_namespace, pod_name, container_name):
        params = f'logs -n {pod_namespace} {pod_name} {container_name}'
        return split_lines(self.kubectl(params))

    def pod_exec(self, pod_namespace, pod_name, container_name, exec_command):
        params = f'exec -n {pod_namespace} {pod_name} {container_name} -- {exec_command}'
        return self.kubectl(params)

    def pods(self):
        return json_parse(self.kubectl('get pods -A -o json'))

    def services(self):
        return json_parse(self.kubectl('get services -A -o json'))