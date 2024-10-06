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
        if source_id not in self.graph.nodes or target_id not in self.graph.nodes:
            raise KeyError("Source and target nodes must exist in the graph.")
        self.graph.add_edge(source_id, target_id, relationship=relationship)

    def get_node(self, node_id):
        node_data = self.graph.nodes[node_id]
        return {"type": node_data["type"], "properties": node_data["properties"]}
    