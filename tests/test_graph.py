import unittest
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge
from knowledge_graph.properties import NodeType, PropertyOntology, PropertySchema, PropertyType
from knowledge_graph.relationships import RelationshipType

class TestKnowledgeGraph(unittest.TestCase):
    def setUp(self):
        self.ontology = PropertyOntology()
        self.ontology.register_property(PropertySchema(name="name", data_type=PropertyType.STRING, description="Name of the node"))
        self.graph = KnowledgeGraph()

    def test_add_node(self):
        node = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=self.ontology, properties={"name": "1984"})
        self.graph.add_node(node)
        self.assertIn("1", self.graph.nodes)

    def test_add_edge(self):
        node1 = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=self.ontology, properties={"name": "1984"})
        node2 = Node(node_id="2", node_type=NodeType.CHARACTER, property_ontology=self.ontology, properties={"name": "Winston Smith"})
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        edge = Edge(source_id="1", target_id="2", relationship=RelationshipType.INVOLVES, property_ontology=self.ontology)
        self.graph.add_edge(edge)
        self.assertIn(edge, self.graph.edges)

    def test_delete_node(self):
        node = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=self.ontology, properties={"name": "1984"})
        self.graph.add_node(node)
        self.graph.delete_node("1")
        self.assertNotIn("1", self.graph.nodes)

    def test_delete_edge(self):
        node1 = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=self.ontology, properties={"name": "1984"})
        node2 = Node(node_id="2", node_type=NodeType.CHARACTER, property_ontology=self.ontology, properties={"name": "Winston Smith"})
        self.graph.add_node(node1)
        self.graph.add_node(node2)
        edge = Edge(source_id="1", target_id="2", relationship=RelationshipType.INVOLVES, property_ontology=self.ontology)
        self.graph.add_edge(edge)
        self.graph.delete_edge("1", "2", RelationshipType.INVOLVES)
        self.assertNotIn(edge, self.graph.edges)

if __name__ == '__main__':
    unittest.main()
