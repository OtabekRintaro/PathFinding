import unittest

from app.src.node import NodeIDGenerator, Node

class NodeTets(unittest.TestCase):
    def setUp(self):
        self.nodes = []

    def tearDown(self):
        self.nodes.clear()

    def test_create_node(self):
        #given-when
        self.nodes.append(Node())

        #then
        self.assertEqual(NodeIDGenerator.ids[0], 0)
        self.assertIn(0, NodeIDGenerator.nodes_and_ids.keys())
        self.assertEqual(NodeIDGenerator.nodes_and_ids[0], self.nodes[0].__hash__())
    
    def test_create_and_delete_node(self):
        #given
        self.nodes.append(Node())

        #when
        self.nodes.pop(0)

        #then
        self.assertEqual(len(NodeIDGenerator.ids), 0)
        self.assertEqual(len(NodeIDGenerator.nodes_and_ids.keys()), 0)

    def test_create_multiple_nodes(self):
        #given-when
        for i in range(10):
            self.nodes.append(Node())
        
        #then
        self.assertEqual(len(self.nodes), 10)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.nodes_and_ids.keys())
            self.assertEqual(NodeIDGenerator.nodes_and_ids[i], self.nodes[i].__hash__())

    def test_create_multiple_nodes_delete_first(self):
        #given
        for i in range(10):
            self.nodes.append(Node())
        
        #when
        self.nodes.pop(0)

        #then
        self.assertEqual(len(self.nodes), 9)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.nodes_and_ids.keys())
            self.assertEqual(NodeIDGenerator.nodes_and_ids[i], self.nodes[i].__hash__())

    def test_create_multiple_nodes_delete_middle(self):
        #given
        for i in range(10):
            self.nodes.append(Node())
        
        #when
        self.nodes.pop(4)

        #then
        self.assertEqual(len(self.nodes), 9)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.nodes_and_ids.keys())
            self.assertEqual(NodeIDGenerator.nodes_and_ids[i], self.nodes[i].__hash__())

    def test_create_multiple_nodes_delete_last(self):
        #given
        for i in range(10):
            self.nodes.append(Node())
        
        #when
        self.nodes.pop(9)

        #then
        self.assertEqual(len(self.nodes), 9)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.nodes_and_ids.keys())
            self.assertEqual(NodeIDGenerator.nodes_and_ids[i], self.nodes[i].__hash__())

    def test_create_and_delete_multiple_times(self):
        #given-when
        for i in range(10):
            self.nodes.append(Node())
            self.nodes.pop(i)
            self.nodes.append(Node())

        #then
        self.assertEqual(len(self.nodes), 10)
        for i in range(0, len(self.nodes)):
            self.assertEqual(NodeIDGenerator.ids[i], i)
            self.assertIn(i, NodeIDGenerator.nodes_and_ids.keys())
            self.assertEqual(NodeIDGenerator.nodes_and_ids[i], self.nodes[i].__hash__())