from app.src.model.algorithms.bellman_ford import BellmanFord
from app.src.model.algorithms.bfs import BFS
from app.src.model.algorithms.dfs import DFS
from app.src.model.algorithms.dijkstra import Dijkstra


class AlgorithmFactory:
    @staticmethod
    def create_DFS():
        return DFS()

    @staticmethod
    def create_BFS():
        return BFS()

    @staticmethod
    def create_Dijkstra():
        return Dijkstra()

    @staticmethod
    def create_BellmanFord():
        return BellmanFord()


algorithm_names = {
    'dfs': AlgorithmFactory.create_DFS(),
    'bfs': AlgorithmFactory.create_BFS(),
    'dijkstra': AlgorithmFactory.create_Dijkstra(),
    'bellmanford': AlgorithmFactory.create_BellmanFord()
}
