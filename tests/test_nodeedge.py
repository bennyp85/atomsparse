# tests/test_nodeedge.py

import pytest
import networkx as nx
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge

class TestNodeEdge:
    def setup_method(self):
        self.graph = nx.DiGraph()

    def test_add_node_valid(self):
        properties = {"name": "John Doe", "age": 30}
        Node.add_node(self.graph, "1", "Person", properties)
        assert self.graph.nodes["1"]["type"] == "Person"
        assert self.graph.nodes["1"]["properties"] == properties

    def test_add_node_no_type(self):
        properties = {"name": "John Doe", "age": 30}
        with pytest.raises(ValueError, match="Node type must be specified"):
            Node.add_node(self.graph, "1", None, properties)

    def test_add_edge_valid(self):
        Node.add_node(self.graph, "1", "Person")
        Node.add_node(self.graph, "2", "Person")
        Edge.add_edge(self.graph, "1", "2", "knows")
        assert self.graph.edges["1", "2"]["relationship"] == "knows"

    def test_add_edge_invalid(self):
        with pytest.raises(KeyError):
            Edge.add_edge(self.graph, "1", "2", "knows")