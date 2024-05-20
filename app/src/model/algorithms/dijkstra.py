from app.src.model.algorithms.algorithm import Algorithm, INF, ARBITRARY_NUMBER
import heapq


class Dijkstra(Algorithm):

    desc = ("Dijkstra algorithm - is an algorithm that finds the shortest path in the graph from the given source node "
            "to all of the other nodes. It uses abstract data structure such as min-priority queue, to find "
            "the shortest paths, from one node to the other. Let N be a number of the nodes in the graph, then the "
            "time complexity of the algorithm will be O(N*N). The algorithm is the best fit for the graphs with "
            "non-negative weighted edges for finding the shortest and minimal path from the source to the target node."
            "Modifications: All of the negative edges in the graph are treated as 0 by the algorithm, "
            "so it is not guaranteed that it will give the correct path for the graphs containing the "
            "negative weights.")

    def description(self):
        return Dijkstra.desc

    def run(self, graph, source, target):
        if source is None or target is None:
            return {'path': Algorithm.PATH_NOT_FOUND, 'steps': [], 'pathCost': 0}
        graph = [[node if node[1] > 0 else [node[0], 0] for node in edges] for edges in graph]
        print(graph)
        path = []
        n = len(graph)
        distances = [INF] * n
        parent = [-1] * n
        print('d', distances)
        print('p', parent)
        if self.is_dense(graph):
            print("The graph is dense!")
            visited = [False] * n

            distances[source] = 0
            for i in range(n):
                v = -1
                for j in range(n):
                    if not visited[j] and (v == -1 or distances[j] < distances[v]):
                        v = j

                if distances[v] == INF:
                    break

                path.append(v)
                visited[v] = True
                for node in graph[v]:
                    to = node[0]
                    weight = node[1]

                    if distances[v] + weight < distances[to]:
                        distances[to] = distances[v] + weight
                        parent[to] = v
        else:
            print("The graph is sparse!")
            distances[source] = 0
            priority_queue = []
            heapq.heapify(priority_queue)
            heapq.heappush(priority_queue, (0, source))

            while len(priority_queue) > 0:
                (current_weight, current_node) = heapq.heappop(priority_queue)
                print(current_node)

                if current_weight != distances[current_node]:
                    continue

                path.append(current_node)
                for node in graph[current_node]:
                    to = node[0]
                    weight = node[1]

                    print(distances[current_node] + weight < distances[to])
                    if distances[current_node] + weight < distances[to]:
                        distances[to] = distances[current_node] + weight
                        parent[to] = current_node
                        heapq.heappush(priority_queue, (distances[to], to))

        path_from_source_to_target = self.get_path(parent, source, target)
        if not path_from_source_to_target:
            return {'path': Algorithm.PATH_NOT_FOUND, 'steps': [], 'pathCost': 0}
        return {'path': path_from_source_to_target, 'steps': path, 'pathCost': distances[target]}

    def get_path(self, p, source, target):
        path = []

        v = target
        while v != source and v != p[v] and v != -1:
            path.append(v)
            v = p[v]
        print('the path', path)
        if v != source:
            return []
        path.append(v)

        return [item for item in reversed(path)]

    def is_dense(self, graph):
        return len(graph) * len(graph) <= sum([sum([1 for _ in edge]) for edge in graph]) + ARBITRARY_NUMBER
