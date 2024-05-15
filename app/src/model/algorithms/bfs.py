from app.src.model.algorithms.algorithm import Algorithm
from app.src.model.data_structures.queue import Queue


class BFS(Algorithm):

    desc = ("BFS(Breadth-First Search) - one of the most fundamental graph traversal/search algorithms. "
            "The algorithm starts from the source node and visits the neighbouring(nodes that are connected "
            "to the source with an edge) nodes until it exhausts itself out of the possible options to traverse."
            "Let N be a number of nodes(vertices) and M be a number of edges, then the time complexity of "
            "such algorithm takes O(N+M) time, to traverse entire graph(connected). The space complexity "
            "of the algorithm implemented by the usage of Queue is O(N). The implementation always finds the path "
            "if there exists one and stops, when it reaches its target. Additionally, it is guaranteed, that the path "
            "is going to be shortest(path consisting of the minimal amount of edges to traverse). "
            "When the graph contains no weights, this algorithm is optimal to find the shortest path.")

    def description(self):
        return BFS.desc

    def run(self, graph, source, target):
        if source is None or target is None:
            return {'path': Algorithm.PATH_NOT_FOUND, 'steps': []}
        path = []
        queue = Queue()
        print("Source and Target", source, target)
        queue.push((source, [source]))
        visited = [False] * (len(graph) + 1)

        while not queue.empty():
            (current_node, current_path) = queue.pop()
            print('current_node', current_node)
            if visited[current_node]:
                continue
            path.append(current_node)
            visited[current_node] = True
            print(current_node)
            if current_node == target:
                return {'path': current_path, 'steps': path}

            for node in sorted(graph[current_node]):
                print(current_node, ' nodes in loop ', node)
                if not visited[node[0]]:
                    queue.push((node[0], current_path + [node[0]]))

        return {'path': Algorithm.PATH_NOT_FOUND, 'steps': path}

