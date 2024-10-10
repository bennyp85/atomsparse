# knowledge_graph/graph.py

from typing import Dict, Any, Tuple
import networkx as nx
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge
from knowledge_graph.properties import PropertyOntology, PropertySchema, PropertyType

class KnowledgeGraph:
    def __init__(self):
        self.graph: nx.DiGraph = nx.DiGraph()
        self.property_ontology = PropertyOntology()

    def add_node(self, node: Node) -> None:
        if node.node_id in self.graph:
            raise ValueError(f"Node {node.node_id} already exists.")
        self.graph.add_node(node.node_id, type=node.node_type, properties=node.properties)

    def add_node_by_attributes(self, node_id: str, node_type: str, properties: Dict[str, Any] = None) -> None:
        if node_id in self.graph:
            raise ValueError(f"Node {node_id} already exists.")
        if not node_type:
            raise ValueError("Node type must be specified")
        node = Node.create_node(node_id, node_type, self.property_ontology, properties)
        self.add_node(node)

    def add_edge(self, edge: Edge) -> None:
        if edge.source_id not in self.graph or edge.target_id not in self.graph:
            raise ValueError(f"Both nodes {edge.source_id} and {edge.target_id} must exist in the graph.")
        if self.graph.has_edge(edge.source_id, edge.target_id):
            raise ValueError(f"Edge from {edge.source_id} to {edge.target_id} already exists.")
        self.graph.add_edge(edge.source_id, edge.target_id, relationship=edge.relationship, properties=edge.properties)

    def delete_node(self, node_id: str) -> None:
        if node_id not in self.graph:
            raise KeyError(f"Node {node_id} does not exist.")
        self.graph.remove_node(node_id)

    def get_nodes(self) -> Dict[str, Dict[str, Any]]:
        return {node: data for node, data in self.graph.nodes(data=True)}

    def get_edges(self) -> Dict[str, Dict[str, Dict[str, Any]]]:
        edges: Dict[str, Dict[str, Dict[str, Any]]] = {}
        for source, target, data in self.graph.edges(data=True):
            if source not in edges:
                edges[source] = {}
            edges[source][target] = data
        return edges

    def get_graph(self) -> Tuple[Dict[str, Dict[str, Any]], Dict[str, Dict[str, Dict[str, Any]]]]:
        nodes = self.get_nodes()
        edges = self.get_edges()
        return nodes, edges

    def add_property_schema(self, name: str, property_type: PropertyType, description: str = "") -> None:
        schema = PropertySchema(name, property_type, description)
        self.property_ontology.add_schema(schema)

    def get_property_schema(self, name: str) -> PropertySchema:
        return self.property_ontology.get_schema(name)

    def update_node_property(self, node_id: str, property_name: str, property_value: Any) -> None:
        if node_id not in self.graph:
            raise KeyError(f"Node {node_id} does not exist.")
        if not self.property_ontology.validate_property(property_name, property_value):
            raise ValueError(f"Invalid property: {property_name}")
        self.graph.nodes[node_id]['properties'][property_name] = property_value

    def update_edge_property(self, source_id: str, target_id: str, property_name: str, property_value: Any) -> None:
        if not self.graph.has_edge(source_id, target_id):
            raise ValueError(f"Edge from {source_id} to {target_id} does not exist.")
        if not self.property_ontology.validate_property(property_name, property_value):
            raise ValueError(f"Invalid property: {property_name}")
        self.graph[source_id][target_id]['properties'][property_name] = property_value
