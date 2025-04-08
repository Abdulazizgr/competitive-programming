class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]

        def dfs(node, current_color):
            color[node] = current_color

            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if current_color == 0:
                        next_color = 1
                    else:
                        next_color = 0

                    if not dfs(neighbor, next_color):
                        return False
                elif color[neighbor] == current_color:
                    return False

            return True

        for i in range(len(graph)):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False

        return True
