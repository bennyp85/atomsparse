# knowledge_graph/graph.py

import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node):
        if node.node_id in self.graph:
            raise ValueError(f"Node {node.node_id} already exists.")
        self.graph.add_node(node.node_id, type=node.node_type, properties=node.properties)

    def add_node_by_attributes(self, node_id, node_type, properties=None):
        if node_id in self.graph:
            raise ValueError(f"Node {node_id} already exists.")
        self.graph.add_node(node_id, type=node_type, properties=properties or {})

    def add_edge(self, edge):
        if edge.source_id not in self.graph or edge.target_id not in self.graph:
            raise ValueError(f"Both nodes {edge.source_id} and {edge.target_id} must exist in the graph.")
        if self.graph.has_edge(edge.source_id, edge.target_id):
            raise ValueError(f"Edge from {edge.source_id} to {edge.target_id} already exists.")
        self.graph.add_edge(edge.source_id, edge.target_id, relationship=edge.relationship)

    def delete_node(self, node_id):
        if node_id not in self.graph:
            raise KeyError(f"Node {node_id} does not exist.")
        self.graph.remove_node(node_id)

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
