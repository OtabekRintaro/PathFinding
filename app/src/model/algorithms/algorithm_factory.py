from app.src.model.algorithms.dfs import DFS


class AlgorithmFactory:
    @staticmethod
    def create_DFS():
        return DFS()


algorithm_names = {
        'dfs': AlgorithmFactory.create_DFS(),
}