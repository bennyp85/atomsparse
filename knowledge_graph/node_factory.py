# knowledge_graph/node_factory.py
from .nodes import Node
from .properties import NodeType, PropertyOntology
from .property_factory import PropertyFactory
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

"""
class EdgeFactory:
    def __init__(self, property_ontology: PropertyOntology):
        self.property_ontology = property_ontology

    def create_edge(self, source_id: str, target_id: str, relationship: RelationshipType, properties: Optional[Dict[str, Any]] = None) -> Edge:
        if relationship not in RelationshipType.__members__.values():
            raise ValueError(f"Invalid relationship type: {relationship}")

        validated_properties = {}
        if properties:
            for prop_name, prop_value in properties.items():
                if prop_name not in self.property_ontology.schemas:
                    raise ValueError(f"Invalid property name: {prop_name}")
                prop_schema = self.property_ontology.schemas[prop_name]
                validate_func = VALIDATION_FUNCTIONS[prop_schema.data_type]
                if not validate_func(prop_value):
                    raise ValueError(f"Invalid property type for {prop_name}: expected {prop_schema.data_type}, got {type(prop_value)}")
                validated_properties[prop_name] = prop_value

        return Edge(source_id, target_id, relationship, self.property_ontology, validated_properties)

class Node:
    def __init__(self, node_id: str, node_type: NodeType, property_ontology: PropertyOntology, properties: Optional[Dict[str, Any]] = None) -> None:
    self.node_id = node_id
    self.node_type = node_type
    self.property_ontology = property_ontology
    self.properties = {'type': node_type.value}
    if properties:
        self.set_properties(properties) 
            
        
"""

class NodeFactory:
    def __init__(self, property_ontology: PropertyOntology):
        self.property_factory = PropertyFactory(property_ontology)

    def create_node(self, node_id: str, node_type: NodeType, properties: Optional[Dict[str, Any]] = None) -> Node:
        node = Node(node_id, node_type, self.property_factory.property_ontology, properties)
        return node