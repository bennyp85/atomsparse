import unittest
from knowledge_graph.property_factory import PropertyFactory
from knowledge_graph.properties import PropertyOntology, PropertySchema, PropertyType

class TestPropertyFactory(unittest.TestCase):
    def setUp(self):
        self.ontology = PropertyOntology()
        self.ontology.register_property(PropertySchema(name="name", data_type=PropertyType.STRING, description="Name of the entity"))
        self.ontology.register_property(PropertySchema(name="age", data_type=PropertyType.INTEGER, description="Age of the entity"))
        self.factory = PropertyFactory(self.ontology)

    def test_create_valid_property(self):
        prop = self.factory.create_property("name", "1984")
        self.assertEqual(prop, {"name": "1984"})

    def test_create_invalid_property(self):
        with self.assertRaises(ValueError):
            self.factory.create_property("invalid_property", "value")

    def test_create_property_with_wrong_type(self):
        with self.assertRaises(ValueError):
            self.factory.create_property("age", "not_an_integer")

    def test_create_property_with_missing_property(self):
        with self.assertRaises(ValueError):
            self.factory.create_property("missing_property", 5)

if __name__ == '__main__':
    unittest.main()