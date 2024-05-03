from app.src.model.algorithms.algorithm import Algorithm
from app.src.model.data_structures.queue import Queue


class BFS(Algorithm):

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

