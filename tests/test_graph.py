# tests/test_graph.py
import unittest
from knowledge_graph.interface import KnowledgeGraphAPI

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.kg_api = KnowledgeGraphAPI()

    def test_add_node(self):
        properties = {"name": "John Doe", "age": 30}
        self.kg_api.add_node("1", "Person", properties)
        self.assertIn("1", self.kg_api.graph.graph.nodes)
        self.assertEqual(self.kg_api.graph.graph.nodes["1"]["type"], "Person")
        self.assertEqual(self.kg_api.graph.graph.nodes["1"]["properties"], properties)

    def test_add_edge(self):
        self.kg_api.add_node("1", "Person", {"name": "John Doe", "age": 30})
        self.kg_api.add_node("2", "Pet", {"name": "Rex", "species": "Dog"})
        self.kg_api.add_edge("1", "2", "owns")
        self.assertIn(("1", "2"), self.kg_api.graph.graph.edges)
        self.assertEqual(self.kg_api.graph.graph.edges["1", "2"]["relationship"], "owns")

    def test_query(self):
        properties_person = {"name": "John Doe", "age": 30}
        properties_pet = {"name": "Rex", "species": "Dog"}
        self.kg_api.add_node("1", "Person", properties_person)
        self.kg_api.add_node("2", "Pet", properties_pet)
        self.kg_api.add_edge("1", "2", "owns")
        results = self.kg_api.query("some_query")
        self.assertEqual(results["nodes"], [("1", {"type": "Person", "properties": properties_person}), ("2", {"type": "Pet", "properties": properties_pet})])
        self.assertEqual(results["edges"], [("1", "2", {"relationship": "owns"})])

if __name__ == '__main__':
    unittest.main()