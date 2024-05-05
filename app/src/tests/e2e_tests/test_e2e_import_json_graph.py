import requests
from app.src.model.graph.directedgraph import DirectedGraph
from app.src.model.graph.undirectedgraph import UndirectedGraph
from app.src.persistence.json_to_graph import JsonToGraph
from app.src.tests.e2e_tests.base_e2e_test import BaseE2ETest

NODES_EXPECTED = [0, 1, 2, 3, 4]
EDGES_EXPECTED_UNDIRECTED = {
      '0': [[1, 1]],
      '1': [[0, 1], [2, -10], [3, 1]],
      '2': [[1, -10], [4, 1]],
      '3': [[1, 1], [4, 9]],
      '4': [[2, 1], [3, 9]]
}

EDGES_EXPECTED_DIRECTED = {
      '0': [[1, 1]],
      '1': [[2, -10], [3, 1]],
      '2': [[4, 1]],
      '3': [[4, 9]],
      '4': [],
}


class TestE2EJsonGraphImport(BaseE2ETest):

    def test_json_to_undirected_graph(self):
        # given
        requests.put('http://localhost:5000/graph/undirected')

        # when
        graph = requests.post('http://localhost:5000/graph/1').json().get('graph')

        # then
        self.assertEqual(graph['nodes'], NODES_EXPECTED)
        self.assertEqual(graph['edges'], EDGES_EXPECTED_UNDIRECTED)

    def test_json_to_directed_graph(self):
        # given
        requests.put('http://localhost:5000/graph/directed')

        # when
        graph = requests.post('http://localhost:5000/graph/1').json().get('graph')

        # then
        self.assertEqual(graph['nodes'], NODES_EXPECTED)
        self.assertEqual(graph['edges'], EDGES_EXPECTED_DIRECTED)
