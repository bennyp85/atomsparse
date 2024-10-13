from .nodes import Node
from .properties import NodeType, PropertyOntology
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

class NodeFactory:
    def __init__(self, property_ontology: PropertyOntology):
        self.property_ontology = property_ontology

    def create_node(self, node_id: str, node_type: NodeType, properties: Optional[Dict[str, Any]] = None) -> Node:
        if node_type == NodeType.BOOK:
            return Node(node_id, node_type, self.property_ontology, properties)
        elif node_type == NodeType.CHARACTER:
            return Node(node_id, node_type, self.property_ontology, properties)
        elif node_type == NodeType.LITERARY_DEVICE:
            return Node(node_id, node_type, self.property_ontology, properties)
        elif node_type == NodeType.PLOT_POINT:
            return Node(node_id, node_type, self.property_ontology, properties)
        elif node_type == NodeType.SYMBOLISM:
            return Node(node_id, node_type, self.property_ontology, properties)
        elif node_type == NodeType.MOTIF:
            return Node(node_id, node_type, self.property_ontology, properties)
        elif node_type == NodeType.SETTING:
            return Node(node_id, node_type, self.property_ontology, properties)
        elif node_type == NodeType.LOCATION:
            return Node(node_id, node_type, self.property_ontology, properties)
        else:
            raise ValueError(f"Invalid node type: {node_type}")