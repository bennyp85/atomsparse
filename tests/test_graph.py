# tests/test_graph.py
import unittest
from knowledge_graph.graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_node(self):
        self.graph.add_node("1", "Person")
        self.assertIn("1", self.graph.graph.nodes)
        self.assertEqual(self.graph.graph.nodes["1"]["type"], "Person")

    def test_add_edge(self):
        self.graph.add_node("1", "Person")
        self.graph.add_node("2", "Pet")
        self.graph.add_edge("1", "2", "owns")
        self.assertIn(("1", "2"), self.graph.graph.edges)
        self.assertEqual(self.graph.graph.edges["1", "2"]["relationship"], "owns")

if __name__ == '__main__':
    unittest.main()