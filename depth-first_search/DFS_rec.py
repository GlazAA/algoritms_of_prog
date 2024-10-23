// Рекурсивный DFS

class GraphRecursive:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack):
        visited.add(v)
        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                self._dfs(neighbor, visited, stack)
        stack.append(v)

    def _reverse_graph(self):
        reversed_graph = GraphRecursive()
        for u in self.graph:
            for v in self.graph[u]:
                reversed_graph.add_edge(v, u)
        return reversed_graph

    def find_scc(self):
        stack = []
        visited = set()

        for vertex in self.graph:
            if vertex not in visited:
                self._dfs(vertex, visited, stack)

        reversed_graph = self._reverse_graph()
        visited.clear()
        sccs = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                component = []
                reversed_graph._dfs(vertex, visited, component)
                sccs.append(component)

        return sccs