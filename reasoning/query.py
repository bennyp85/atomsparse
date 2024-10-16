from knowledge_graph.properties import NodeType
from knowledge_graph.relationships import RelationshipType

def get_node_by_id(graph, node_id):
  """Retrieves a node from the graph based on its ID."""
  return graph.get_node(node_id)

def get_nodes_by_type(graph, node_type):
  """Retrieves all nodes of a specific type from the graph."""
  nodes = []
  for node_id, node in graph.nodes.items():
    if node.node_type == node_type:
      nodes.append(node)
  return nodes

def get_edges_by_relationship(graph, relationship_type):
  """Retrieves all edges with a specific relationship type from the graph."""
  edges = []
  for edge in graph.edges:
    if edge.relationship == relationship_type:
      edges.append(edge)
  return edges

def get_nodes_by_property_value(graph, property_name, property_value):
  """Retrieves all nodes with a specific property value."""
  nodes = []
  for node_id, node in graph.nodes.items():
    if property_name in node.properties and node.properties[property_name] == property_value:
      nodes.append(node)
  return nodes

def get_neighbor_nodes(graph, node_id, relationship_type):
  """Retrieves neighbor nodes connected by a specific relationship."""
  neighbors = []
  for edge in graph.edges:
    if edge.relationship == relationship_type:
      if edge.source_id == node_id:
        neighbors.append(graph.get_node(edge.target_id))
      elif edge.target_id == node_id:
        neighbors.append(graph.get_node(edge.source_id))
  return neighbors
