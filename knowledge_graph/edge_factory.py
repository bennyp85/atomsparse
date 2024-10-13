from .edges import Edge
from .relationships import RelationshipType
from .properties import PropertyOntology
from typing import Dict, Any, Optional

"""
class NodeType(Enum):
    BOOK = "Book"
    CHARACTER = "Character"
    LITERARY_DEVICE = "LiteraryDevice"
    PLOT_POINT = "PlotPoint"
    SYMBOLISM = "Symbolism"
    MOTIF = "Motif"
    SETTING = "Setting"
    LOCATION = "Location"


class RelationshipType(Enum):
    IS_A = "is_a"
    PART_OF = "part_of"
    CAUSES = "causes"
    USES = "uses"
    PARTICIPATES_IN = "participates_in"
    OCCURS_IN = "occurs_in"
    INVOLVES = "involves"
    
"""

class EdgeFactory:
    def __init__(self, property_ontology: PropertyOntology):
        self.property_ontology = property_ontology

    def create_edge(self, source_id: str, target_id: str, relationship: RelationshipType, properties: Optional[Dict[str, Any]] = None) -> Edge:
        if relationship == RelationshipType.IS_A:
            return Edge(source_id, target_id, relationship, self.property_ontology, properties)
        elif relationship == RelationshipType.PART_OF:
            return Edge(source_id, target_id, relationship, self.property_ontology, properties)
        elif relationship == RelationshipType.CAUSES:
            return Edge(source_id, target_id, relationship, self.property_ontology, properties)
        elif relationship == RelationshipType.USES:
            return Edge(source_id, target_id, relationship, self.property_ontology, properties)
        elif relationship == RelationshipType.PARTICIPATES_IN:
            return Edge(source_id, target_id, relationship, self.property_ontology, properties)
        elif relationship == RelationshipType.OCCURS_IN:
            return Edge(source_id, target_id, relationship, self.property_ontology, properties)
        elif relationship == RelationshipType.INVOLVES:
            return Edge(source_id, target_id, relationship, self.property_ontology, properties)
        else:
            raise ValueError(f"Invalid relationship type: {relationship}")
