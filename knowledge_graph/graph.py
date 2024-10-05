# knowledge_graph/graph.py
import networkx as nx

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id: str, node_type: str):
        self.graph.add_node(node_id, type=node_type)

    def add_edge(self, source_id: str, target_id: str, relationship: str):
        self.graph.add_edge(source_id, target_id, relationship=relationship)

    def get_node(self, node_id: str):
        return self.graph.nodes.get(node_id)

    def query(self, query: str):
        # For simplicity, return all nodes and edges
        nodes = list(self.graph.nodes(data=True))
        edges = list(self.graph.edges(data=True))
        return {"nodes": nodes, "edges": edges}