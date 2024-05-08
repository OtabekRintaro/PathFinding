from unittest import TestCase

import requests


class BaseE2ETest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        response = requests.delete("http://127.0.0.1:5000/graph")
        response.raise_for_status()
        response = requests.delete("http://127.0.0.1:5000/algorithm")
        response.raise_for_status()

    @staticmethod
    def _request_add_node():
        requests.post("http://127.0.0.1:5000/node").json()
        return requests.get("http://127.0.0.1:5000/graph").json()

    def _get_graph(self):
        return requests.get("http://127.0.0.1:5000/graph").json()
