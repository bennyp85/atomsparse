# knowledge_graph/graph.py
import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id, node_type, properties=None):
        if properties is None:
            properties = {}
        self.graph.add_node(node_id, type=node_type, properties=properties)

    def add_edge(self, source_id, target_id, relationship):
        self.graph.add_edge(source_id, target_id, relationship=relationship)