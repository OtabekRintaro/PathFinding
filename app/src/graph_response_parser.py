from app.main import database, graph
from app.src.model.node import NodeIDGenerator

EMPTY_GRAPH_TABLE = {'graph': {'nodes': []}}


class GraphResponseParser:

    @staticmethod
    def clear_graph():
        while len(graph.nodes) > 0:
            graph.remove_node(0)
        return GraphResponseParser._update_database_data()

    @staticmethod
    def add_node():
        if database.is_empty():
            database.add_table(EMPTY_GRAPH_TABLE)
        graph.add_node()
        return GraphResponseParser._update_database_data()

    @staticmethod
    def remove_node(index):
        graph.remove_node(index)
        return GraphResponseParser._update_database_data()

    @staticmethod
    def get_nodes():
        return {'graph': database.get_table('graph')}

    @staticmethod
    def _update_database_data():
        new_table = {'graph': {'nodes': NodeIDGenerator.ids}}
        database.add_table(new_table)
        return new_table
