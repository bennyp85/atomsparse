# file: /home/ben/atomsparse/tests/test_properties.py

import pytest
import networkx as nx
from knowledge_graph.properties import Property

class TestProperties:
    def setup_method(self):
        self.graph = nx.DiGraph()

    def test_property_valid(self):
        prop = Property("name", "Alice", str)
        assert prop.value == "Alice"
        assert prop.data_type == str
        assert prop._convert_value("Alice") == "Alice"
        prop.validate()

    def test_property_invalid(self):
        prop = Property("age", 30, int)  # Use an integer instead of a string
        with pytest.raises(TypeError, match="Property 'age' must be of type 'int'"):
            prop.value = "30"  # Assign an invalid type to raise TypeError
            prop.validate()

    def test_property_float_invalid(self):
        prop = Property("height", 5.9, float)  # Use a float instead of a string
        with pytest.raises(TypeError, match="Property 'height' must be of type 'float'"):
            prop.value = "5.9"  # Assign an invalid type to raise TypeError
            prop.validate()

    def test_property_bool_invalid(self):
        prop = Property("is_active", True, bool)  # Use a boolean instead of a string
        with pytest.raises(TypeError, match="Property 'is_active' must be of type 'bool'"):
            prop.value = "True"  # Assign an invalid type to raise TypeError
            prop.validate()
