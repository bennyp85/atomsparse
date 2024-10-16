import unittest
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.properties import NodeType, PropertyOntology
from knowledge_graph.edges import Edge
from knowledge_graph.relationships import RelationshipType
from knowledge_graph.properties import PropertySchema, PropertyType
from reasoning.query import Query

class TestQuery(unittest.TestCase):

    def test_get_node_by_id(self):
        ontology = PropertyOntology()
        ontology.register_property(PropertySchema(name="age", data_type=PropertyType.INTEGER, description="Age of the entity"))
        graph = KnowledgeGraph()
        node1 = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=ontology)
        graph.add_node(node1)

        query = Query(graph)

        # Test retrieving an existing node
        retrieved_node = query.get_node_by_id("1")
        self.assertEqual(retrieved_node, node1)

        # Test retrieving a non-existent node
        retrieved_node = query.get_node_by_id("2")
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

        query = Query(graph)

        # Test retrieving nodes of type BOOK
        retrieved_nodes = query.get_nodes_by_type(NodeType.BOOK)
        self.assertEqual(len(retrieved_nodes), 2)
        self.assertIn(node1, retrieved_nodes)
        self.assertIn(node3, retrieved_nodes)

        # Test retrieving nodes of type CHARACTER
        retrieved_nodes = query.get_nodes_by_type(NodeType.CHARACTER)
        self.assertEqual(len(retrieved_nodes), 1)
        self.assertIn(node2, retrieved_nodes)

        # Test retrieving nodes of a non-existent type
        retrieved_nodes = query.get_nodes_by_type(NodeType.SETTING)
        self.assertEqual(len(retrieved_nodes), 0)

    def test_get_edges_by_relationship(self):
        ontology = PropertyOntology()
        graph = KnowledgeGraph()
        node1 = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=ontology)
        node2 = Node(node_id="2", node_type=NodeType.CHARACTER, property_ontology=ontology)
        graph.add_node(node1)
        graph.add_node(node2)
        edge1 = Edge(source_id="1", target_id="2", relationship=RelationshipType.INVOLVES, property_ontology=ontology)
        edge2 = Edge(source_id="2", target_id="1", relationship=RelationshipType.PART_OF, property_ontology=ontology)
        graph.add_edge(edge1)
        graph.add_edge(edge2)

        query = Query(graph)

        # Test retrieving edges with relationship INVOLVES
        retrieved_edges = query.get_edges_by_relationship(RelationshipType.INVOLVES)
        self.assertEqual(len(retrieved_edges), 1)
        self.assertIn(edge1, retrieved_edges)

        # Test retrieving edges with relationship PART_OF
        retrieved_edges = query.get_edges_by_relationship(RelationshipType.PART_OF)
        self.assertEqual(len(retrieved_edges), 1)
        self.assertIn(edge2, retrieved_edges)

        # Test retrieving edges with a non-existent relationship
        retrieved_edges = query.get_edges_by_relationship(RelationshipType.CAUSES)
        self.assertEqual(len(retrieved_edges), 0)

    def test_get_nodes_by_property_value(self):
        ontology = PropertyOntology()
        ontology.register_property(PropertySchema(name="age", data_type=PropertyType.INTEGER, description="Age of the entity"))
        graph = KnowledgeGraph()
        node1 = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=ontology, properties={"name": "1984"})
        node2 = Node(node_id="2", node_type=NodeType.CHARACTER, property_ontology=ontology, properties={"name": "Winston Smith", "age": 39})
        node3 = Node(node_id="3", node_type=NodeType.BOOK, property_ontology=ontology, properties={"name": "Animal Farm"})
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)

        query = Query(graph)

        # Test retrieving nodes with property "name" equal to "1984"
        retrieved_nodes = query.get_nodes_by_property_value("name", "1984")
        self.assertEqual(len(retrieved_nodes), 1)
        self.assertIn(node1, retrieved_nodes)

        # Test retrieving nodes with property "age" equal to 39
        retrieved_nodes = query.get_nodes_by_property_value("age", 39)
        self.assertEqual(len(retrieved_nodes), 1)
        self.assertIn(node2, retrieved_nodes)

        # Test retrieving nodes with a non-existent property
        retrieved_nodes = query.get_nodes_by_property_value("author", "George Orwell")
        self.assertEqual(len(retrieved_nodes), 0)

    def test_get_neighbor_nodes(self):
        ontology = PropertyOntology()
        graph = KnowledgeGraph()
        node1 = Node(node_id="1", node_type=NodeType.BOOK, property_ontology=ontology)
        node2 = Node(node_id="2", node_type=NodeType.CHARACTER, property_ontology=ontology)
        node3 = Node(node_id="3", node_type=NodeType.LOCATION, property_ontology=ontology)
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)
        edge1 = Edge(source_id="1", target_id="2", relationship=RelationshipType.INVOLVES, property_ontology=ontology)
        edge2 = Edge(source_id="2", target_id="3", relationship=RelationshipType.OCCURS_IN, property_ontology=ontology)
        graph.add_edge(edge1)
        graph.add_edge(edge2)

        query = Query(graph)

        # Test retrieving neighbors of node1 with relationship INVOLVES
        neighbors = query.get_neighbor_nodes("1", RelationshipType.INVOLVES)
        self.assertEqual(len(neighbors), 1)
        self.assertIn(node2, neighbors)

        # Test retrieving neighbors of node2 with relationship OCCURS_IN
        neighbors = query.get_neighbor_nodes("2", RelationshipType.OCCURS_IN)
        self.assertEqual(len(neighbors), 1)
        self.assertIn(node3, neighbors)

        # Test retrieving neighbors of node1 with a non-existent relationship
        neighbors = query.get_neighbor_nodes("1", RelationshipType.CAUSES)
        self.assertEqual(len(neighbors), 0)


if __name__ == '__main__':
    unittest.main()
