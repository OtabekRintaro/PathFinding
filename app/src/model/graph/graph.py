import abc


class Graph:

    def __init__(self, nodes: list = None, edges: list = None):
        if not nodes:
            nodes = list()
        if not edges:
            edges = list()
        self.nodes = nodes
        self.edges = edges

    @abc.abstractmethod
    def add_node(self):
        pass

    @abc.abstractmethod
    def remove_node(self, index):
        pass

    @abc.abstractmethod
    def add_edge(self, first_node, second_node):
        pass
