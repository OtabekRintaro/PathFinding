import requests

from app.src.tests.e2e_tests.base_e2e_test import BaseE2ETest

EXPECTED_GRAPHS = [
    {'graph':
        {
            'nodes': [],
            'edges': {}
        }
     },
    {'graph':
        {
            'nodes': [0],
            'edges': {
                '0': []
            }
        }
     },
    {'graph':
        {
            'nodes': [0, 1],
            'edges': {
                '0': [1],
                '1': [0]
            }
        }
     },
    {'graph':
        {
            'nodes': [0, 1],
            'edges': {
                '0': [],
                '1': []
            }
        }
     }
]


class UndirectedGraphE2ETest(BaseE2ETest):

    def test_add_node(self):
        # given-when
        graph = UndirectedGraphE2ETest._request_add_node()

        # then
        self.assertEqual(graph, EXPECTED_GRAPHS[1])

    def test_remove_node(self):
        # given
        UndirectedGraphE2ETest._request_add_node()
        node_id = 0

        # when
        graph = requests.delete(f'http://127.0.0.1:5000/node/{node_id}').json()

        # then
        self.assertEqual(graph, EXPECTED_GRAPHS[0])

    def test_get_nodes(self):
        # given-when
        graph = requests.get("http://127.0.0.1:5000/graph").json()

        # then
        self.assertEqual(graph, EXPECTED_GRAPHS[0])

    def test_add_edge(self):
        # given
        UndirectedGraphE2ETest._request_add_node()
        UndirectedGraphE2ETest._request_add_node()

        # when
        graph = requests.post("http://127.0.0.1:5000/edges/0/1").json()

        # then
        self.assertEqual(graph, EXPECTED_GRAPHS[2])

    def test_remove_edge(self):
        # given
        UndirectedGraphE2ETest._request_add_node()
        UndirectedGraphE2ETest._request_add_node()
        requests.post("http://127.0.0.1:5000/edges/0/1").json()

        # when
        graph = requests.delete("http://127.0.0.1:5000/edges/0/1").json()

        # then
        self.assertEqual(graph, EXPECTED_GRAPHS[3])

