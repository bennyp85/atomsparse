# tests/test_properties.py

import pytest
from knowledge_graph.properties import PropertyType, PropertySchema, PropertyOntology

class TestProperties:
    def test_property_type(self) -> None:
        assert PropertyType.STRING.value == "string"
        assert PropertyType.INTEGER.value == "integer"
        assert PropertyType.DATE.value == "date"
        assert PropertyType.BOOLEAN.value == "boolean"

    def test_property_schema(self) -> None:
        schema = PropertySchema("name", PropertyType.STRING, "The name of the entity")
        assert schema.name == "name"
        assert schema.type == PropertyType.STRING
        assert schema.description == "The name of the entity"

    def test_property_ontology(self) -> None:
        ontology = PropertyOntology()
        schema = PropertySchema("name", PropertyType.STRING, "The name of the entity")
        ontology.add_schema(schema)
        assert ontology.get_schema("name") == schema

    def test_validate_property(self) -> None:
        ontology = PropertyOntology()
        schema = PropertySchema("name", PropertyType.STRING, "The name of the entity")
        ontology.add_schema(schema)
        assert ontology.validate_property("name", "John Doe") == True
        assert ontology.validate_property("name", 123) == False

    def test_validate_property_invalid_type(self) -> None:
        ontology = PropertyOntology()
        schema = PropertySchema("age", PropertyType.INTEGER, "The age of the entity")
        ontology.add_schema(schema)
        assert ontology.validate_property("age", "thirty") == False

    def test_validate_property_missing_schema(self) -> None:
        ontology = PropertyOntology()
        assert ontology.validate_property("name", "John Doe") == False
