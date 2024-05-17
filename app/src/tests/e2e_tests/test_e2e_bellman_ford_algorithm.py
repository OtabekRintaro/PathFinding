import requests

from app.src.tests.e2e_tests.base_e2e_test import BaseE2ETest
from app.src.tests.e2e_tests.e2e_utils import RUNNING_STATE, FINISHED_STATE


class TestE2EBellmanFordAlgorithm(BaseE2ETest):

    def setUp(self):
        requests.put('http://127.0.0.1:5000/graph/directed')
        requests.put(f'http://127.0.0.1:5000/algorithm/bellmanford')

    def test_one_node_graph(self):
        # given
        TestE2EBellmanFordAlgorithm._request_add_node()

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/0').json()
        gathered_steps = [response['algorithm']['currentLink']]
        while ((response := requests.put('http://127.0.0.1:5000/algorithm/next_step').json())
                .get('algorithm').get('currentState') == RUNNING_STATE):
            gathered_steps.append(response['algorithm']['currentLink'])

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [0])
        self.assertEqual(response['pathCost'], 0)
        self.assertEqual(response['isBellmanFord'], 'True')
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_two_node_unconnected_graph(self):
        # given
        TestE2EBellmanFordAlgorithm._request_add_node()
        TestE2EBellmanFordAlgorithm._request_add_node()

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/1').json()

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [])
        self.assertEqual(response['isBellmanFord'], 'True')
        self.assertEqual(response['currentStep'], -1)
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_two_node_connected_graph(self):
        # given
        TestE2EBellmanFordAlgorithm._request_add_node()
        TestE2EBellmanFordAlgorithm._request_add_node()
        requests.post('http://127.0.0.1:5000/edges/0/1')

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/1').json()
        gathered_steps = [response['algorithm']['currentLink']]
        while ((response := requests.put('http://127.0.0.1:5000/algorithm/next_step').json())
                .get('algorithm').get('currentState') == RUNNING_STATE):
            gathered_steps.append(response['algorithm']['currentLink'])

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [0, 1])
        self.assertEqual(response['pathCost'], 0)
        self.assertEqual(response['isBellmanFord'], 'True')
        self.assertEqual(len(gathered_steps), len(response['links']))
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_multiple_node_unconnected_graph(self):
        # given
        for i in range(10):
            TestE2EBellmanFordAlgorithm._request_add_node()

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/9').json()

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [])
        self.assertEqual(response['pathCost'], 0)
        self.assertEqual(response['isBellmanFord'], 'True')
        self.assertEqual(response['currentLink'], -1)
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_multiple_node_connected_graph(self):
        # given
        for i in range(10):
            TestE2EBellmanFordAlgorithm._request_add_node()
            if i > 0:
                requests.post(f'http://127.0.0.1:5000/edges/{i}/{i-1}')

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/9/0').json()
        gathered_steps = [response['algorithm']['currentStep']]
        while ((response := requests.put('http://127.0.0.1:5000/algorithm/next_step').json())
                .get('algorithm').get('currentState') == RUNNING_STATE):
            gathered_steps.append(response['algorithm']['currentLink'])

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [i for i in range(9, -1, -1)])
        self.assertEqual(response['pathCost'], 0)
        self.assertEqual(response['isBellmanFord'], 'True')
        self.assertEqual(len(gathered_steps), len(response['links']))
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_multiple_node_two_unconnected_graphs(self):
        # given
        for i in range(10):
            TestE2EBellmanFordAlgorithm._request_add_node()
            if i > 0:
                requests.post(f'http://127.0.0.1:5000/edges/{i}/{i-1}')

        requests.delete(f'http://127.0.0.1:5000/node/5')

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/8').json()

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [])
        self.assertEqual(response['isBellmanFord'], 'True')
        self.assertEqual(response['currentLink'], -1)
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_custom_graph_edge_case_with_negative_number(self):
        # given
        for i in range(5):
            TestE2EBellmanFordAlgorithm._request_add_node()

        requests.post(f'http://127.0.0.1:5000/edges/0/1/1')
        requests.post(f'http://127.0.0.1:5000/edges/1/2/-10')
        requests.post(f'http://127.0.0.1:5000/edges/1/3/1')
        requests.post(f'http://127.0.0.1:5000/edges/2/4/1')
        requests.post(f'http://127.0.0.1:5000/edges/3/4/9')

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/3').json()

        gathered_steps = [response['algorithm']['currentLink']]
        while ((response := requests.put('http://127.0.0.1:5000/algorithm/next_step').json())
                .get('algorithm').get('currentState') == RUNNING_STATE):
            gathered_steps.append(response['algorithm']['currentLink'])

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [0, 1, 3])
        self.assertEqual(response['pathCost'], 2.0)
        self.assertEqual(response['isBellmanFord'], 'True')
        self.assertEqual(len(gathered_steps), len(response['links']))
        self.assertEqual(response['currentLink'], -1)
        self.assertEqual(response['currentState'], FINISHED_STATE)

    def test_custom_graph_with_floating_point_number_weights(self):
        # given
        requests.post(f'http://127.0.0.1:5000/graph/4')

        # when
        response = requests.post('http://127.0.0.1:5000/algorithm/0/7').json()

        gathered_steps = [response['algorithm']['currentStep']]
        while ((response := requests.put('http://127.0.0.1:5000/algorithm/next_step').json())
                .get('algorithm').get('currentState') == RUNNING_STATE):
            gathered_steps.append(response['algorithm']['currentStep'])

        response = response['algorithm']

        # then
        self.assertEqual(response['path'], [0, 1, 2, 4, 5, 7])
        self.assertAlmostEqual (response['pathCost'], 3.3, delta=0.00001)
        self.assertEqual(response['isBellmanFord'], 'True')
        self.assertEqual(len(gathered_steps), len(response['links']))
        self.assertEqual(response['currentLink'], -1)
        self.assertEqual(response['currentState'], FINISHED_STATE)
