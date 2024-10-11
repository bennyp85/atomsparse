# knowledge_graph/nodes.py
from typing import Dict, Optional
from enum import Enum
from .properties import PropertyOntology, PropertySchema

class NodeType(Enum):
    BOOK = "Book"
    CHARACTER = "Character"
    LITERARY_DEVICE = "LiteraryDevice"
    PLOT_POINT = "PlotPoint"
    SYMBOLISM = "Symbolism"
    MOTIF = "Motif"
    SETTING = "Setting"
    LOCATION = "Location"

class Node:
    def __init__(self, node_id: str, node_type: NodeType, property_ontology: PropertyOntology, properties: Optional[Dict[str, any]] = None) -> None:
        self.node_id = node_id
        self.node_type = node_type
        self.property_ontology = property_ontology
        self.properties = {'type': node_type.value}
        if properties:
            self.set_properties(properties)

    @staticmethod
    def create_node(node_id: str, node_type: NodeType, property_ontology: PropertyOntology, properties: Optional[Dict[str, any]] = None) -> 'Node':
        if not node_id or not node_type:
            raise ValueError("node_id and node_type are required")
        return Node(node_id, node_type, property_ontology, properties)

    def set_properties(self, properties: Dict[str, any]) -> None:
        for name, value in properties.items():
            if not self.property_ontology.validate_property(name, value):
                raise ValueError(f"Invalid property: {name}")
            self.properties[name] = value

    def add_property(self, name: str, value: any) -> None:
        if not self.property_ontology.validate_property(name, value):
            raise ValueError(f"Invalid property: {name}")
        self.properties[name] = value

    def __repr__(self) -> str:
        return f"Node(id={self.node_id}, type={self.node_type.value}, properties={self.properties})"
