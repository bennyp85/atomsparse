import unittest
from knowledge_graph.properties import PropertySchema, PropertyType, PropertyOntology, NodeType

class TestPropertySchema(unittest.TestCase):
    def test_property_schema_creation(self):
        schema = PropertySchema(name="title", data_type=PropertyType.STRING, description="Title of the book", required=True)
        self.assertEqual(schema.name, "title")
        self.assertEqual(schema.data_type, PropertyType.STRING)
        self.assertEqual(schema.description, "Title of the book")
        self.assertTrue(schema.required)

    def test_property_schema_to_dict(self):
        schema = PropertySchema(name="title", data_type=PropertyType.STRING, description="Title of the book", required=True)
        schema_dict = schema.to_dict()
        self.assertEqual(schema_dict["name"], "title")
        self.assertEqual(schema_dict["data_type"], "string")
        self.assertEqual(schema_dict["description"], "Title of the book")
        self.assertTrue(schema_dict["required"])

class TestPropertyOntology(unittest.TestCase):
    def setUp(self):
        self.ontology = PropertyOntology()

    def test_register_property(self):
        schema = PropertySchema(name="author", data_type=PropertyType.STRING, description="Author of the book")
        self.ontology.register_property(schema)
        self.assertIn("author", self.ontology.schemas)

    def test_validate_property(self):
        schema = PropertySchema(name="pages", data_type=PropertyType.INTEGER, description="Number of pages")
        self.ontology.register_property(schema)
        self.assertTrue(self.ontology.validate_property("pages", 300))
        self.assertFalse(self.ontology.validate_property("pages", "three hundred"))

if __name__ == '__main__':
    unittest.main()
