# knowledge_graph/interface.py
from knowledge_graph.graph import Graph

class KnowledgeGraphAPI:
    def __init__(self):
        self.graph = Graph()

    def add_node(self, node_id: str, node_type: str):
        self.graph.add_node(node_id, node_type)

    def add_edge(self, source_id: str, target_id: str, relationship: str):
        self.graph.add_edge(source_id, target_id, relationship)

    def get_node(self, node_id: str):
        return self.graph.get_node(node_id)

    def query(self, query: str):
        return self.graph.query(query)