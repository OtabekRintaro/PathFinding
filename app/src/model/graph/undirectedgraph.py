from app.src.model.exceptions.invalidnode_exception import InvalidNodeException
from app.src.model.graph.graph import Graph
from app.src.model.graph.node import Node


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
                if edge[i][0] == index:
                    index_to_pop = i
            if index_to_pop != -1:
                edge.pop(index_to_pop)
            for i in range(len(edge)):
                if edge[i][0] > index:
                    edge[i][0] -= 1

    def add_edge(self, first_node, second_node, weight=0):
        if not (first_node in self.nodes or second_node in self.nodes):
            raise InvalidNodeException("One of the nodes in the edge is not in the nodes set.")
        first_node_index = self.nodes.index(first_node)
        second_node_index = self.nodes.index(second_node)
        self.edges[first_node_index].append([second_node_index, weight])
        self.edges[second_node_index].append([first_node_index, weight])

    def set_weight(self, first_node, second_node, weight):
        if not (first_node in self.nodes or second_node in self.nodes):
            raise InvalidNodeException("One of the nodes in the edge is not in the nodes set.")
        first_node_index = self.nodes.index(first_node)
        second_node_index = self.nodes.index(second_node)
        second_node_in_first_nodes_index = [node[0] for node in self.edges[first_node_index]].index(second_node_index)
        first_node_in_second_nodes_index = [node[0] for node in self.edges[second_node_index]].index(first_node_index)

        self.edges[first_node_index][second_node_in_first_nodes_index][1] = weight
        self.edges[second_node_index][first_node_in_second_nodes_index][1] = weight

    def remove_edge(self, first_node, second_node):
        if not (first_node in self.nodes or second_node in self.nodes):
            raise InvalidNodeException("One of the nodes in the edge is not in the nodes set.")
        first_node_index = self.nodes.index(first_node)
        second_node_index = self.nodes.index(second_node)
        if not (second_node_index in [node[0] for node in self.edges[first_node_index]] or
                first_node_index in [node[0] for node in self.edges[second_node_index]]):
            raise InvalidNodeException("There is no edge between the nodes")
        first_to_second_edge_index = [node[0] for node in self.edges[first_node_index]].index(second_node_index)
        second_to_first_edge_index = [node[0] for node in self.edges[second_node_index]].index(first_node_index)
        self.edges[first_node_index].pop(first_to_second_edge_index)
        self.edges[second_node_index].pop(second_to_first_edge_index)
