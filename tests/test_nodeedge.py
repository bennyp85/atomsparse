import unittest
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge

class TestNodeEdge(unittest.TestCase):
    def setUp(self):
        self.graph = KnowledgeGraph()

    def test_add_node_valid(self):
        properties = {"type": "Person", "name": "John Doe", "age": 30}
        Node.add_node(self.graph.graph, "1", properties)
        self.assertIn("1", self.graph.graph.nodes)
        self.assertEqual(self.graph.graph.nodes["1"]["type"], "Person")
        self.assertEqual(self.graph.graph.nodes["1"]["name"], "John Doe")
        self.assertEqual(self.graph.graph.nodes["1"]["age"], 30)

    def test_add_node_no_type(self):
        properties = {"name": "John Doe", "age": 30}
        with self.assertRaises(ValueError) as context:
            Node.add_node(self.graph.graph, "1", properties)
        self.assertTrue("Node must have a type." in str(context.exception))

    def test_add_edge_valid(self):
        Node.add_node(self.graph.graph, "1", {"type": "Person", "name": "John Doe", "age": 30})
        Node.add_node(self.graph.graph, "2", {"type": "Pet", "name": "Rex", "species": "Dog"})
        Edge.add_edge(self.graph.graph, "1", "2", "owns")
        self.assertIn(("1", "2"), self.graph.graph.edges)
        self.assertEqual(self.graph.graph.edges["1", "2"]["relationship"], "owns")

    def test_add_edge_invalid(self):
        Node.add_node(self.graph.graph, "1", {"type": "Person", "name": "John Doe", "age": 30})
        with self.assertRaises(ValueError) as context:
            Edge.add_edge(self.graph.graph, "1", "3", "owns")
        self.assertTrue("Source and target nodes must exist in the graph." in str(context.exception))

if __name__ == '__main__':
    unittest.main()