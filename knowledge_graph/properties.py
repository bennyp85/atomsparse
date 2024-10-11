from enum import Enum
from typing import Dict, List, Any

class NodeType(Enum):
    BOOK = "Book"
    CHARACTER = "Character"
    LITERARY_DEVICE = "LiteraryDevice"
    PLOT_POINT = "PlotPoint"
    SYMBOLISM = "Symbolism"
    MOTIF = "Motif"
    SETTING = "Setting"
    LOCATION = "Location"

class PropertyType(Enum):
    STRING = "string"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    LIST = "list"

class PropertySchema:
    def __init__(self, name: str, data_type: PropertyType, description: str = "", required: bool = False) -> None:
        self.name = name
        self.data_type = data_type
        self.description = description
        self.required = required
        
    def __repr__(self) -> str:
        return f"PropertySchema(name={self.name}, data_type={self.data_type.value}, description={self.description}, required={self.required})"
    
    def to_dict(self) -> Dict[str, Any]:
        """Return a dictionary representation of the property schema."""
        return {
            "name": self.name,
            "data_type": self.data_type.value,
            "description": self.description,
            "required": self.required
        }

class PropertyOntology:
    def __init__(self):
        self.schemas: Dict[str, PropertySchema] = {}
        self.required_properties: Dict[NodeType, List[str]] = {node_type: [] for node_type in NodeType}

    def register_property(self, property_schema: PropertySchema, node_types: List[NodeType] = None) -> None:
        """Register a new property schema."""
        self.schemas[property_schema.name] = property_schema
        if property_schema.required and node_types:
            for node_type in node_types:
                self.required_properties[node_type].append(property_schema.name)

    def validate_property(self, name: str, value: Any) -> bool:
        """Validate a property against its schema."""
        if name not in self.schemas:
            return False
        
        schema = self.schemas[name]
        if schema.data_type == PropertyType.STRING:
            return isinstance(value, str)
        elif schema.data_type == PropertyType.INTEGER:
            return isinstance(value, int)
        elif schema.data_type == PropertyType.BOOLEAN:
            return isinstance(value, bool)
        elif schema.data_type == PropertyType.LIST:
            return isinstance(value, list)
        return False

# Example usage
ontology = PropertyOntology()
schema = PropertySchema(name="Author", data_type=PropertyType.STRING, description="The author of the work.", required=True)
ontology.register_property(schema, [NodeType.BOOK])

print(ontology.schemas)
print(schema.to_dict())
print(ontology.required_properties)
