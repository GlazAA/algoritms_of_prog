// функция 

import time
import random

def benchmark(graph_class, num_vertices, num_edges):
    graph = graph_class()
    
    for _ in range(num_edges):
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        graph.add_edge(u, v)

    start_time = time.time()
    sccs = graph.find_scc()
    end_time = time.time()

    return end_time - start_time, len(sccs)

num_vertices = 1000
num_edges = 5000

time_recursive, scc_count_recursive = benchmark(GraphRecursive, num_vertices, num_edges)
time_iterative, scc_count_iterative = benchmark(GraphIterative, num_vertices, num_edges)

print(f"Рек версия: t = {time_recursive:.5f} сек, компонент связности = {scc_count_recursive}")
print(f"Итер версия: t = {time_iterative:.5f} сек, компонент связности = {scc_count_iterative}")