# tests/test_graph.py
import unittest
from knowledge_graph.interface import KnowledgeGraphAPI

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.kg_api = KnowledgeGraphAPI()

    def test_add_node(self):
        self.kg_api.add_node("1", "Person")
        self.assertIn("1", self.kg_api.graph.graph.nodes)
        self.assertEqual(self.kg_api.graph.graph.nodes["1"]["type"], "Person")

    def test_add_edge(self):
        self.kg_api.add_node("1", "Person")
        self.kg_api.add_node("2", "Pet")
        self.kg_api.add_edge("1", "2", "owns")
        self.assertIn(("1", "2"), self.kg_api.graph.graph.edges)
        self.assertEqual(self.kg_api.graph.graph.edges["1", "2"]["relationship"], "owns")

    def test_query(self):
        self.kg_api.add_node("1", "Person")
        self.kg_api.add_node("2", "Pet")
        self.kg_api.add_edge("1", "2", "owns")
        results = self.kg_api.query("some_query")
        self.assertEqual(results["nodes"], [("1", {"type": "Person"}), ("2", {"type": "Pet"})])
        self.assertEqual(results["edges"], [("1", "2", {"relationship": "owns"})])

if __name__ == '__main__':
    unittest.main()