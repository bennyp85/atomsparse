# knowledge_graph/nodes.py

class Node:
    def __init__(self, node_id, properties):
        self.node_id = node_id
        self.properties = properties

    @staticmethod
    def add_node(graph, node_id, properties=None):
        if properties is None:
            properties = {}
        if 'type' not in properties:
            raise ValueError("Node must have a type.")
        graph.add_node(node_id, **properties)

    def __repr__(self):
        return f"Node(id={self.node_id}, properties={self.properties})"