import unittest

from app.src.model.graph.directedgraph import DirectedGraph
from app.src.model.graph.undirectedgraph import UndirectedGraph
from app.src.persistence.json_to_graph import JsonToGraph

NODES_EXPECTED = [0, 1, 2, 3, 4]
EDGES_EXPECTED_UNDIRECTED = [
      [[1, 1]],
      [[0, 1], [2, -10], [3, 1]],
      [[1, -10], [4, 1]],
      [[1, 1], [4, 9]],
      [[2, 1], [3, 9]]
    ]

EDGES_EXPECTED_DIRECTED = [
      [[1, 1]],
      [[2, -10], [3, 1]],
      [[4, 1]],
      [[4, 9]],
      []
    ]


class TestJsonToGraph(unittest.TestCase):
    def setUp(self):
        self.json_path = ('C:\\Users\\mykye\\Desktop\\Thesis_PathFinding\\app\\src\\persistence\\graph_templates'
                          '\\custom_graph1.json')

    def test_json_to_undirected_graph(self):
        # given-when
        graph = JsonToGraph.json_to_graph(self.json_path, UndirectedGraph)

        # then
        self.assertIsInstance(graph, UndirectedGraph)
        self.assertEqual([index for index in range(len(graph.nodes))], NODES_EXPECTED)
        self.assertEqual(graph.edges, EDGES_EXPECTED_UNDIRECTED)

    def test_json_to_directed_graph(self):
        # given-when
        graph = JsonToGraph.json_to_graph(self.json_path, DirectedGraph)

        # then
        self.assertIsInstance(graph, DirectedGraph)
        self.assertEqual([index for index in range(len(graph.nodes))], NODES_EXPECTED)
        self.assertEqual(graph.edges, EDGES_EXPECTED_DIRECTED)
