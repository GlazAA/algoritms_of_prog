import random

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.values = []

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def add_value(self, value):
        self.values.append(value)

    def search(self, target):
        visited = [False] * self.V
        return self._dfs_search(0, target, visited)

    def _dfs_search(self, v, target, visited):
        visited[v] = True
        if self.values[v] == target:
            return v

        for i in self.graph[v]:
            if not visited[i]:
                result = self._dfs_search(i, target, visited)
                if result != -1:
                    return result

        return -1

def create_graph(size):
    g = Graph(size)
    for i in range(size):
        value = random.randint(1, 1000000)
        g.add_value(value)
        if i > 0:
            g.add_edge(i, i-1)
    return g

if __name__ == "__main__":
    long = int(input("Введите длину массива: "))
    g = create_graph(long)

    find_num = int(input("Введите число для поиска: "))
    resalt = g.search(find_num)

    if resalt != -1:
        print(f"Число {find_num} найдено по индексу {resalt}")
    else:
        print("Такого числа нет")
        print("Все числа в массиве:")
        print(g.values)
		
		
/*
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
long = int(input("Введите длину массива: "))

arr = [random.randint(1, 100) for _ in range(long)]
find_num = int(input("Введите число для поиска: "))

resalt = linear_search(arr, find_num)

if resalt != -1:
    print(f"Число {find_num} найдено по индексу {resalt}")
else:
    print("Такого числа нет")
    print("Все числа в arrе:")
    print(arr)
	*/