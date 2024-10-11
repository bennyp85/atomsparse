# tests/test_edges.py

import unittest
from knowledge_graph.edges import Edge
from unittest.mock import Mock
from knowledge_graph.relationships import RelationshipType

class TestEdge(unittest.TestCase):
    def setUp(self):
        self.mock_property_ontology = Mock()
        self.mock_property_ontology.validate_property.return_value = True

    def test_edge_creation(self):
        edge = Edge("source_id", "target_id", RelationshipType.IS_A, self.mock_property_ontology)
        self.assertEqual(edge.source_id, "source_id")
        self.assertEqual(edge.target_id, "target_id")
        self.assertEqual(edge.relationship, RelationshipType.IS_A)
        self.assertEqual(edge.property_ontology, self.mock_property_ontology)
        self.assertEqual(edge.properties, {})
        self.mock_property_ontology.validate_property.assert_not_called()

    def test_edge_representation(self):
        edge = Edge("source_id", "target_id", RelationshipType.IS_A, self.mock_property_ontology)
        self.assertEqual(str(edge), "Edge(source=source_id, target=target_id, relationship=RelationshipType.IS_A, properties={})")

    def test_create_edge(self):
        edge = Edge.create_edge("source_id", "target_id", RelationshipType.IS_A, self.mock_property_ontology)
        self.assertEqual(edge.source_id, "source_id")
        self.assertEqual(edge.target_id, "target_id")
        self.assertEqual(edge.relationship, RelationshipType.IS_A)
        self.assertEqual(edge.property_ontology, self.mock_property_ontology)
        self.assertEqual(edge.properties, {})
        self.mock_property_ontology.validate_property.assert_not_called()

    def test_set_properties(self):
        edge = Edge("source_id", "target_id", RelationshipType.IS_A, self.mock_property_ontology)
        properties = {"name": "Alice", "age": 30}
        edge.set_properties(properties)
        self.assertEqual(edge.properties, properties)
        self.mock_property_ontology.validate_property.assert_called()

    def test_add_property(self):
        edge = Edge("source_id", "target_id", RelationshipType.IS_A, self.mock_property_ontology)
        edge.add_property("name", "Alice")
        self.assertEqual(edge.properties, {"name": "Alice"})
        self.mock_property_ontology.validate_property.assert_called_once_with("name", "Alice")

    def test_set_relationship(self):
        edge = Edge("source_id", "target_id", RelationshipType.IS_A, self.mock_property_ontology)
        edge.set_relationship(RelationshipType.PART_OF)
        self.assertEqual(edge.relationship, RelationshipType.PART_OF)

if __name__ == '__main__':
    unittest.main()