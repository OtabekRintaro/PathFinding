from app.src.model.algorithms.algorithm import Algorithm
from app.src.model.data_structures.stack import Stack


class DFS(Algorithm):
    desc = ("DFS(Depth-First Search) - one of the most fundamental graph traversal/search algorithms. "
            "The algorithm starts from the source node and goes in depth of it until it starves "
            "out of possible edges to traverse and backtracks, to the previous nodes, to see if "
            "there had been any unvisited nodes or unused edges. Let N be a number of nodes(vertices) "
            "and M be a number of edges, then the time complexity of such algorithm takes O(N+M) time, "
            "to traverse entire graph(connected). The space complexity of the algorithm implemented "
            "by the usage of Stack is O(N). The DFS's purpose is not finding the shortest path to the target, "
            "but to find the first lexicographical one. So in order to find the shortest path, "
            "it is advised to use different algorithms.")

    def description(self):
        return DFS.desc

    def run(self, graph, source, target):
        if source is None or target is None:
            return {'path': Algorithm.PATH_NOT_FOUND, 'steps': []}
        print('DFS received graph', graph)
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
