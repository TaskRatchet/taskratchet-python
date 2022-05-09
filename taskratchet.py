import requests


class TaskRatchet:
    _base_url = 'https://api.taskratchet.com/api1/'
    _user_id = None
    _token = None

    def set_user_id(self, user_id):
        self._user_id = user_id

    def set_token(self, token):
        self._token = token

    def get_me(self):
        url = self._base_url + 'me'

        return self._make_request(url, 'GET')

    def update_me(self, data):
        url = self._base_url + 'me'

        return self._make_request(url, 'PUT', data)

    def get_task(self, task_id):
        url = self._base_url + 'me/tasks/' + task_id

        return self._make_request(url, 'GET')

    def update_task(self, task_id, data):
        url = self._base_url + 'me/tasks/' + task_id

        return self._make_request(url, 'PUT', data)

    def get_tasks(self):
        url = self._base_url + 'me/tasks'

        return self._make_request(url, 'GET')

    def create_task(self, data):
        url = self._base_url + 'me/tasks'

        return self._make_request(url, 'POST', data)

    def _make_request(self, url, method, data=None):
        headers = {
            'X-Taskratchet-Userid': self._user_id,
            'X-Taskratchet-Token': self._token
        }

        if data:
            response = requests.request(method, url, headers=headers, json=data)
        else:
            response = requests.request(method, url, headers=headers)

        return response.json()
