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

if __name__ == '__main__':
    unittest.main()
