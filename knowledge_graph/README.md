# Knowledge Graph Module

The `knowledge_graph` module is a core component of this project, designed to represent and manipulate knowledge graphs. It provides the following functionalities:

- **Node and Edge Management**: Create and manage nodes and edges, representing concepts and relationships within the graph.
- **Property Validation**: Define and enforce property schemas to ensure data integrity across nodes and edges.
- **Factories for Nodes and Edges**: Use `NodeFactory` and `EdgeFactory` to streamline the creation of nodes and edges with validated properties.
- **Graph Operations**: Perform operations such as adding, deleting, and updating nodes and edges within the graph.
- **Relationship Types**: Utilize predefined relationship types to establish connections between nodes.

## Structure

- `properties.py`: Defines property types and schemas for nodes and edges.
- `nodes.py`: Manages node creation and property assignment.
- `edges.py`: Manages edge creation and property assignment.
- `graph.py`: Provides operations for managing the graph structure.
- `node_factory.py` and `edge_factory.py`: Factories for creating nodes and edges.
- `relationships.py`: Defines relationship types between nodes.
- `graph_builder.py`: Provides a builder pattern for constructing complex graphs.

## Usage

To use the `knowledge_graph` module, import the necessary classes and create instances of nodes, edges, and graphs as needed.

### Example

```python
from knowledge_graph.graph_builder import GraphBuilder
from knowledge_graph.properties import PropertyType

# Initialize the graph builder
builder = GraphBuilder()

# Add properties to the ontology
builder.add_property(name="name", data_type=PropertyType.STRING, description="Name of the node", required=True)

# Add nodes
builder.add_node(node_id="1", node_type=NodeType.BOOK, properties={"name": "1984"})
builder.add_node(node_id="2", node_type=NodeType.CHARACTER, properties={"name": "Winston Smith"})

# Add an edge
builder.add_edge(source_id="1", target_id="2", relationship=RelationshipType.INVOLVES)

# Build the graph
graph = builder.build()

# Print the graph
print(graph)