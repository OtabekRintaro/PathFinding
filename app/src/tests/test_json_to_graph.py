import os
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
      [],
      [[3, 9]]
    ]


# IsLocalTestRun=True when run from the dev environment
class TestJsonToGraph(unittest.TestCase):
    def setUp(self):
        self.json_path = self._find_path(1)

    def _find_path(self, index_of_graph):
        dirs_to_find = ['app', 'src', 'persistence', 'graph_templates']
        path = os.getcwd()
        print(path)
        graph_file_name = 'custom_graph' + str(index_of_graph) + '.json'
        while len(directory := os.listdir(path)) > 0:
            if graph_file_name in directory:
                path += os.sep + graph_file_name
                break

            any_path_found = False
            for _dir in directory:
                if _dir in dirs_to_find:
                    path += os.sep + _dir
                    any_path_found = True
                    break

            if not any_path_found and len(path) < 3:
                break
            elif not any_path_found:
                path = os.sep.join(path.split(os.sep)[:-1])

        return path

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
