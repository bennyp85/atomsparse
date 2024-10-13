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

if __name__ == '__main__':
    unittest.main()
