from unittest import TestCase

import requests


class BaseE2ETest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        requests.delete("http://127.0.0.1:5000/graph")

    @staticmethod
    def _request_add_node():
        return requests.post("http://127.0.0.1:5000/node").json()