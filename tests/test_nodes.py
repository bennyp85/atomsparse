import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from knowledge_graph.nodes import Node
from knowledge_graph.properties import NodeType, PropertyOntology, PropertyType, PropertySchema

class TestNode(unittest.TestCase):
    def setUp(self):
        self.property_ontology = PropertyOntology()
        self.property_ontology.register_property(PropertySchema("name", PropertyType.STRING, "Name of the node"))
        self.property_ontology.register_property(PropertySchema("age", PropertyType.INTEGER, "Age of the person"))

    def test_create_node(self):
        node = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe", "age": 30})
        self.assertEqual(node.node_id, "1")
        self.assertEqual(node.node_type, NodeType.CHARACTER)
        self.assertEqual(node.properties["type"], "Character")
        self.assertEqual(node.properties["name"], "John Doe")
        self.assertEqual(node.properties["age"], 30)

    def test_create_node_without_properties(self):
        node = Node.create_node("2", NodeType.BOOK, self.property_ontology)
        self.assertEqual(node.node_id, "2")
        self.assertEqual(node.node_type, NodeType.BOOK)
        self.assertEqual(node.properties, {"type": "Book"})

    def test_create_node_with_invalid_property(self):
        with self.assertRaises(ValueError):
            Node.create_node("3", NodeType.CHARACTER, self.property_ontology, {"invalid_prop": "value"})

    def test_node_representation(self):
        node = Node.create_node("4", NodeType.LOCATION, self.property_ontology, {"name": "New York"})
        expected_repr = "Node(id=4, type=Location, properties={'type': 'Location', 'name': 'New York'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == '__main__':
    unittest.main()
