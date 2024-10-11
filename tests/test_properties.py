import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from knowledge_graph.properties import PropertySchema, PropertyType, PropertyOntology

class TestPropertySchema(unittest.TestCase):
    def test_to_dict(self):
        schema = PropertySchema(name="Author", data_type=PropertyType.STRING, description="The author of the work.")
        expected_dict = {
            "name": "Author",
            "data_type": "string",
            "description": "The author of the work.",
            "required": False  # Add this line
        }
        self.assertEqual(schema.to_dict(), expected_dict)

class TestPropertyOntology(unittest.TestCase):
    
    def setUp(self):
        self.ontology = PropertyOntology()
        
    def test_register_property(self):
        schema = PropertySchema(name="Publisher", data_type=PropertyType.STRING, description="The publisher of the book.")
        self.ontology.register_property(schema)
        self.assertIn("Publisher", self.ontology.schemas)
        self.assertEqual(self.ontology.schemas["Publisher"].name, "Publisher")
        self.assertEqual(self.ontology.schemas["Publisher"].data_type, PropertyType.STRING)

    def test_register_multiple_properties(self):
        schema1 = PropertySchema(name="ISBN", data_type=PropertyType.STRING, description="The ISBN number of the book.")
        schema2 = PropertySchema(name="PageCount", data_type=PropertyType.INTEGER, description="The number of pages in the book.")
        self.ontology.register_property(schema1)
        self.ontology.register_property(schema2)
        self.assertEqual(len(self.ontology.schemas), 2)
        self.assertIn("ISBN", self.ontology.schemas)
        self.assertIn("PageCount", self.ontology.schemas)

if __name__ == '__main__':
    unittest.main()
