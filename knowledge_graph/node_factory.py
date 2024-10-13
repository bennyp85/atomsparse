from .nodes import Node
from .properties import NodeType, PropertyOntology
from typing import Dict, Any, Optional

class NodeFactory:
    def __init__(self, property_ontology: PropertyOntology):
        self.property_ontology = property_ontology

    def create_node(self, node_id: str, node_type: NodeType, properties: Optional[Dict[str, Any]] = None) -> Node:
        return Node(node_id, node_type, self.property_ontology, properties)
