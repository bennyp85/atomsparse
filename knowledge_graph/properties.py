# knowledge_graph/properties.py

from enum import Enum
from typing import Dict, Any
from datetime import datetime

class PropertyType(Enum):
    STRING = "string"
    INTEGER = "integer"
    DATE = "date"
    BOOLEAN = "boolean"

class PropertySchema:
    """
    A class representing a property schema.
    
    Attributes:
    name (str): The name of the property.
    type (PropertyType): The type of the property.
    description (str): A description of the property.
    """
    def __init__(self, name: str, type: PropertyType, description: str = ""):
        self.name = name
        self.type = type
        self.description = description

    def __repr__(self):
        return f"PropertySchema(name={self.name}, type={self.type.value})"

class PropertyOntology:
    """
    A class representing an ontology of property schemas.
    
    Attributes:
    schemas (Dict[str, PropertySchema]): A dictionary mapping property names to their corresponding schemas.    
    """
    def __init__(self):
        self.schemas: Dict[str, PropertySchema] = {}

    def add_schema(self, schema: PropertySchema):
        """
        Add a property schema to the ontology.
        
        Args:
            schema (PropertySchema): The property schema to add.
            
        Raises:
            ValueError: If the property schema already exists in the ontology.
            
        Returns:
            None
        
        """
        if not schema.description:
            schema.description = self._get_default_description(schema.type)
        if not all([schema.name, schema.type, schema.description]):
            raise ValueError("Property schema name, type, and description must be provided")
        if schema.type not in PropertyType:
            raise ValueError(f"Invalid property type: {schema.type}")
        self.schemas[schema.name] = schema

    def _get_default_description(self, property_type: PropertyType) -> str:
        descriptions = {
            PropertyType.STRING: "A string property",
            PropertyType.INTEGER: "An integer property",
            PropertyType.DATE: "A date property",
            PropertyType.BOOLEAN: "A boolean property"
        }
        return descriptions.get(property_type, "")

    def get_schema(self, name: str) -> PropertySchema:
        return self.schemas.get(name)

    def validate_property(self, name: str, value: Any) -> bool:
        """
        Validate a property value against its schema.
        
        Args:
            name (str): The name of the property.
            value (Any): The value of the property.
            
        Returns:
            bool: True if the value is valid, False otherwise.
        
        """
        schema = self.get_schema(name)
        if schema is None:
            return False

        if schema.type == PropertyType.STRING:
            return isinstance(value, str)
        elif schema.type == PropertyType.INTEGER:
            return isinstance(value, int)
        elif schema.type == PropertyType.DATE:
            # Add date validation logic here
            try:
                datetime.strptime(value, '%Y-%m-%d')
                return True
            except ValueError:
                return False
        elif schema.type == PropertyType.BOOLEAN:
            return isinstance(value, bool)

        return False
