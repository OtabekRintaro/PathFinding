from app.main import algorithm, change_algorithm, graph
from app.src.model.algorithms.algorithm_factory import algorithm_names


class AlgorithmResponseHandler:
    @staticmethod
    def choose_algorithm(algorithm_name):
        change_algorithm(algorithm_names(algorithm_name))

    @staticmethod
    def run_algorithm(source, target):
        return algorithm.run(graph.edges, source, target)
