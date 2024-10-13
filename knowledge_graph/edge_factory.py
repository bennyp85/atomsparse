from .edges import Edge
from .relationships import RelationshipType
from .properties import PropertyOntology
from typing import Dict, Any, Optional

class EdgeFactory:
    def __init__(self, property_ontology: PropertyOntology):
        self.property_ontology = property_ontology

    def create_edge(self, source_id: str, target_id: str, relationship: RelationshipType, properties: Optional[Dict[str, Any]] = None) -> Edge:
        return Edge(source_id, target_id, relationship, self.property_ontology, properties)
