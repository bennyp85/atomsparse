# knowledge_graph/edge_factory.py
from knowledge_graph.edges import Edge
from knowledge_graph.properties import PropertyOntology, PropertyType
from knowledge_graph.relationships import RelationshipType
from typing import Optional, Dict, Any

def validate_string(value: Any) -> bool:
    return isinstance(value, str)

def validate_integer(value: Any) -> bool:
    return isinstance(value, int)

def validate_boolean(value: Any) -> bool:
    return isinstance(value, bool)

def validate_list(value: Any) -> bool:
    return isinstance(value, list)

VALIDATION_FUNCTIONS = {
    PropertyType.STRING: validate_string,
    PropertyType.INTEGER: validate_integer,
    PropertyType.BOOLEAN: validate_boolean,
    PropertyType.LIST: validate_list,
}

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