# knowledge_graph/nodes.py

from .properties import Property

# knowledge_graph/nodes.py

class Node:
    def __init__(self, node_id, properties=None):
        self.node_id = node_id
        self.properties = properties or []

    @staticmethod
    def add_node(graph, node_id, node_type, properties=None):
        if not node_type:
            raise ValueError("Node type must be specified")
    
        # Convert dictionary to list of Property instances if necessary
        if isinstance(properties, dict):
            properties = [Property(name, value, type(value)) for name, value in properties.items()]
    
        # Check if properties is a valid type otherwise raise class TypeError
        if properties and not isinstance(properties, list):
            raise TypeError("Properties must be a list of Property instances")
    
        # Validate properties
        if properties:
            for prop in properties:
                if isinstance(prop, Property):
                    prop.validate()
                else:
                    raise TypeError("All properties must be instances of the Property class")
    
        graph.add_node(node_id, node_type=node_type, properties=properties or [])

    def __repr__(self):
        return f"Node(id={self.node_id}, properties={self.properties})"