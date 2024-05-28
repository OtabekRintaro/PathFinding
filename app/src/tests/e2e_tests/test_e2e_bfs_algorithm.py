import requests

from app.src.tests.e2e_tests.base_e2e_test import BaseE2ETest
from app.src.tests.e2e_tests.e2e_utils import RUNNING_STATE, FINISHED_STATE


class TestE2EBFSAlgorithm(BaseE2ETest):

    def setUp(self):
        requests.put(f'http://127.0.0.1:5000/graph/undirected')
        requests.put(f'http://127.0.0.1:5000/algorithm/bfs')

    def test_one_node_graph(self):
        # given
        TestE2EBFSAlgorithm._request_add_node()

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/0').json()
        gathered_steps = [response['algorithm']['currentStep']]
        while ((response := requests.put('http://127.0.0.1:5000/algorithm/next_step').json())
                .get('algorithm').get('currentState') == RUNNING_STATE):
            gathered_steps.append(response['algorithm']['currentStep'])

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [0])
        self.assertEqual(gathered_steps, [0])
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_two_node_unconnected_graph(self):
        # given
        TestE2EBFSAlgorithm._request_add_node()
        TestE2EBFSAlgorithm._request_add_node()

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/1').json()

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [])
        self.assertEqual(response['currentStep'], -1)
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_two_node_connected_graph(self):
        # given
        TestE2EBFSAlgorithm._request_add_node()
        TestE2EBFSAlgorithm._request_add_node()
        requests.post('http://127.0.0.1:5000/edges/0/1')

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/1').json()
        gathered_steps = [response['algorithm']['currentStep']]
        while ((response := requests.put('http://127.0.0.1:5000/algorithm/next_step').json())
                .get('algorithm').get('currentState') == RUNNING_STATE):
            gathered_steps.append(response['algorithm']['currentStep'])

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [0, 1])
        self.assertEqual(gathered_steps, [0, 1])
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_multiple_node_unconnected_graph(self):
        # given
        for i in range(10):
            TestE2EBFSAlgorithm._request_add_node()

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/9').json()

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [])
        self.assertEqual(response['currentStep'], -1)
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_multiple_node_connected_graph(self):
        # given
        for i in range(10):
            TestE2EBFSAlgorithm._request_add_node()
            if i > 0:
                requests.post(f'http://127.0.0.1:5000/edges/{i}/{i-1}')

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/9').json()
        gathered_steps = [response['algorithm']['currentStep']]
        while ((response := requests.put('http://127.0.0.1:5000/algorithm/next_step').json())
                .get('algorithm').get('currentState') == RUNNING_STATE):
            gathered_steps.append(response['algorithm']['currentStep'])

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [i for i in range(10)])
        self.assertEqual(gathered_steps, [i for i in range(10)])
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_multiple_node_two_unconnected_graphs(self):
        # given
        for i in range(10):
            TestE2EBFSAlgorithm._request_add_node()
            if i > 0:
                requests.post(f'http://127.0.0.1:5000/edges/{i}/{i-1}')

        requests.delete(f'http://127.0.0.1:5000/node/5')

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/8').json()

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [])
        self.assertEqual(response['currentStep'], -1)
        self.assertEqual(response['currentState'], FINISHED_STATE)
