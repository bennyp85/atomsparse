from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.properties import NodeType, RelationshipType
from reasoning.query import get_nodes_by_type, get_neighbor_nodes

# Example graph (replace with your actual graph construction)
graph = KnowledgeGraph()
# ... (Add nodes and edges to the graph) ...

# Get all book nodes
book_nodes = get_nodes_by_type(graph, NodeType.BOOK)
print("Book nodes:", book_nodes)

# Get all characters involved in a specific book (replace with actual node ID)
characters = get_neighbor_nodes(graph, "book_node_id", RelationshipType.INVOLVES) 
print("Characters involved:", characters)
