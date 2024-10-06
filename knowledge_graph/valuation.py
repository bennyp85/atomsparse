# knowledge_graph/valuation.py
from knowledge_graph.nodes import Node
from knowledge_graph.edges import Edge
from knowledge_graph.properties import Property

def evaluate_node(node):
    """
    Evaluate a node based on its properties. Assign a score based on the quality
    and significance of its properties.

    Parameters:
        node (Node): A node object containing properties.

    Returns:
        float: A score representing the value of the node.
    """
    if not isinstance(node, Node):
        raise TypeError("Expected node to be of type 'Node'")
    
    if not isinstance(node.properties, list):
        raise ValueError("Properties must be a list of Property instances")
    
    if not node.properties:
        raise ValueError("Node must have at least one property")
    
    score = 0.0

    for prop in node.properties:
        if not isinstance(prop, Property):
            raise TypeError("All properties must be instances of the Property class")

        # Use evaluate_property to get the score for each property
        score += evaluate_property(prop)

    # Normalizing the score based on the number of properties
    if len(node.properties) > 0:
        score /= len(node.properties)

    return score


def evaluate_edge(edge):
    """
    Evaluate an edge based on its relationship type and the nodes it connects.
    Assign a score depending on the relationship significance.

    Parameters:
        edge (Edge): An edge object containing source, target, and relation.

    Returns:
        float: A score representing the value of the edge.
    """
    if not isinstance(edge, Edge):
        raise TypeError("Expected edge to be of type 'Edge'")

    score = 0.0

    # Assign score based on relation type (e.g., 'important' relations have a higher score)
    relation_weights = {
        "is_a": 1.5,
        "part_of": 1.2,
        "related_to": 1.0,
        "similar_to": 0.8,
    }
    score += relation_weights.get(edge.relation, 0.5)  # Default score if relation is unknown

    # Boost score based on the quality of nodes it connects
    score += (evaluate_node(edge.source) + evaluate_node(edge.target)) * 0.1

    return score


def evaluate_property(property):
    """
    Evaluate a property based on its key-value pair.
    Assign a score depending on the type and significance of the property.

    Parameters:
        property (Property): A property object containing key and value.

    Returns:
        float: A score representing the value of the property.
    """
    if not isinstance(property, Property):
        raise TypeError("Expected property to be of type 'Property'")

    score = 0.0

    # Define key importance weights
    key_weights = {
        "name": 1.5,
        "type": 1.2,
        "description": 1.0,
        "category": 0.8,
    }
    score += key_weights.get(property.name, 0.5)  # Default score if key is unknown

    return score