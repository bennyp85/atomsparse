# /home/ben/atomsparse/knowledge_graph/nodes.py

class Node:
    def __init__(self, node_id, properties):
        self.node_id = node_id
        self.properties = properties

    def __repr__(self):
        return f"Node(id={self.node_id}, properties={self.properties})"