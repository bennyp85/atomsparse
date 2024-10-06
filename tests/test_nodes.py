import pytest
from knowledge_graph.nodes import Node
from knowledge_graph.properties import Property

# /home/ben/atomsparse/tests/test_nodes.py


class MockGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id, **attrs):
        self.nodes[node_id] = attrs

def test_node_initialization():
    node = Node(node_id="1", properties=[Property("name", "value", str)])
    assert node.node_id == "1"
    assert len(node.properties) == 1
    assert node.properties[0].name == "name"
    assert node.properties[0].value == "value"

def test_add_node_with_valid_properties():
    graph = MockGraph()
    properties = {"name": "value"}
    Node.add_node(graph, node_id="1", node_type="type", properties=properties)
    assert "1" in graph.nodes
    assert graph.nodes["1"]["node_type"] == "type"
    assert len(graph.nodes["1"]["properties"]) == 1
    assert graph.nodes["1"]["properties"][0].name == "name"
    assert graph.nodes["1"]["properties"][0].value == "value"

def test_add_node_without_node_type():
    graph = MockGraph()
    with pytest.raises(ValueError, match="Node type must be specified"):
        Node.add_node(graph, node_id="1", node_type=None)

def test_add_node_with_invalid_properties_type():
    graph = MockGraph()
    with pytest.raises(TypeError, match="Properties must be a list of Property instances"):
        Node.add_node(graph, node_id="1", node_type="type", properties="invalid")

def test_add_node_with_invalid_property_instance():
    graph = MockGraph()
    with pytest.raises(TypeError, match="All properties must be instances of the Property class"):
        Node.add_node(graph, node_id="1", node_type="type", properties=["invalid"])

def test_node_repr():
    node = Node(node_id="1", properties=[Property("name", "value", str)])
    assert repr(node) == "Node(id=1, properties=[Property(name=name, value=value, data_type=<class 'str'>)])"

