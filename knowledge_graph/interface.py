# knowledge_graph/interface.py
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge
from knowledge_graph.properties import PropertyType

class KnowledgeGraphAPI:
    def __init__(self):
        self.graph = KnowledgeGraph()

    def add_node(self, node_id: str, node_type: str, properties=None):
        node = Node.create_node(node_id, node_type, self.graph.property_ontology, properties)
        self.graph.add_node(node)

    def add_edge(self, source_id: str, target_id: str, relationship: str, properties=None):
        edge = Edge.create_edge(source_id, target_id, relationship, self.graph.property_ontology, properties)
        self.graph.add_edge(edge)

    def delete_node(self, node_id: str):
        self.graph.delete_node(node_id)

    def get_graph(self):
        nodes, edges = self.graph.get_graph()
        if nodes is None or edges is None:
            raise ValueError("Failed to retrieve graph data")
        return nodes, edges

    def add_property_schema(self, name: str, property_type: PropertyType, description: str = ""):
        self.graph.add_property_schema(name, property_type, description)

    def get_property_schema(self, name: str):
        return self.graph.get_property_schema(name)

    def update_node_property(self, node_id: str, property_name: str, property_value):
        self.graph.update_node_property(node_id, property_name, property_value)

    def update_edge_property(self, source_id: str, target_id: str, property_name: str, property_value):
        self.graph.update_edge_property(source_id, target_id, property_name, property_value)

    def list_property_schemas(self):
        return self.graph.property_ontology.schemas
