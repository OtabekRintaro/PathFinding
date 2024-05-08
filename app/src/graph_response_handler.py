import os.path

from app.main import Storage
from app.src.model.graph.node import NodeIDGenerator
from app.src.model.graph.graph_factory import graph_types
from app.src.algorithm_response_handler import AlgorithmResponseHandler
from app.src.persistence.json_to_graph import JsonToGraph

EMPTY_GRAPH_TABLE = {'graph': {'nodes': [], 'edges': {}}}


class GraphResponseHandler:

    @staticmethod
    def set_graph_type(graph_type_name):
        Storage.change_graph(graph_types.get(graph_type_name)())
        return GraphResponseHandler._update_database_data()

    @staticmethod
    def import_ready_graph(index_of_graph, is_e2e=False):
        print('handling response')
        path_to_graph_file = ('src' + os.sep + 'persistence' + os.sep + 'graph_templates' + os.sep +
                              'custom_graph' + str(index_of_graph) + '.json')
        if is_e2e:
            path_to_graph_file = ('app' + os.sep + 'src' + os.sep + 'persistence' + os.sep + 'graph_templates' + os.sep +
                                  'custom_graph' + str(index_of_graph) + '.json')
        print('importing graph')
        Storage.graph = JsonToGraph.json_to_graph(path_to_graph_file, Storage.graph.__class__)
        return GraphResponseHandler._update_database_data()

    @staticmethod
    def clear_graph():
        while len(Storage.graph.nodes) > 0:
            Storage.graph.remove_node(0)
        return GraphResponseHandler._update_database_data()

    @staticmethod
    def add_node():
        if Storage.database.is_empty():
            Storage.database.add_table(EMPTY_GRAPH_TABLE)
        Storage.graph.add_node()
        return GraphResponseHandler._update_database_data()

    @staticmethod
    def remove_node(index):
        Storage.graph.remove_node(index)
        return GraphResponseHandler._update_database_data()

    @staticmethod
    def get_graph():
        graph_data = {'graph': Storage.database.get_table('graph')}
        if graph_data['graph'] == {}:
            graph_data.update({'nodes': [], 'edges': {}})
        return graph_data

    @staticmethod
    def add_edge(first_node_id, second_node_id, weight=0):
        first_node = GraphResponseHandler._find_node_by_id(first_node_id)
        second_node = GraphResponseHandler._find_node_by_id(second_node_id)
        Storage.graph.add_edge(first_node, second_node, weight)
        return GraphResponseHandler._update_database_data()

    @staticmethod
    def set_weight(first_node_id, second_node_id, weight):
        first_node = GraphResponseHandler._find_node_by_id(first_node_id)
        second_node = GraphResponseHandler._find_node_by_id(second_node_id)
        Storage.graph.set_weight(first_node, second_node, weight)
        return GraphResponseHandler._update_database_data()

    @staticmethod
    def remove_edge(first_node_id, second_node_id):
        first_node = GraphResponseHandler._find_node_by_id(first_node_id)
        second_node = GraphResponseHandler._find_node_by_id(second_node_id)
        Storage.graph.remove_edge(first_node, second_node)
        return GraphResponseHandler._update_database_data()

    @staticmethod
    def _find_node_by_id(node_id):
        node_hash = NodeIDGenerator.ids_and_nodes[node_id]
        for node in Storage.graph.nodes:
            if node.__hash__() == node_hash:
                return node

    @staticmethod
    def _update_database_data():
        new_table = {'graph': {'nodes': NodeIDGenerator.ids, 'edges': GraphResponseHandler._get_graph_edges()}}
        AlgorithmResponseHandler.clear_algorithm()
        Storage.database.add_table(new_table)
        return new_table

    @staticmethod
    def _get_graph_edges():
        edges_obj = dict()
        for i in range(len(Storage.graph.edges)):
            edges_obj.update({i: Storage.graph.edges[i]})
        return edges_obj
