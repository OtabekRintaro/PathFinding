from app.src.model.exceptions.invalidnode_exception import InvalidNodeException
from app.src.model.graph import Graph
from app.src.model.node import Node


class UndirectedGraph(Graph):

    def __init__(self, nodes: list = None, edges: list = None):
        super().__init__(nodes, edges)

    def add_node(self) -> Node:
        new_node = Node()
        self.nodes.append(new_node)
        self.edges.append([])
        return new_node

    def remove_node(self, index):
        self.nodes.pop(index)

        self.edges.pop(index)

        for edge in self.edges:
            index_to_pop = -1
            for i in range(len(edge)):
                if edge[i] == index:
                    index_to_pop = i
            if index_to_pop != -1:
                edge.pop(index_to_pop)
            for i in range(len(edge)):
                if edge[i] > index:
                    edge[i] -= 1

    def add_edge(self, first_node, second_node):
        if not (first_node in self.nodes or second_node in self.nodes):
            raise InvalidNodeException("One of the nodes in the edge is not in the nodes set.")
        first_node_index = self.nodes.index(first_node)
        second_node_index = self.nodes.index(second_node)
        self.edges[first_node_index].append(second_node_index)
        self.edges[second_node_index].append(first_node_index)

    def remove_edge(self, first_node, second_node):
        if not (first_node in self.nodes or second_node in self.nodes):
            raise InvalidNodeException("One of the nodes in the edge is not in the nodes set.")
        first_node_index = self.nodes.index(first_node)
        second_node_index = self.nodes.index(second_node)
        if not (second_node_index in self.edges[first_node_index] or first_node_index in self.edges[second_node_index]):
            raise InvalidNodeException("There is no edge between the edges")
        self.edges[first_node_index].remove(second_node_index)
        self.edges[second_node_index].remove(first_node_index)
