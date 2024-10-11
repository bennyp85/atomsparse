# tests/test_graph.py

import unittest
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge
from knowledge_graph.properties import NodeType, PropertyOntology, PropertySchema, PropertyType
from knowledge_graph.relationships import RelationshipType

class TestKnowledgeGraph(unittest.TestCase):
    def setUp(self):
        self.graph = KnowledgeGraph()
        self.property_ontology = PropertyOntology()
        self.property_ontology.register_property(PropertySchema("name", PropertyType.STRING, "Name of the node"))
        self.property_ontology.register_property(PropertySchema("importance", PropertyType.STRING, "Importance of the edge"))

    def test_add_node(self):
        node = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        self.graph.add_node(node)
        self.assertIn("1", self.graph.nodes)
        self.assertEqual(self.graph.nodes["1"], node)

    def test_add_duplicate_node(self):
        node = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        self.graph.add_node(node)
        with self.assertRaises(ValueError):
            self.graph.add_node(node)

    def test_add_edge(self):
        node1 = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        node2 = Node.create_node("2", NodeType.BOOK, self.property_ontology, {"name": "Book Title"})
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        edge = Edge.create_edge("1", "2", RelationshipType.USES, self.property_ontology)
        self.graph.add_edge(edge)
        self.assertIn(edge, self.graph.edges)

    def test_add_edge_with_nonexistent_nodes(self):
        edge = Edge.create_edge("1", "2", RelationshipType.USES, self.property_ontology)
        with self.assertRaises(ValueError):
            self.graph.add_edge(edge)

    def test_add_duplicate_edge(self):
        node1 = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        node2 = Node.create_node("2", NodeType.BOOK, self.property_ontology, {"name": "Book Title"})
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        edge = Edge.create_edge("1", "2", RelationshipType.USES, self.property_ontology)
        self.graph.add_edge(edge)
        with self.assertRaises(ValueError):
            self.graph.add_edge(edge)

    def test_delete_node(self):
        node1 = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        node2 = Node.create_node("2", NodeType.BOOK, self.property_ontology, {"name": "Book Title"})
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        edge = Edge.create_edge("1", "2", RelationshipType.USES, self.property_ontology)
        self.graph.add_edge(edge)
        self.graph.delete_node("1")
        self.assertNotIn("1", self.graph.nodes)
        self.assertNotIn(edge, self.graph.edges)

    def test_delete_nonexistent_node(self):
        with self.assertRaises(ValueError):
            self.graph.delete_node("nonexistent")

    def test_delete_edge(self):
        node1 = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        node2 = Node.create_node("2", NodeType.BOOK, self.property_ontology, {"name": "Book Title"})
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        edge = Edge.create_edge("1", "2", RelationshipType.USES, self.property_ontology)
        self.graph.add_edge(edge)
        self.graph.delete_edge("1", "2", RelationshipType.USES)
        self.assertNotIn(edge, self.graph.edges)

    def test_get_node(self):
        node = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        self.graph.add_node(node)
        retrieved_node = self.graph.get_node("1")
        self.assertEqual(retrieved_node, node)

    def test_get_nonexistent_node(self):
        self.assertIsNone(self.graph.get_node("nonexistent"))

    def test_get_edge(self):
        node1 = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        node2 = Node.create_node("2", NodeType.BOOK, self.property_ontology, {"name": "Book Title"})
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        edge = Edge.create_edge("1", "2", RelationshipType.USES, self.property_ontology)
        self.graph.add_edge(edge)
        retrieved_edge = self.graph.get_edge("1", "2", RelationshipType.USES)
        self.assertEqual(retrieved_edge, edge)

    def test_get_nonexistent_edge(self):
        self.assertIsNone(self.graph.get_edge("1", "2", RelationshipType.USES))

    def test_update_node(self):
        node = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        self.graph.add_node(node)
        self.graph.update_node("1", {"name": "Jane Doe"})
        self.assertEqual(self.graph.nodes["1"].properties["name"], "Jane Doe")

    def test_update_nonexistent_node(self):
        with self.assertRaises(ValueError):
            self.graph.update_node("nonexistent", {"name": "Jane Doe"})

    def test_update_edge(self):
        node1 = Node.create_node("1", NodeType.CHARACTER, self.property_ontology, {"name": "John Doe"})
        node2 = Node.create_node("2", NodeType.BOOK, self.property_ontology, {"name": "Book Title"})
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        edge = Edge.create_edge("1", "2", RelationshipType.USES, self.property_ontology)
        self.graph.add_edge(edge)
        self.graph.update_edge("1", "2", RelationshipType.USES, {"importance": "high"})
        self.assertEqual(self.graph.get_edge("1", "2", RelationshipType.USES).properties["importance"], "high")

    def test_update_nonexistent_edge(self):
        with self.assertRaises(ValueError):
            self.graph.update_edge("1", "2", RelationshipType.USES, {"importance": "high"})

if __name__ == '__main__':
    unittest.main()