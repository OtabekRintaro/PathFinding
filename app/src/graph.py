from app.src.invalidnode_exception import InvalidNodeException
from app.src.node import Node

class Graph():
    def __init__(self):
        self.nodes = list()
        self.edges = list()
            
class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_node(self) -> Node:
        new_node = Node()
        self.nodes.append(new_node)
        self.edges.append([])
        return new_node

    def remove_node(self, index):
        self.nodes.pop(index)
        
        self.edges.pop(index)
        
        for edge in self.edges:
            for i in range(len(edge)):
                if edge[i] >= index:
                    edge[i] -= 1
        

    def add_edge(self, first_node, second_node):
        if not (first_node in self.nodes or second_node in self.nodes):
            raise InvalidNodeException("One of the nodes in the edge is not in the nodes set.")
        first_node_index = self.nodes.index(first_node)
        second_node_index = self.nodes.index(second_node)
        self.edges[first_node_index].append(second_node_index)
        self.edges[second_node_index].append(first_node_index)