from app.main import database, graph
from app.src.model.node import NodeIDGenerator

EMPTY_GRAPH_TABLE = {'graph': {'nodes': [], 'edges': {}}}


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
    def add_edge(first_node_id, second_node_id):
        first_node = GraphResponseParser._find_node_by_id(first_node_id)
        second_node = GraphResponseParser._find_node_by_id(second_node_id)
        graph.add_edge(first_node, second_node)
        return GraphResponseParser._update_database_data()

    @staticmethod
    def remove_edge(first_node_id, second_node_id):
        first_node = GraphResponseParser._find_node_by_id(first_node_id)
        second_node = GraphResponseParser._find_node_by_id(second_node_id)
        graph.remove_edge(first_node, second_node)
        return GraphResponseParser._update_database_data()

    @staticmethod
    def _find_node_by_id(node_id):
        node_hash = NodeIDGenerator.ids_and_nodes[node_id]
        for node in graph.nodes:
            if node.__hash__() == node_hash:
                return node

    @staticmethod
    def _update_database_data():
        new_table = {'graph': {'nodes': NodeIDGenerator.ids, 'edges': GraphResponseParser._get_graph_edges()}}
        database.add_table(new_table)
        return new_table

    @staticmethod
    def _get_graph_edges():
        edges_obj = dict()
        for i in range(len(graph.edges)):
            edges_obj.update({i: graph.edges[i]})
        return edges_obj
