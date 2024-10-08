# tests/test_graph.py
import unittest
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = KnowledgeGraph()

    def test_add_node(self):
        properties = {"name": "John Doe", "age": 30}
        self.graph.add_node_by_attributes("1", "Person", properties)
        self.assertIn("1", self.graph.graph.nodes)
        self.assertEqual(self.graph.graph.nodes["1"]["type"], "Person")
        self.assertEqual(self.graph.graph.nodes["1"]["properties"], properties)

    def test_add_edge(self):
        self.graph.add_node_by_attributes("1", "Person", {"name": "John Doe", "age": 30})
        self.graph.add_node_by_attributes("2", "Pet", {"name": "Rex", "species": "Dog"})
        self.graph.add_edge(Edge("1", "2", "owns"))
        self.assertIn(("1", "2"), self.graph.graph.edges)
        self.assertEqual(self.graph.graph.edges["1", "2"]["relationship"], "owns")

    def test_get_node(self):
        properties = {"name": "John Doe", "age": 30}
        self.graph.add_node_by_attributes("1", "Person", properties)
        nodes = self.graph.get_nodes()
        self.assertEqual(nodes["1"]["type"], "Person")

        

if __name__ == '__main__':
    unittest.main()
