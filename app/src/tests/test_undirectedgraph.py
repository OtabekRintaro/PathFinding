from app.src.model.undirectedgraph import UndirectedGraph
import unittest

from app.src.model.node import NodeIDGenerator


class UndirectedGraphTest(unittest.TestCase):

    def setUp(self):
        self.graph = UndirectedGraph()

    def tearDown(self):
        self.graph = None

    def test_add_node(self):
        # given-when
        created_node = self.graph.add_node()

        # then
        self.assertEqual(len(self.graph.nodes), 1)
        self.assertEqual(self.graph.nodes[0], created_node)
        self.assertEqual(NodeIDGenerator.get_id_of_node(created_node), 0)

    def test_remove_node(self):
        # given
        created_node = self.graph.add_node()
        id = NodeIDGenerator.get_id_of_node(created_node)

        # when
        self.graph.remove_node(id)

        # then
        self.assertEqual(len(self.graph.nodes), 0)

    def test_add_multiple_nodes(self):
        # given-when
        nodes = []
        for i in range(10):
            nodes.append(self.graph.add_node())

        # then
        self.assertListEqual(self.graph.nodes, nodes)
        self.assertEqual(len(self.graph.nodes), 10)
        self.assertNotEqual(nodes[0], nodes[1])
        i = 0
        for node in nodes:
            self.assertEqual(NodeIDGenerator.get_id_of_node(node), i)
            i += 1

    def test_remove_multiple_nodes(self):
        # given
        nodes = []
        for i in range(10):
            nodes.append(self.graph.add_node())

        # when
        for i in range(10):
            self.graph.remove_node(0)
        nodes.clear()

        # then
        self.assertListEqual(self.graph.nodes, [])
        self.assertEqual(len(self.graph.nodes), 0)

    def test_add_and_remove_multiple_nodes(self):
        # given-when
        nodes = []
        for i in range(10):
            nodes.append(self.graph.add_node())
            nodes.pop(i)
            self.graph.remove_node(i)
            nodes.append(self.graph.add_node())

        # then
        self.assertListEqual(self.graph.nodes, nodes)
        self.assertEqual(len(self.graph.nodes), 10)
        self.assertNotEqual(nodes[0], nodes[1])
        i = 0
        for node in nodes:
            self.assertEqual(NodeIDGenerator.get_id_of_node(node), i)
            i += 1

    def test_add_edge(self):
        # given-when
        node_with_outcoming_edge = self.graph.add_node()
        node_with_incoming_edge = self.graph.add_node()
        self.graph.add_edge(node_with_outcoming_edge, node_with_incoming_edge)

        # then
        self.assertEqual(len(self.graph.nodes), 2)
        self.assertEqual(len(self.graph.edges), 2)
        self._assert_all_edges_len_equal(1)

    def test_add_multiple_edges(self):
        # given-when
        nodes = []
        for i in range(10):
            nodes.append(self.graph.add_node())
            nodes.append(self.graph.add_node())
            self.graph.add_edge(nodes[2*i], nodes[(2*i)+1])

        # then
        self.assertListEqual(self.graph.nodes, nodes)
        self.assertEqual(len(self.graph.nodes), 20)
        self.assertEqual(len(self.graph.edges), 20)
        self._assert_all_edges_len_equal(1)

    def test_add_multiple_edges_to_one_edge(self):
        # given-when
        nodes = list()
        nodes.append(self.graph.add_node())

        for i in range(10):
            nodes.append(self.graph.add_node())
            self.graph.add_edge(nodes[0], nodes[i+1])

        # then
        self.assertListEqual(self.graph.nodes, nodes)
        self.assertEqual(len(self.graph.nodes), 11)
        self.assertEqual(len(self.graph.edges), 11)
        self.assertEqual(len(self.graph.edges[0]), 10)
        self.assertEqual([self._find_node_by_id(node_id) for node_id in self.graph.edges[0]], nodes[1:])

    def test_remove_edge(self):
        # given
        node_with_outcoming_edge = self.graph.add_node()
        node_with_incoming_edge = self.graph.add_node()
        self.graph.add_edge(node_with_outcoming_edge, node_with_incoming_edge)

        # when
        self.graph.remove_edge(node_with_outcoming_edge, node_with_incoming_edge)

        # then
        self.assertEqual(len(self.graph.nodes), 2)
        self.assertEqual(len(self.graph.edges), 2)
        self._assert_all_edges_len_equal(0)

    def test_remove_first_node_with_an_edge(self):
        # given
        node_with_outcoming_edge = self.graph.add_node()
        node_with_incoming_edge = self.graph.add_node()
        self.graph.add_edge(node_with_outcoming_edge, node_with_incoming_edge)

        # when
        self.graph.remove_node(NodeIDGenerator.get_id_of_node(node_with_outcoming_edge))
        del node_with_outcoming_edge

        # then
        self.assertEqual(len(self.graph.edges[0]), 0)
        self.assertEqual(NodeIDGenerator.get_id_of_node(self.graph.nodes[0]), 0)
        self.assertEqual(len(self.graph.nodes), 1)
        self._assert_all_edges_len_equal(0)

    def test_remove_second_node_with_an_edge(self):
        # given
        node_with_outcoming_edge = self.graph.add_node()
        node_with_incoming_edge = self.graph.add_node()
        self.graph.add_edge(node_with_outcoming_edge, node_with_incoming_edge)

        # when
        self.graph.remove_node(NodeIDGenerator.get_id_of_node(node_with_incoming_edge))
        del node_with_incoming_edge

        # then
        self.assertEqual(NodeIDGenerator.get_id_of_node(self.graph.nodes[0]), 0)
        self.assertEqual(len(self.graph.nodes), 1)
        self.assertEqual(len(self.graph.edges), 1)
        self._assert_all_edges_len_equal(0)

    def test_remove_three_nodes_with_edges_between(self):
        # given
        node1 = self.graph.add_node()
        node2 = self.graph.add_node()
        node3 = self.graph.add_node()

        self.graph.add_edge(node1, node2)
        self.graph.add_edge(node2, node3)

        # when
        self.graph.remove_node(NodeIDGenerator.get_id_of_node(node1))
        del node1

        # then
        self.assertEqual([NodeIDGenerator.get_id_of_node(node) for node in self.graph.nodes], [0, 1])
        self.assertEqual(len(self.graph.nodes), 2)
        self.assertEqual(len(self.graph.edges), 2)
        for edge in self.graph.edges:
            self.assertEqual(len(edge), 1)

        # when
        self.graph.remove_node(NodeIDGenerator.get_id_of_node(node2))
        del node2

        # then
        self.assertEqual([NodeIDGenerator.get_id_of_node(node) for node in self.graph.nodes], [0])
        self.assertEqual(len(self.graph.nodes), 1)
        self.assertEqual(len(self.graph.edges), 1)

        # when
        self.graph.remove_node(NodeIDGenerator.get_id_of_node(node3))
        del node3

        # then
        self.assertEqual(len(self.graph.nodes), 0)
        self.assertEqual(len(self.graph.edges), 0)

    def test_remove_three_nodes_with_edges_between_starting_from_middle(self):
        # given
        node1 = self.graph.add_node()
        node2 = self.graph.add_node()
        node3 = self.graph.add_node()

        self.graph.add_edge(node1, node2)
        self.graph.add_edge(node2, node3)

        # when
        self.graph.remove_node(NodeIDGenerator.get_id_of_node(node1))
        del node1

        # then
        self.assertEqual([NodeIDGenerator.get_id_of_node(node) for node in self.graph.nodes], [0, 1])
        self.assertEqual(len(self.graph.nodes), 2)
        self.assertEqual(len(self.graph.edges), 2)
        for edge in self.graph.edges:
            self.assertEqual(len(edge), 1)

        # when
        self.graph.remove_node(NodeIDGenerator.get_id_of_node(node2))
        del node2

        # then
        self.assertEqual([NodeIDGenerator.get_id_of_node(node) for node in self.graph.nodes], [0])
        self.assertEqual(len(self.graph.nodes), 1)
        self.assertEqual(len(self.graph.edges), 1)

        # when
        self.graph.remove_node(NodeIDGenerator.get_id_of_node(node3))
        del node3

        # then
        self.assertEqual(len(self.graph.nodes), 0)
        self.assertEqual(len(self.graph.edges), 0)

    def test_remove_multiple_edges(self):
        # given
        nodes = []
        for i in range(10):
            nodes.append(self.graph.add_node())
            nodes.append(self.graph.add_node())
            self.graph.add_edge(nodes[2*i], nodes[(2*i)+1])

        # when
        for i in range(10):
            self.graph.remove_edge(nodes[2*i], nodes[(2*i)+1])

        # then
        self.assertListEqual(self.graph.nodes, nodes)
        self.assertEqual(len(self.graph.nodes), 20)
        self.assertEqual(len(self.graph.edges), 20)
        self._assert_all_edges_len_equal(0)

    def _assert_all_edges_len_equal(self, num):
        for edge in self.graph.edges:
            self.assertEqual(len(edge), num)

    def _find_node_by_id(self, node_id):
        node_hash = NodeIDGenerator.ids_and_nodes[node_id]
        for node in self.graph.nodes:
            if node.__hash__() == node_hash:
                return node
