# tests/test_graph.py
import unittest
from knowledge_graph.graph import KnowledgeGraph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = KnowledgeGraph()

    def test_add_node(self):
        properties = {"name": "John Doe", "age": 30}
        self.graph.add_node("1", "Person", properties)
        self.assertIn("1", self.graph.graph.nodes)
        self.assertEqual(self.graph.graph.nodes["1"]["type"], "Person")
        self.assertEqual(self.graph.graph.nodes["1"]["properties"], properties)

    def test_add_edge(self):
        self.graph.add_node("1", "Person", {"name": "John Doe", "age": 30})
        self.graph.add_node("2", "Pet", {"name": "Rex", "species": "Dog"})
        self.graph.add_edge("1", "2", "owns")
        self.assertIn(("1", "2"), self.graph.graph.edges)
        self.assertEqual(self.graph.graph.edges["1", "2"]["relationship"], "owns")

    def test_get_node(self):
        properties = {"name": "John Doe", "age": 30}
        self.graph.add_node("1", "Person", properties)
        node = self.graph.get_nodes()
        self.assertEqual(node["1"]["type"], "Person")

        

if __name__ == '__main__':
    unittest.main()