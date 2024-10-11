# knowledge_graph/graph.py

from typing import Dict, Any, Tuple
import networkx as nx
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge
from knowledge_graph.properties import PropertyOntology, PropertySchema, PropertyType

from typing import Dict, Any, Tuple, Optional
from knowledge_graph.relationships import RelationshipType
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

    def add_edge(self, source_id: str, target_id: str, relationship: RelationshipType, properties: Optional[Dict[str, any]] = None) -> None:
        if source_id not in self.graph or target_id not in self.graph:
            raise ValueError(f"Both nodes {source_id} and {target_id} must exist in the graph.")
        if self.graph.has_edge(source_id, target_id):
            raise ValueError(f"Edge from {source_id} to {target_id} already exists.")
        edge = Edge(source_id, target_id, relationship, self.property_ontology, properties)
        self.graph.add_edge(source_id, target_id, relationship=edge.relationship, properties=edge.properties)

    def add_character_uses_literary_device(self, character_id: str, device_id: str, properties: Optional[Dict[str, any]] = None) -> None:
        self.add_edge(character_id, device_id, RelationshipType.USES, properties)

    def add_character_participates_in_event(self, character_id: str, event_id: str, properties: Optional[Dict[str, any]] = None) -> None:
        self.add_edge(character_id, event_id, RelationshipType.PARTICIPATES_IN, properties)

    def add_event_occurs_in_setting(self, event_id: str, setting_id: str, properties: Optional[Dict[str, any]] = None) -> None:
        self.add_edge(event_id, setting_id, RelationshipType.OCCURS_IN, properties)

    def add_plot_point_involves_character(self, plot_point_id: str, character_id: str, properties: Optional[Dict[str, any]] = None) -> None:
        self.add_edge(plot_point_id, character_id, RelationshipType.INVOLVES, properties)

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
