# tests/test_graph.py

import unittest
from knowledge_graph.graph_builder import GraphBuilder
from knowledge_graph.properties import NodeType, PropertyOntology, PropertySchema, PropertyType
from knowledge_graph.relationships import RelationshipType

class TestKnowledgeGraph(unittest.TestCase):
    def setUp(self):
        self.builder = GraphBuilder()
        self.builder.add_property("name", PropertyType.STRING, "Name of the node")
        self.builder.add_property("importance", PropertyType.STRING, "Importance of the edge")

    def test_add_node(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        graph = self.builder.build()
        self.assertIn("1", graph.nodes)
        self.assertEqual(graph.nodes["1"].properties["name"], "John Doe")

    def test_add_duplicate_node(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        graph = self.builder.build()
        with self.assertRaises(ValueError):
            self.graph.add_node(node)

    def test_add_edge(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        self.builder.add_node("2", NodeType.BOOK, {"name": "Book Title"})
        self.builder.add_edge("1", "2", RelationshipType.USES)
        graph = self.builder.build()
        self.assertTrue(any(e.source_id == "1" and e.target_id == "2" and e.relationship == RelationshipType.USES for e in graph.edges))

    def test_add_edge_with_nonexistent_nodes(self):
        self.builder.add_edge("1", "2", RelationshipType.USES)
        with self.assertRaises(ValueError):
            self.builder.build()

    def test_add_duplicate_edge(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        self.builder.add_node("2", NodeType.BOOK, {"name": "Book Title"})
        self.builder.add_edge("1", "2", RelationshipType.USES)
        graph = self.builder.build()
        with self.assertRaises(ValueError):
            graph.add_edge(graph.get_edge("1", "2", RelationshipType.USES))

    def test_delete_node(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        self.builder.add_node("2", NodeType.BOOK, {"name": "Book Title"})
        self.builder.add_edge("1", "2", RelationshipType.USES)
        graph = self.builder.build()
        graph.delete_node("1")
        self.assertNotIn("1", graph.nodes)
        self.assertTrue(all(e.source_id != "1" and e.target_id != "1" for e in graph.edges))

    def test_delete_nonexistent_node(self):
        with self.assertRaises(ValueError):
            self.graph.delete_node("nonexistent")

    def test_delete_edge(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        self.builder.add_node("2", NodeType.BOOK, {"name": "Book Title"})
        self.builder.add_edge("1", "2", RelationshipType.USES)
        graph = self.builder.build()
        graph.delete_edge("1", "2", RelationshipType.USES)
        self.assertIsNone(graph.get_edge("1", "2", RelationshipType.USES))

    def test_get_node(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        graph = self.builder.build()
        retrieved_node = graph.get_node("1")
        self.assertEqual(retrieved_node.properties["name"], "John Doe")

    def test_get_nonexistent_node(self):
        self.assertIsNone(self.graph.get_node("nonexistent"))

    def test_get_edge(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        self.builder.add_node("2", NodeType.BOOK, {"name": "Book Title"})
        self.builder.add_edge("1", "2", RelationshipType.USES)
        graph = self.builder.build()
        retrieved_edge = graph.get_edge("1", "2", RelationshipType.USES)
        self.assertEqual(retrieved_edge.source_id, "1")
        self.assertEqual(retrieved_edge.target_id, "2")
        self.assertEqual(retrieved_edge.relationship, RelationshipType.USES)

    def test_get_nonexistent_edge(self):
        self.assertIsNone(self.graph.get_edge("1", "2", RelationshipType.USES))

    def test_update_node(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        graph = self.builder.build()
        graph.update_node("1", {"name": "Jane Doe"})
        self.assertEqual(graph.nodes["1"].properties["name"], "Jane Doe")

    def test_update_nonexistent_node(self):
        with self.assertRaises(ValueError):
            self.graph.update_node("nonexistent", {"name": "Jane Doe"})

    def test_update_edge(self):
        self.builder.add_node("1", NodeType.CHARACTER, {"name": "John Doe"})
        self.builder.add_node("2", NodeType.BOOK, {"name": "Book Title"})
        self.builder.add_edge("1", "2", RelationshipType.USES)
        graph = self.builder.build()
        graph.update_edge("1", "2", RelationshipType.USES, {"importance": "high"})
        self.assertEqual(graph.get_edge("1", "2", RelationshipType.USES).properties["importance"], "high")

    def test_update_nonexistent_edge(self):
        with self.assertRaises(ValueError):
            self.graph.update_edge("1", "2", RelationshipType.USES, {"importance": "high"})

if __name__ == '__main__':
    unittest.main()
