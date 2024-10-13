# knowledge_graph/property_factory.py
from .properties import PropertyOntology
from typing import Dict, Any

class PropertyFactory:
    def __init__(self, property_ontology: PropertyOntology):
        self.property_ontology = property_ontology

    def create_property(self, property_name: str, property_value: Any) -> Dict[str, Any]:
        if not self.property_ontology.validate_property(property_name, property_value):
            raise ValueError(f"Invalid property value for {property_name}: {property_value}")
        return {property_name: property_value}
    
    