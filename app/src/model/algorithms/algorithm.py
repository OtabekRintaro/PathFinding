from abc import abstractmethod

INF = 10000000000
ARBITRARY_NUMBER = 10


class Algorithm:
    PATH_NOT_FOUND = []

    @property
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def run(self, graph, source, target):
        pass
