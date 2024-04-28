from abc import abstractmethod


class Algorithm:
    PATH_NOT_FOUND = []



    @abstractmethod
    def run(self, graph, source, target):
        pass
