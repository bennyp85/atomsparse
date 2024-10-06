# knowledge_graph/interface.py
from knowledge_graph.graph import KnowledgeGraph

class KnowledgeGraphAPI:
    def __init__(self):
        self.graph = KnowledgeGraph()

    def add_node(self, node_id, node_type, properties=None):
        if not node_id or not node_type:
            raise ValueError("node_id and node_type are required")
        self.graph.add_node(node_id, node_type, properties)

    def add_edge(self, source_id, target_id, relationship):
        if not source_id or not target_id or not relationship:
            raise ValueError("source_id, target_id, and relationship are required")
        self.graph.add_edge(source_id, target_id, relationship)

    def get_graph(self):
        nodes, edges = self.graph.get_graph()
        if nodes is None or edges is None:
            raise ValueError("Failed to retrieve graph data")
        return nodes, edges