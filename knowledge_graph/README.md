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

## Usage

To use the `knowledge_graph` module, import the necessary classes and create instances of nodes, edges, and graphs as needed.
