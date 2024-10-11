# knowledge_graph/graph.py

class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        if node.node_id in self.nodes:
            raise ValueError(f"Node with id {node.node_id} already exists.")
        self.nodes[node.node_id] = node

    def add_edge(self, edge):
        if edge.source_id not in self.nodes or edge.target_id not in self.nodes:
            raise ValueError("Both source and target nodes must exist in the graph.")
        if any(e.source_id == edge.source_id and e.target_id == edge.target_id and e.relationship == edge.relationship for e in self.edges):
            raise ValueError("Edge already exists.")
        self.edges.append(edge)

    def delete_node(self, node_id):
        if node_id not in self.nodes:
            raise ValueError(f"Node with id {node_id} does not exist.")
        del self.nodes[node_id]
        self.edges = [edge for edge in self.edges if edge.source_id != node_id and edge.target_id != node_id]

    def delete_edge(self, source_id, target_id, relationship):
        self.edges = [edge for edge in self.edges if not (edge.source_id == source_id and edge.target_id == target_id and edge.relationship == relationship)]

    def get_node(self, node_id):
        return self.nodes.get(node_id, None)

    def get_edge(self, source_id, target_id, relationship):
        for edge in self.edges:
            if edge.source_id == source_id and edge.target_id == target_id and edge.relationship == relationship:
                return edge
        return None

    def update_node(self, node_id, properties):
        if node_id not in self.nodes:
            raise ValueError(f"Node with id {node_id} does not exist.")
        node = self.nodes[node_id]
        node.set_properties(properties)

    def update_edge(self, source_id, target_id, relationship, properties):
        edge = self.get_edge(source_id, target_id, relationship)
        if not edge:
            raise ValueError("Edge does not exist.")
        edge.set_properties(properties)