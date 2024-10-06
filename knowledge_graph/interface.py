# knowledge_graph/interface.py
from knowledge_graph.graph import KnowledgeGraph

class KnowledgeGraphAPI:
    def __init__(self):
        self.graph = KnowledgeGraph()

    def add_node(self, node_id, node_type, properties=None):
        self.graph.add_node(node_id, node_type, properties)

    def add_edge(self, source_id, target_id, relationship):
        self.graph.add_edge(source_id, target_id, relationship)