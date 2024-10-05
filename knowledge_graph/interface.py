# knowledge_graph/interface.py
from knowledge_graph.graph import KnowledgeGraph

class KnowledgeGraphAPI:
    def __init__(self):
        self.graph = KnowledgeGraph()

    def add_node(self, node_id, node_type, properties=None):
        self.graph.add_node(node_id, node_type, properties)

    def add_edge(self, source_id, target_id, relationship):
        self.graph.add_edge(source_id, target_id, relationship)

    def get_node(self, node_id):
        node_data = self.graph.graph.nodes[node_id]
        return {"type": node_data["type"], "properties": node_data["properties"]}

    def query(self, query):
        nodes = [(node, data) for node, data in self.graph.graph.nodes(data=True)]
        edges = [(source, target, data) for source, target, data in self.graph.graph.edges(data=True)]
        return {"nodes": nodes, "edges": edges}