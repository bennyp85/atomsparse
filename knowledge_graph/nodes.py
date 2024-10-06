# knowledge_graph/nodes.py

class Node:
    def __init__(self, node_id, properties):
        self.node_id = node_id
        self.properties = properties

    @staticmethod
    def add_node(graph, node_id, node_type, properties=None):
        if not node_type:
            raise ValueError("Node type must be specified")
        graph.add_node(node_id, type=node_type, properties=properties or {})


    def __repr__(self):
        return f"Node(id={self.node_id}, properties={self.properties})"