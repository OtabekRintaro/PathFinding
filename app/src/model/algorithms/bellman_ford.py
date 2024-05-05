from app.src.model.algorithms.algorithm import Algorithm, INF


class BellmanFord(Algorithm):

    def run(self, graph, source, target):
        if source is None or target is None:
            return {'path': Algorithm.PATH_NOT_FOUND, 'steps': []}
        path = []
        n = len(graph)
        distances = [INF] * n
        parent = [-1] * n

        distances[source] = 0

        while True:
            any_change = False

            index = 0
            for edges_of_node in graph:
                path.append(index)
                for edge in edges_of_node:
                    to = edge[0]
                    weight = edge[1]
                    path.append(to)

                    if distances[to] > distances[index] + weight:
                        distances[to] = distances[index] + weight
                        parent[to] = index
                        any_change = True
                index += 1

            if not any_change:
                break

        if distances[target] == INF:
            return {'path': Algorithm.PATH_NOT_FOUND, 'steps': []}
        steps = []
        current_node = target
        while current_node != -1:
            steps.append(current_node)
            current_node = parent[current_node]

        return {'path': path, 'steps': steps}
