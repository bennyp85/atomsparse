import unittest
from knowledge_graph.nodes import Node
from knowledge_graph.properties import NodeType, PropertyOntology, PropertySchema, PropertyType

class TestNode(unittest.TestCase):
    def setUp(self):
        self.ontology = PropertyOntology()
        self.ontology.register_property(PropertySchema(name="name", data_type=PropertyType.STRING, description="Name of the node"))

    def test_node_creation(self):
        node = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=self.ontology, properties={"name": "1984"})
        self.assertEqual(node.node_id, "1")
        self.assertEqual(node.node_type, NodeType.BOOK)
        self.assertEqual(node.properties["name"], "1984")

    def test_set_properties(self):
        node = Node(node_id="2", node_type=NodeType.CHARACTER, property_ontology=self.ontology)
        node.set_properties({"name": "Winston Smith"})
        self.assertEqual(node.properties["name"], "Winston Smith")

    def test_invalid_property(self):
        node = Node(node_id="3", node_type=NodeType.BOOK, property_ontology=self.ontology)
        with self.assertRaises(ValueError):
            node.set_properties({"invalid_property": "value"})

if __name__ == '__main__':
    unittest.main()
