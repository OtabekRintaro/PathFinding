from unittest import TestCase
import requests

from app.src.tests.e2e_tests.test_e2e_utils import get_ids_and_nodes, set_default_undirected_graph


class BaseE2ETest(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        requests.post("http://127.0.0.1:5000/graph/clear")


class UndirectedGraphE2ETest(BaseE2ETest):

    def test_add_node(self):
        # given-when
        graphs = requests.post("http://127.0.0.1:5000/node").json()
        print(graphs)
        # then
        self.assertEqual(graphs, {'graph': {'nodes': [0]}})

    def test_remove_node(self):
        # given
        requests.post("http://127.0.0.1:5000/node").json()
        node_id = 0

        # when
        graph = requests.post(f'http://127.0.0.1:5000/node/{node_id}').json()

        # then
        self.assertEqual(graph, {'graph': {'nodes': []}})

    def test_get_nodes(self):
        # given-when
        graph = requests.get("http://127.0.0.1:5000/nodes").json()

        # then
        self.assertEqual(graph, {'graph': {'nodes': []}})
