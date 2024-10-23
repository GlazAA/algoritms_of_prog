// Итеративный подход к DFS

class GraphIterative:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def _iterative_dfs(self, start, visited, stack):
        stack_dfs = [start]
        while stack_dfs:
            vertex = stack_dfs.pop()
            if vertex not in visited:
                visited.add(vertex)
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        stack_dfs.append(neighbor)
                stack.append(vertex)

    def _reverse_graph(self):
        reversed_graph = GraphIterative()
        for u in self.graph:
            for v in self.graph[u]:
                reversed_graph.add_edge(v, u)
        return reversed_graph

    def find_scc(self):
        stack = []
        visited = set()

        for vertex in self.graph:
            if vertex not in visited:
                self._iterative_dfs(vertex, visited, stack)

        reversed_graph = self._reverse_graph()
        visited.clear()
        sccs = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                component = []
                reversed_graph._iterative_dfs(vertex, visited, component)
                sccs.append(component)

        return sccs