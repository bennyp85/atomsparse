# knowledge_graph/edges.py
from typing import Optional, Dict
from .properties import PropertyOntology

class Edge:
    def __init__(self, source_id: str, target_id: str, relationship: str, property_ontology: PropertyOntology, properties: Optional[Dict[str, any]] = None) -> None:
        self.source_id: str = source_id
        self.target_id: str = target_id
        self.relationship: str = relationship
        self.property_ontology = property_ontology
        self.properties: Dict[str, any] = {}
        if properties:
            self.set_properties(properties)

    @staticmethod
    def create_edge(source_id: str, target_id: str, relationship: str, property_ontology: PropertyOntology, properties: Optional[Dict[str, any]] = None) -> 'Edge':
        if not source_id or not target_id or not relationship:
            raise ValueError("source_id, target_id, and relationship are required")
        return Edge(source_id, target_id, relationship, property_ontology, properties)

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
        return f"Edge(source={self.source_id}, target={self.target_id}, relationship={self.relationship}, properties={self.properties})"
