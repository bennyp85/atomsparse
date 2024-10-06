import pytest
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.edges import Edge
from knowledge_graph.nodes import Node
from knowledge_graph.properties import Property

def test_add_edge():
    graph = KnowledgeGraph()
    node1 = Node(node_id="1", properties=[Property("name", "Node1", str)])
    node2 = Node(node_id="2", properties=[Property("name", "Node2", str)])
    
    Node.add_node(graph, node1.node_id, "Type1", node1.properties)
    Node.add_node(graph, node2.node_id, "Type2", node2.properties)
    
    Edge.add_edge(graph.graph, node1.node_id, node2.node_id, "related_to")
    
    assert graph.graph.has_edge(node1.node_id, node2.node_id)
    assert graph.graph[node1.node_id][node2.node_id]["relationship"] == "related_to"

def test_add_invalid_edge():
    graph = KnowledgeGraph()
    node1 = Node(node_id="1", properties=[Property("name", "Node1", str)])
    node2 = Node(node_id="2", properties=[Property("name", "Node2", str)])
    
    Node.add_node(graph, node1.node_id, "Type1", node1.properties)
    
    with pytest.raises(KeyError, match="One or both nodes do not exist in the graph"):
        Edge.add_edge(graph.graph, node1.node_id, node2.node_id, "related_to")