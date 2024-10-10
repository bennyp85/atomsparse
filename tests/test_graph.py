# tests/test_graph.py
import unittest
from typing import Dict, Any
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge
from knowledge_graph.properties import PropertyType

class TestGraph(unittest.TestCase):
    def setUp(self) -> None:
        self.graph: KnowledgeGraph = KnowledgeGraph()
        self.graph.add_property_schema("name", PropertyType.STRING, "Name of the entity")
        self.graph.add_property_schema("age", PropertyType.INTEGER, "Age of the person")
        self.graph.add_property_schema("species", PropertyType.STRING, "Species of the pet")

    def test_add_node(self) -> None:
        properties: Dict[str, Any] = {"name": "John Doe", "age": 30}
        self.graph.add_node_by_attributes("1", "Person", properties)
        self.assertIn("1", self.graph.graph.nodes)
        self.assertEqual(self.graph.graph.nodes["1"]["type"], "Person")
        self.assertEqual(self.graph.graph.nodes["1"]["properties"], properties)

    def test_add_edge(self) -> None:
        self.graph.add_node_by_attributes("1", "Person", {"name": "John Doe", "age": 30})
        self.graph.add_node_by_attributes("2", "Pet", {"name": "Rex", "species": "Dog"})
        edge = Edge.create_edge("1", "2", "owns", self.graph.property_ontology)
        self.graph.add_edge(edge)
        self.assertIn(("1", "2"), self.graph.graph.edges)
        self.assertEqual(self.graph.graph.edges["1", "2"]["relationship"], "owns")

    def test_get_node(self) -> None:
        properties: Dict[str, Any] = {"name": "John Doe", "age": 30}
        self.graph.add_node_by_attributes("1", "Person", properties)
        nodes = self.graph.get_nodes()
        self.assertEqual(nodes["1"]["type"], "Person")
        self.assertEqual(nodes["1"]["properties"], properties)

    def test_property_validation(self) -> None:
        # Valid properties
        self.graph.add_node_by_attributes("1", "Person", {"name": "John Doe", "age": 30})
        
        # Invalid property type
        with self.assertRaises(ValueError):
            self.graph.add_node_by_attributes("2", "Person", {"name": "Jane Doe", "age": "thirty"})

        # Unknown property
        with self.assertRaises(ValueError):
            self.graph.add_node_by_attributes("3", "Person", {"name": "Bob", "height": 180})

    def test_update_node_property(self) -> None:
        self.graph.add_node_by_attributes("1", "Person", {"name": "John Doe", "age": 30})
        self.graph.update_node_property("1", "age", 31)
        nodes = self.graph.get_nodes()
        self.assertEqual(nodes["1"]["properties"]["age"], 31)

        # Invalid property update
        with self.assertRaises(ValueError):
            self.graph.update_node_property("1", "age", "thirty-one")

    def test_update_edge_property(self) -> None:
        self.graph.add_property_schema("since", PropertyType.INTEGER, "Year of ownership")
        self.graph.add_node_by_attributes("1", "Person", {"name": "John Doe", "age": 30})
        self.graph.add_node_by_attributes("2", "Pet", {"name": "Rex", "species": "Dog"})
        edge = Edge.create_edge("1", "2", "owns", self.graph.property_ontology, {"since": 2020})
        self.graph.add_edge(edge)
        
        self.graph.update_edge_property("1", "2", "since", 2021)
        edges = self.graph.get_edges()
        self.assertEqual(edges["1"]["2"]["properties"]["since"], 2021)

        # Invalid property update
        with self.assertRaises(ValueError):
            self.graph.update_edge_property("1", "2", "since", "last year")

    def test_get_property_schema(self) -> None:
        schema = self.graph.get_property_schema("name")
        self.assertEqual(schema.name, "name")
        self.assertEqual(schema.type, PropertyType.STRING)
        self.assertEqual(schema.description, "Name of the entity")

if __name__ == '__main__':
    unittest.main()
