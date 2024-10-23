import unittest
import random
from program import Graph, create_graph

class TestGraphSearch(unittest.TestCase):

    def test_search_existing_value(self):
        g = create_graph(1000)
        target = random.choice(g.values)
        result = g.search(target)
        self.assertNotEqual(result, -1)
        self.assertEqual(g.values[result], target)

    def test_search_non_existing_value(self):
        g = create_graph(1000)
        target = max(g.values) + 1 
        result = g.search(target)
        self.assertEqual(result, -1)

    def test_large_graph(self):
        g = create_graph(100000)
        target = random.choice(g.values)
        result = g.search(target)
        self.assertNotEqual(result, -1)
        self.assertEqual(g.values[result], target)

    def test_graph_structure(self):
        size = 100
        g = create_graph(size)
        self.assertEqual(len(g.values), size)
        for i in range(1, size):
            self.assertIn(i-1, g.graph[i])
            self.assertIn(i, g.graph[i-1])

    def test_multiple_searches(self):
        g = create_graph(10000)
        for _ in range(100):
            target = random.randint(1, 1000000)
            result = g.search(target)
            if result != -1:
                self.assertEqual(g.values[result], target)
            else:
                self.assertNotIn(target, g.values)

if __name__ == '__main__':
    unittest.main()