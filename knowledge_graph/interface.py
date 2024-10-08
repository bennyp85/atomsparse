# knowledge_graph/interface.py
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge

class KnowledgeGraphAPI:
    def __init__(self):
        self.graph = KnowledgeGraph()

    def add_node(self, node_id, node_type, properties=None):
        node = Node.create_node(node_id, node_type, properties)
        self.graph.add_node(node)

    def add_edge(self, source_id, target_id, relationship):
        edge = Edge.create_edge(source_id, target_id, relationship)
        self.graph.add_edge(edge)

    def delete_node(self, node_id):
        self.graph.delete_node(node_id)

    def get_graph(self):
        nodes, edges = self.graph.get_graph()
        if nodes is None or edges is None:
            raise ValueError("Failed to retrieve graph data")
        return nodes, edges
