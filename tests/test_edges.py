# tests/test_edges.py
import unittest
from knowledge_graph.edges import Edge
from knowledge_graph.properties import PropertyOntology, PropertySchema, PropertyType
from knowledge_graph.relationships import RelationshipType

class TestEdge(unittest.TestCase):
    def setUp(self):
        self.ontology = PropertyOntology()
        self.ontology.register_property(PropertySchema(name="weight", data_type=PropertyType.INTEGER, description="Weight of the edge"))

    def test_edge_creation(self):
        edge = Edge(source_id="1", target_id="2", relationship=RelationshipType.IS_A, property_ontology=self.ontology, properties={"weight": 5})
        self.assertEqual(edge.source_id, "1")
        self.assertEqual(edge.target_id, "2")
        self.assertEqual(edge.relationship, RelationshipType.IS_A)
        self.assertEqual(edge.properties["weight"], 5)

    def test_set_properties(self):
        edge = Edge(source_id="1", target_id="2", relationship=RelationshipType.PART_OF, property_ontology=self.ontology)
        edge.set_properties({"weight": 10})
        self.assertEqual(edge.properties["weight"], 10)

    def test_invalid_property(self):
        edge = Edge(source_id="1", target_id="2", relationship=RelationshipType.CAUSES, property_ontology=self.ontology)
        with self.assertRaises(ValueError):
            edge.set_properties({"invalid_property": "value"})

if __name__ == '__main__':
    unittest.main()
