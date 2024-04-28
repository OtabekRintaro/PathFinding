from app.src.model.algorithms.algorithm import Algorithm
from app.src.model.data_structures.Stack import Stack


class DFS(Algorithm):

    def run(self, graph, source, target):
        if source is None or target is None:
            return {'path': Algorithm.PATH_NOT_FOUND, 'steps': []}
        path = []
        stack = Stack()
        stack.push((source, [source]))
        visited = [False] * len(graph)

        while not stack.empty():
            (current_node, current_path) = stack.pop()
            path.append(current_node)
            visited[current_node] = True
            print(current_node)
            if current_node == target:
                return {'path': current_path, 'steps': path}

            for node in graph[current_node]:
                if not visited[node]:
                    stack.push((node, current_path + [node]))

        return {'path': Algorithm.PATH_NOT_FOUND, 'steps': path}

