import unittest

from app.src.model.algorithms.algorithm import Algorithm
from app.src.model.algorithms.dfs import DFS
from app.src.model.graph.node import NodeIDGenerator
from app.src.model.graph.undirectedgraph import UndirectedGraph


class DFSTest(unittest.TestCase):
    def setUp(self):
        self.dfs = DFS()
        self.graph = UndirectedGraph()

    def tearDown(self):
        print('teardown: check len nodes', len(self.graph.nodes))
        del self.graph

    def test_empty_graph(self):
        # given-when
        path = self.dfs.run(self.graph.edges, None, None).get('path')

        # then
        self.assertEqual(path, Algorithm.PATH_NOT_FOUND)

    def test_one_node_graph(self):
        # given
        self.graph.add_node()
        node_id = self._get_node_id(0)

        # when
        print('edges', self.graph.edges)
        path = self.dfs.run(self.graph.edges, node_id, node_id).get('path')

        # then
        self.assertEqual(path, [node_id])

    def test_two_node_unconnected_graph(self):
        # given
        self.graph.add_node()
        self.graph.add_node()
        node_id1 = self._get_node_id(0)
        node_id2 = self._get_node_id(1)

        # when
        path = self.dfs.run(self.graph.edges, node_id1, node_id2).get('path')

        # then
        self.assertEqual(path, Algorithm.PATH_NOT_FOUND)

    def test_two_node_connected_graph(self):
        # given
        self.graph.add_node()
        self.graph.add_node()
        self.graph.add_node()
        self.graph.add_edge(self.graph.nodes[0], self.graph.nodes[1])
        self.graph.add_edge(self.graph.nodes[1], self.graph.nodes[2])
        node_id1 = self._get_node_id(0)
        node_id2 = self._get_node_id(1)
        node_id3 = self._get_node_id(2)

        # when
        path = self.dfs.run(self.graph.edges, node_id1, node_id3).get('path')

        # then
        self.assertEqual(path, [node_id1, node_id2, node_id3])

    def test_multiple_node_dense_connected_graph(self):
        # given
        for i in range(10):
            new_node = self.graph.add_node()
            for node in self.graph.nodes:
                self.graph.add_edge(new_node, node)

        node_id1 = self._get_node_id(0)
        node_id2 = self._get_node_id(9)

        # when
        path = self.dfs.run(self.graph.edges, node_id1, node_id2).get('path')

        # then
        self.assertEqual(path, [node_id1, node_id2])

    def test_multiple_node_sparse_connected_graph(self):
        # given
        for i in range(10):
            new_node = self.graph.add_node()
            if i > 0:
                self.graph.add_edge(new_node, self.graph.nodes[i-1])

        node_id1 = self._get_node_id(0)
        node_id2 = self._get_node_id(9)

        # when
        path = self.dfs.run(self.graph.edges, node_id1, node_id2).get('path')

        # then
        self.assertEqual(path, [self._get_node_id(i) for i in range(len(self.graph.nodes))])

    def test_multiple_node_sparse_unconnected_graph(self):
        # given
        new_node = None
        for i in range(10):
            new_node = self.graph.add_node()
            if i > 0:
                self.graph.add_edge(new_node, self.graph.nodes[i - 1])
        new_node = None

        self.graph.remove_node(5)

        node_id1 = self._get_node_id(0)
        node_id2 = self._get_node_id(8)

        print(self.graph.edges)
        # when
        path = self.dfs.run(self.graph.edges, node_id1, node_id2).get('path')

        # then
        self.assertEqual(path, Algorithm.PATH_NOT_FOUND)

    def _get_node_id(self, index):
        return NodeIDGenerator.get_id_of_node(self.graph.nodes[index])
