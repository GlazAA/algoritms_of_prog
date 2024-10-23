class Graph:
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
        reversed_graph = Graph()
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


def test_strongly_connected_components():
    g1 = Graph()
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(3, 1)
    g1.add_edge(3, 4)
    g1.add_edge(4, 5)
    g1.add_edge(5, 4)

    print("Test Case 1 SCCs:", g1.find_scc()) 

    g2 = Graph()
    g2.add_edge('A', 'B')
    g2.add_edge('B', 'C')
    g2.add_edge('C', 'A')
    g2.add_edge('B', 'D')
    g2.add_edge('D', 'E')
    g2.add_edge('E', 'F')
    g2.add_edge('F', 'E')

    print("Test Case 2 SCCs:", g2.find_scc())  
    g3 = Graph()
    g3.add_edge('A', 'B')
    g3.add_edge('B', 'C')
    g3.add_edge('C', 'D')
    g3.add_edge('D', 'E')

    print("Test Case 3 SCCs:", g3.find_scc())  

    g4 = Graph()
    g4.add_edge('1', '2')
    g4.add_edge('2', '3')
    g4.add_edge('3', '1')
    g4.add_edge('3', '4')
    g4.add_edge('4', '5')
    g4.add_edge('5', '4')
    g4.add_edge('6', '7')
    g4.add_edge('7', '8')
    g4.add_edge('8', '6')

    print("Test Case 4 SCCs:", g4.find_scc())  


if __name__ == "__main__":
    test_strongly_connected_components()
