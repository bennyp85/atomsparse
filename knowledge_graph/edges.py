# knowledge_graph/edges.py
from typing import Optional, Dict
from .properties import PropertyOntology
from .relationships import RelationshipType

class Edge:
    def __init__(self, source_id: str, target_id: str, relationship: RelationshipType, property_ontology: PropertyOntology, properties: Optional[Dict[str, any]] = None) -> None:
        if not isinstance(relationship, RelationshipType):
            raise ValueError(f"Invalid relationship type: {relationship}")
        self.source_id: str = source_id
        self.target_id: str = target_id
        self.relationship: RelationshipType = relationship
        self.property_ontology = property_ontology
        self.properties: Dict[str, any] = {}
        if properties:
            self.set_properties(properties)


    def set_properties(self, properties: Dict[str, any]) -> None:
        for name, value in properties.items():
            if not self.property_ontology.validate_property(name, value):
                raise ValueError(f"Invalid property: {name}")
            self.properties[name] = value
            self.property_ontology.validate_property(name, value)

    def add_property(self, name: str, value: any) -> None:
        if not self.property_ontology.validate_property(name, value):
            raise ValueError(f"Invalid property: {name}")
        self.properties[name] = value

    def set_relationship(self, relationship: RelationshipType) -> None:
        if not isinstance(relationship, RelationshipType):
            raise ValueError(f"Invalid relationship type: {relationship}")
        self.relationship = relationship

    def __repr__(self) -> str:
        return f"Edge(source={self.source_id}, target={self.target_id}, relationship={self.relationship}, properties={self.properties})"
