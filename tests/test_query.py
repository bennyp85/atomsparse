import unittest
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.properties import NodeType, PropertyOntology
from reasoning.query import get_node_by_id

class TestQuery(unittest.TestCase):

    def test_get_node_by_id(self):
        ontology = PropertyOntology()
        graph = KnowledgeGraph()
        node1 = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=ontology)
        graph.add_node(node1)

        # Test retrieving an existing node
        retrieved_node = get_node_by_id(graph, "1")
        self.assertEqual(retrieved_node, node1)

        # Test retrieving a non-existent node
        retrieved_node = get_node_by_id(graph, "2")
        self.assertIsNone(retrieved_node)

    def test_get_nodes_by_type(self):
        ontology = PropertyOntology()
        graph = KnowledgeGraph()
        node1 = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=ontology)
        node2 = Node(node_id="2", node_type=NodeType.CHARACTER, property_ontology=ontology)
        node3 = Node(node_id="3", node_type=NodeType.BOOK, property_ontology=ontology)
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)

        # Test retrieving nodes of type BOOK
        retrieved_nodes = get_nodes_by_type(graph, NodeType.BOOK)
        self.assertEqual(len(retrieved_nodes), 2)
        self.assertIn(node1, retrieved_nodes)
        self.assertIn(node3, retrieved_nodes)

        # Test retrieving nodes of type CHARACTER
        retrieved_nodes = get_nodes_by_type(graph, NodeType.CHARACTER)
        self.assertEqual(len(retrieved_nodes), 1)
        self.assertIn(node2, retrieved_nodes)

        # Test retrieving nodes of a non-existent type
        retrieved_nodes = get_nodes_by_type(graph, NodeType.SETTING)
        self.assertEqual(len(retrieved_nodes), 0)


if __name__ == '__main__':
    unittest.main()
