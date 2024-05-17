import time

from app.src.model.algorithms.algorithm import Algorithm, INF


class BellmanFord(Algorithm):

    desc = ("Bellman-Ford algorithm - an algorithm which computes the shortest path from the source node to all "
            "of the other nodes in a weighted graph. The graph traverses all of the edges of the graph and "
            "applies relaxations to them, further approximating the total cost of the path. With each step of "
            "the traversal, it minimizes the path cost and when it comes to the final step, it finds all of "
            "the shortest and minimal paths from the source node in the graph. Let N be a number of nodes and "
            "M be a number of edges, then the time complexity of the algorithm is O(N*M). It is optimal for the graphs "
            "with negative weighted edges and it always finds the correct solution except for the cases when "
            "there are negative cycles in the graph(the sum of the cycled path is negative).")

    def description(self):
        return BellmanFord.desc

    def run(self, graph, source, target):
        if source is None or target is None:
            return {
                'path': Algorithm.PATH_NOT_FOUND,
                'steps': [],
                'pathCost': 0,
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
                'pathCost': 0,
                'isBellmanFord': 'True',
                'links': [],
                'currentLink': -1}

        if distances[target] == INF:
            return {
                'path': Algorithm.PATH_NOT_FOUND,
                'steps': [],
                'pathCost': 0,
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
                'pathCost': distances[target],
                'isBellmanFord': 'True',
                'links': self._flatten([[[index, node_index[0]] for node_index in graph[index]]
                                       for index in range(len(graph))]) * rotate_links_times,
                'currentLink': 0
                }

    def _flatten(self, list_of_lists):
        return [list2 for list1 in list_of_lists for list2 in list1]
