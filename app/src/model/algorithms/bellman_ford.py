import time

from app.src.model.algorithms.algorithm import Algorithm, INF


class BellmanFord(Algorithm):

    def run(self, graph, source, target):
        if source is None or target is None:
            return {
                'path': Algorithm.PATH_NOT_FOUND,
                'steps': [],
                'isBellmanFord': 'True',
                'links': [],
                'currentLink': -1}
        path = []
        rotate_links_times = 0
        n = len(graph)
        distances = [INF] * n
        parent = [-1] * n

        distances[source] = 0

        any_change = False
        for i in range(n):
            any_change = False
            index = 0
            for edges_of_node in graph:
                path.append(index)
                if distances[index] < INF:
                    for edge in edges_of_node:
                        to = edge[0]
                        weight = edge[1]
                        path.append(to)

                        if distances[to] > distances[index] + weight:
                            distances[to] = distances[index] + weight
                            parent[to] = index
                            any_change = True
                index += 1
            rotate_links_times += 1
            if not any_change:
                break

        if any_change:
            return {
                'path': Algorithm.PATH_NOT_FOUND,
                'steps': [],
                'isBellmanFord': 'True',
                'links': [],
                'currentLink': -1}

        if distances[target] == INF:
            return {
                'path': Algorithm.PATH_NOT_FOUND,
                'steps': [],
                'isBellmanFord': 'True',
                'links': [],
                'currentLink': -1}
        steps = []
        current_node = target
        while current_node != -1:
            steps.append(current_node)
            current_node = parent[current_node]

        return {
                'path': list(reversed(steps)),
                'steps': path,
                'isBellmanFord': 'True',
                'links': self.flatten([[[index, node_index[0]] for node_index in graph[index]]
                                      for index in range(len(graph))]) * rotate_links_times,
                'currentLink': 0
                }

    def flatten(self, list_of_lists):
        return [list2 for list1 in list_of_lists for list2 in list1]
