# tests/test_nodeedge.py

import pytest
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge

class TestNodeEdge:
    def setup_method(self):
        self.graph = KnowledgeGraph()

    def test_add_node_valid(self):
        properties = {"name": "John Doe", "age": 30}
        self.graph.add_node_by_attributes("1", "Person", properties)
        nodes = self.graph.get_nodes()
        assert nodes["1"]["type"] == "Person"
        assert nodes["1"]["properties"] == properties

    def test_add_node_no_type(self):
        properties = {"name": "John Doe", "age": 30}
        with pytest.raises(ValueError):
            self.graph.add_node_by_attributes("1", "", properties)

    def test_add_edge_valid(self):
        self.graph.add_node_by_attributes("1", "Person")
        self.graph.add_node_by_attributes("2", "Person")
        self.graph.add_edge(Edge("1", "2", "knows"))
        edges = self.graph.get_edges()
        assert edges["1"]["2"]["relationship"] == "knows"

    def test_add_edge_invalid(self):
        with pytest.raises(ValueError):
            self.graph.add_edge(Edge("1", "2", "knows"))
