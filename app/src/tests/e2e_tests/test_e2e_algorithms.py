import requests

from app.src.tests.e2e_tests.base_e2e_test import BaseE2ETest


class TestE2EAlgorithms(BaseE2ETest):

    def test_one_node_graph(self):
        # given
        requests.put(f'http://127.0.0.1:5000/algorithm/dfs')
        TestE2EAlgorithms._request_add_node()

        # when
        response = requests.get('http://127.0.0.1:5000/algorithm/0/0').json()

        # then
        self.assertEqual(response['path'], [0])

    def test_two_node_unconnected_graph(self):
        # given
        requests.put(f'http://127.0.0.1:5000/algorithm/dfs')
        TestE2EAlgorithms._request_add_node()
        TestE2EAlgorithms._request_add_node()

        # when
        response = requests.get('http://127.0.0.1:5000/algorithm/0/1').json()

        # then
        self.assertEqual(response['path'], [])

    def test_two_node_connected_graph(self):
        # given
        requests.put(f'http://127.0.0.1:5000/algorithm/dfs')
        TestE2EAlgorithms._request_add_node()
        TestE2EAlgorithms._request_add_node()
        requests.post('http://127.0.0.1:5000/edges/0/1')

        # when
        response = requests.get('http://127.0.0.1:5000/algorithm/0/1').json()

        # then
        self.assertEqual(response['path'], [0, 1])

    def test_multiple_node_unconnected_graph(self):
        # given
        requests.put(f'http://127.0.0.1:5000/algorithm/dfs')
        for i in range(10):
            TestE2EAlgorithms._request_add_node()

        # when
        response = requests.get('http://127.0.0.1:5000/algorithm/0/9').json()

        # then
        self.assertEqual(response['path'], [])

    def test_multiple_node_connected_graph(self):
        # given
        requests.put(f'http://127.0.0.1:5000/algorithm/dfs')
        for i in range(10):
            TestE2EAlgorithms._request_add_node()
            if i > 0:
                requests.post(f'http://127.0.0.1:5000/edges/{i}/{i-1}')

        # when
        response = requests.get('http://127.0.0.1:5000/algorithm/0/9').json()

        # then
        self.assertEqual(response['path'], [i for i in range(10)])

    def test_multiple_node_two_unconnected_graphs(self):
        # given
        requests.put(f'http://127.0.0.1:5000/algorithm/dfs')
        for i in range(10):
            TestE2EAlgorithms._request_add_node()
            if i > 0:
                requests.post(f'http://127.0.0.1:5000/edges/{i}/{i-1}')

        requests.delete(f'http://127.0.0.1:5000/node/5')

        # when
        response = requests.get('http://127.0.0.1:5000/algorithm/0/9').json()

        # then
        self.assertEqual(response['path'], [])
