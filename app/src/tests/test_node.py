import unittest

from app.src.model.graph.node import NodeIDGenerator, Node


class NodeTest(unittest.TestCase):
    def setUp(self):
        self.nodes = []

    def tearDown(self):
        self.nodes.clear()

    def test_create_node(self):
        # given-when
        self.nodes.append(Node())

        # then
        self.assertEqual(NodeIDGenerator.ids[0], 0)
        self.assertIn(0, NodeIDGenerator.ids_and_nodes.keys())
        self.assertEqual(NodeIDGenerator.ids_and_nodes[0], self.nodes[0].__hash__())
    
    def test_create_and_delete_node(self):
        # given
        self.nodes.append(Node())

        # when
        self.nodes.pop(0)

        # then
        self.assertEqual(len(NodeIDGenerator.ids), 0)
        self.assertEqual(len(NodeIDGenerator.ids_and_nodes.keys()), 0)

    def test_create_multiple_nodes(self):
        # given-when
        for i in range(10):
            self.nodes.append(Node())
        
        # then
        self.assertEqual(len(self.nodes), 10)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.ids_and_nodes.keys())
            self.assertEqual(NodeIDGenerator.ids_and_nodes[i], self.nodes[i].__hash__())

    def test_create_multiple_nodes_delete_first(self):
        # given
        for i in range(10):
            self.nodes.append(Node())
        
        # when
        self.nodes.pop(0)

        # then
        self.assertEqual(len(self.nodes), 9)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.ids_and_nodes.keys())
            self.assertEqual(NodeIDGenerator.ids_and_nodes[i], self.nodes[i].__hash__())

    def test_create_multiple_nodes_delete_middle(self):
        # given
        for i in range(10):
            self.nodes.append(Node())
        
        # when
        self.nodes.pop(4)

        # then
        self.assertEqual(len(self.nodes), 9)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.ids_and_nodes.keys())
            self.assertEqual(NodeIDGenerator.ids_and_nodes[i], self.nodes[i].__hash__())

    def test_create_multiple_nodes_delete_last(self):
        # given
        for i in range(10):
            self.nodes.append(Node())
        
        # when
        self.nodes.pop(9)

        # then
        self.assertEqual(len(self.nodes), 9)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.ids_and_nodes.keys())
            self.assertEqual(NodeIDGenerator.ids_and_nodes[i], self.nodes[i].__hash__())

    def test_create_and_delete_multiple_times(self):
        # given-when
        for i in range(10):
            self.nodes.append(Node())
            self.nodes.pop(i)
            self.nodes.append(Node())

        # then
        self.assertEqual(len(self.nodes), 10)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.ids_and_nodes.keys())
            self.assertEqual(NodeIDGenerator.ids_and_nodes[i], self.nodes[i].__hash__())