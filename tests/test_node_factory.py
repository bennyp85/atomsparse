import unittest
from knowledge_graph.node_factory import NodeFactory
from knowledge_graph.nodes import Node
from knowledge_graph.properties import NodeType, PropertyOntology, PropertySchema, PropertyType

class TestNodeFactory(unittest.TestCase):
    def setUp(self):
        self.ontology = PropertyOntology()
        self.ontology.register_property(PropertySchema(name="name", data_type=PropertyType.STRING, description="Name of the node"))
        self.factory = NodeFactory(self.ontology)

    def test_create_node(self):
        node = self.factory.create_node(node_id="1", node_type=NodeType.BOOK, properties={"name": "1984"})
        self.assertIsInstance(node, Node)
        self.assertEqual(node.node_id, "1")
        self.assertEqual(node.node_type, NodeType.BOOK)
        self.assertEqual(node.properties["name"], "1984")

    def test_create_node_with_invalid_property(self):
        with self.assertRaises(ValueError):
            self.factory.create_node(node_id="2", node_type=NodeType.CHARACTER, properties={"invalid_property": "value"})

    def test_create_node_with_missing_property(self):
        with self.assertRaises(ValueError):
            self.factory.create_node(node_id="3", node_type=NodeType.PLOT_POINT, properties={"missing_property": "value"})

    def test_create_node_with_multiple_properties(self):
        self.ontology.register_property(PropertySchema(name="age", data_type=PropertyType.INTEGER, description="Age of the character"))
        node = self.factory.create_node(node_id="4", node_type=NodeType.CHARACTER, properties={"name": "Winston", "age": 39})
        self.assertIsInstance(node, Node)
        self.assertEqual(node.node_id, "4")
        self.assertEqual(node.node_type, NodeType.CHARACTER)
        self.assertEqual(node.properties["name"], "Winston")
        self.assertEqual(node.properties["age"], 39)

if __name__ == '__main__':
    unittest.main()