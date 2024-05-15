from app.main import Storage
from app.src.model.algorithms.algorithm_factory import algorithm_names
from app.src.model.graph.node import NodeIDGenerator


RUNNING_STATE = 'running'
FINISHED_STATE = 'finished'


class AlgorithmResponseHandler:
    @staticmethod
    def choose_algorithm(algorithm_name):
        Storage.change_algorithm(algorithm_names.get(algorithm_name))
        updated_table = Storage.database.get_tables().get('algorithm', {})
        updated_table.update({'description': Storage.algorithm.description()})
        return AlgorithmResponseHandler._update_database_data(updated_table)

    @staticmethod
    def run_algorithm(source, target):
        algorithm_data = Storage.algorithm.run(Storage.graph.edges, source, target)
        if algorithm_data['path'] == Storage.algorithm.PATH_NOT_FOUND:
            algorithm_data.update({'currentStep': -1, 'currentState': FINISHED_STATE})
        else:
            algorithm_data.update({'currentStep': 0, 'currentState': RUNNING_STATE})

        return AlgorithmResponseHandler._update_database_data(algorithm_data)

    @staticmethod
    def do_step():
        updated_table = Storage.database.get_tables().get('algorithm')
        if updated_table.get('isBellmanFord', '') == 'True':
            if updated_table['currentLink'] >= len(updated_table['links']) - 1 or updated_table['currentLink'] == -1:
                updated_table.update({'currentLink': -1, 'currentState': FINISHED_STATE})
            else:
                updated_table.update({'currentLink': (updated_table['currentLink'] + 1)})
        else:
            if updated_table['currentStep'] >= len(updated_table['steps']) - 1:
                updated_table.update({'currentStep': -1, 'currentState': FINISHED_STATE})
            else:
                updated_table.update({'currentStep': (updated_table['currentStep'] + 1)})
        return AlgorithmResponseHandler._update_database_data(updated_table)

    @staticmethod
    def get_algorithm():
        return {'algorithm': Storage.database.get_table('algorithm')}

    @staticmethod
    def clear_algorithm():
        cleared_table = {}
        return AlgorithmResponseHandler._update_database_data(cleared_table)

    @staticmethod
    def _update_database_data(algorithm_data):
        new_table = {'graph': {'nodes': NodeIDGenerator.ids, 'edges': AlgorithmResponseHandler._get_graph_edges()},
                     'algorithm': algorithm_data}
        Storage.database.add_table(new_table)
        return new_table

    @staticmethod
    def _get_graph_edges():
        edges_obj = dict()
        for i in range(len(Storage.graph.edges)):
            edges_obj.update({i: Storage.graph.edges[i]})
        return edges_obj
