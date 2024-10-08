# knowledge_graph/nodes.py

class Node:
    def __init__(self, node_id, node_type, properties=None):
        self.node_id = node_id
        self.node_type = node_type
        self.properties = properties or {}

    @staticmethod
    def create_node(node_id, node_type, properties=None):
        if not node_id or not node_type:
            raise ValueError("node_id and node_type are required")
        return Node(node_id, node_type, properties)

    def __repr__(self):
        return f"Node(id={self.node_id}, type={self.node_type}, properties={self.properties})"
