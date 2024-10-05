# /home/ben/atomsparse/knowledge_graph/nodes.py

class Node:
    def __init__(self, node_id, node_type):
        self.node_id = node_id
        self.node_type = node_type

    def __repr__(self):
        return f"Node(id={self.node_id}, type={self.node_type})"