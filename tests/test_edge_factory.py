import unittest
from knowledge_graph.edge_factory import EdgeFactory
from knowledge_graph.edges import Edge
from knowledge_graph.properties import PropertyOntology, PropertySchema, PropertyType
from knowledge_graph.relationships import RelationshipType

class TestEdgeFactory(unittest.TestCase):
    def setUp(self):
        self.ontology = PropertyOntology()
        self.ontology.register_property(PropertySchema(name="weight", data_type=PropertyType.INTEGER, description="Weight of the edge"))
        self.factory = EdgeFactory(self.ontology)

    def test_create_edge(self):
        edge = self.factory.create_edge(source_id="1", target_id="2", relationship=RelationshipType.IS_A, properties={"weight": 5})
        self.assertIsInstance(edge, Edge)
        self.assertEqual(edge.source_id, "1")
        self.assertEqual(edge.target_id, "2")
        self.assertEqual(edge.relationship, RelationshipType.IS_A)
        self.assertEqual(edge.properties["weight"], 5)

    def test_create_edge_with_invalid_property(self):
        with self.assertRaises(ValueError):
            self.factory.create_edge(source_id="1", target_id="2", relationship=RelationshipType.CAUSES, properties={"invalid_property": "value"})

if __name__ == '__main__':
    unittest.main()
