# tests/test_edges.py

import unittest
from unittest.mock import MagicMock
from knowledge_graph.graph_builder import GraphBuilder
from knowledge_graph.properties import NodeType, PropertyType
from knowledge_graph.relationships import RelationshipType
from knowledge_graph.edge_factory import EdgeFactory

class TestEdge(unittest.TestCase):
    def setUp(self):
        self.property_ontology = PropertyOntology()
        self.property_ontology.register_property(PropertySchema("name", PropertyType.STRING, "Name of the node"))
        self.property_ontology.register_property(PropertySchema("age", PropertyType.INTEGER, "Age of the edge"))
        self.builder = GraphBuilder()
        self.builder.property_ontology = self.property_ontology

    def test_edge_creation(self):
        self.builder.add_node("source_id", NodeType.CHARACTER, {"name": "Source"})
        self.builder.add_node("target_id", NodeType.BOOK, {"name": "Target"})
        self.builder.add_edge("source_id", "target_id", RelationshipType.IS_A)
        graph = self.builder.build()
        edge = graph.get_edge("source_id", "target_id", RelationshipType.IS_A)
        self.assertEqual(edge.source_id, "source_id")
        self.assertEqual(edge.target_id, "target_id")
        self.assertEqual(edge.relationship, RelationshipType.IS_A)
        self.assertEqual(edge.properties, {})
        self.mock_property_ontology.validate_property.assert_not_called()

    def test_edge_representation(self):
        self.builder.add_node("source_id", NodeType.CHARACTER, {"name": "Source"})
        self.builder.add_node("target_id", NodeType.BOOK, {"name": "Target"})
        self.builder.add_edge("source_id", "target_id", RelationshipType.IS_A)
        graph = self.builder.build()
        edge = graph.get_edge("source_id", "target_id", RelationshipType.IS_A)
        self.assertEqual(str(edge), "Edge(source=source_id, target=target_id, relationship=RelationshipType.IS_A, properties={})")

    def test_create_edge(self):
        factory = EdgeFactory(self.mock_property_ontology)
        edge = factory.create_edge("source_id", "target_id", RelationshipType.IS_A)
        self.assertEqual(edge.source_id, "source_id")
        self.assertEqual(edge.target_id, "target_id")
        self.assertEqual(edge.relationship, RelationshipType.IS_A)
        self.assertEqual(edge.property_ontology, self.mock_property_ontology)
        self.assertEqual(edge.properties, {})
        self.mock_property_ontology.validate_property.assert_not_called()

    def test_set_properties(self):
        self.builder.add_node("source_id", NodeType.CHARACTER, {"name": "Source"})
        self.builder.add_node("target_id", NodeType.BOOK, {"name": "Target"})
        self.builder.add_edge("source_id", "target_id", RelationshipType.IS_A, {"name": "Alice", "age": 30})
        graph = self.builder.build()
        edge = graph.get_edge("source_id", "target_id", RelationshipType.IS_A)
        self.assertEqual(edge.properties, {"name": "Alice", "age": 30})
        self.mock_property_ontology.validate_property.assert_called()

    def test_add_property(self):
        self.builder.add_node("source_id", NodeType.CHARACTER, {"name": "Source"})
        self.builder.add_node("target_id", NodeType.BOOK, {"name": "Target"})
        self.builder.add_edge("source_id", "target_id", RelationshipType.IS_A, {"name": "Alice", "age": 30})
        graph = self.builder.build()
        edge = graph.get_edge("source_id", "target_id", RelationshipType.IS_A)
        self.assertEqual(edge.properties, {"name": "Alice", "age": 30})
        self.mock_property_ontology.validate_property.assert_called_once_with("name", "Alice")

    def test_set_relationship(self):
        self.builder.add_node("source_id", NodeType.CHARACTER, {"name": "Source"})
        self.builder.add_node("target_id", NodeType.BOOK, {"name": "Target"})
        self.builder.add_edge("source_id", "target_id", RelationshipType.IS_A)
        graph = self.builder.build()
        edge = graph.get_edge("source_id", "target_id", RelationshipType.IS_A)
        edge.set_relationship(RelationshipType.PART_OF)
        self.assertEqual(edge.relationship, RelationshipType.PART_OF)

if __name__ == '__main__':
    unittest.main()
