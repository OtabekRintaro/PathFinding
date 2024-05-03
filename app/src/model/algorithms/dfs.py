from app.src.model.algorithms.algorithm import Algorithm
from app.src.model.data_structures.stack import Stack


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

            if target in [node[0] for node in graph[current_node]]:
                return {'path': current_path + [target], 'steps': path + [target]}
            for node in sorted(graph[current_node], reverse=True):
                if not visited[node[0]]:
                    stack.push((node[0], current_path + [node[0]]))

        return {'path': Algorithm.PATH_NOT_FOUND, 'steps': path}

