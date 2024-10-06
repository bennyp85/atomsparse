# knowledge_graph/graph.py

import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id, node_type, properties=None):
        if node_id in self.graph:
            raise ValueError(f"Node {node_id} already exists.")
        self.graph.add_node(node_id, type=node_type, properties=properties or {})

    def add_edge(self, source_id, target_id, relationship):
        if source_id not in self.graph or target_id not in self.graph:
            raise ValueError(f"Both nodes {source_id} and {target_id} must exist in the graph.")
        if self.graph.has_edge(source_id, target_id):
            raise ValueError(f"Edge from {source_id} to {target_id} already exists.")
        self.graph.add_edge(source_id, target_id, relationship=relationship)

    def get_nodes(self):
        return {node: data for node, data in self.graph.nodes(data=True)}

    def get_edges(self):
        edges = {}
        for source, target, data in self.graph.edges(data=True):
            if source not in edges:
                edges[source] = {}
            edges[source][target] = data
        return edges

    def get_graph(self):
        nodes = self.get_nodes()
        edges = self.get_edges()
        return nodes, edges