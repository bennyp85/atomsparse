# file: /home/ben/atomsparse/tests/test_properties.py

import pytest
import networkx as nx
from knowledge_graph.properties import Property

class TestProperties:
    def setup_method(self):
        self.graph = nx.DiGraph()

    def test_property_valid(self):
        prop = Property("name", "John Doe", str)
        prop.validate()
        assert prop.value == "John Doe"

    def test_property_invalid(self):
        prop = Property("age", "30", int)
        with pytest.raises(TypeError, match="Value '30' of property 'age' is not of type <class 'int'>"):
            prop.validate()
