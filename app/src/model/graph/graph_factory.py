from app.src.model.graph.directedgraph import DirectedGraph
from app.src.model.graph.undirectedgraph import UndirectedGraph


class GraphFactory:
    @staticmethod
    def create_UndirectedGraph():
        return UndirectedGraph()

    @staticmethod
    def create_DirectedGraph():
        return DirectedGraph()


graph_types = {
    'undirected': GraphFactory.create_UndirectedGraph,
    'directed': GraphFactory.create_DirectedGraph,
}