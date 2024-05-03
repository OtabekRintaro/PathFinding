from app.src.model.algorithms.algorithm import Algorithm
import heapq


INF = 10000000000
ARBITRARY_NUMBER = 10


class Dijkstra(Algorithm):
    def run(self, graph, source, target):
        if source is None or target is None:
            return {'path': Algorithm.PATH_NOT_FOUND, 'steps': []}
        graph = [[node if node[1] > 0 else [node[0], 0] for node in edges] for edges in graph]
        print(graph)
        path = []
        n = len(graph)
        d = [INF] * n
        p = [-1] * n
        print('d', d)
        print('p', p)
        if self.is_dense(graph):
            print("The graph is dense!")
            visited = [False] * n

            d[source] = 0
            for i in range(n):
                v = -1
                for j in range(n):
                    if not visited[j] and (v == -1 or d[j] < d[v]):
                        v = j

                if d[v] == INF:
                    break

                path.append(v)
                visited[v] = True
                for node in graph[v]:
                    to = node[0]
                    weight = node[1]

                    if d[v] + weight < d[to]:
                        d[to] = d[v] + weight
                        p[to] = v
        else:
            print("The graph is sparse!")
            d[source] = 0
            priority_queue = []
            heapq.heapify(priority_queue)
            heapq.heappush(priority_queue, (source, 0))

            while len(priority_queue) > 0:
                (current_node, current_weight) = heapq.heappop(priority_queue)
                print(current_node)

                if current_weight != d[current_node]:
                    continue

                path.append(current_node)
                for node in graph[current_node]:
                    to = node[0]
                    weight = node[1]

                    print(d[current_node] + weight < d[to])
                    if d[current_node] + weight < d[to]:
                        d[to] = d[current_node] + weight
                        p[to] = current_node
                        heapq.heappush(priority_queue, (to, d[to]))

        return {'path': self.get_path(p, source, target), 'steps': path}

    def get_path(self, p, source, target):
        path = []

        v = target
        while v != source and v != p[v]:
            path.append(v)
            v = p[v]
        if v != source:
            return []
        path.append(v)

        return [item for item in reversed(path)]

    def is_dense(self, graph):
        return len(graph) * len(graph) <= sum([sum([1 for _ in edge]) for edge in graph]) + ARBITRARY_NUMBER
