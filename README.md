# Knowledge Graph Project

This project is designed to represent and manipulate knowledge graphs, providing a robust framework for managing nodes, edges, and their properties. It includes modules for creating and validating properties, managing nodes and edges, and performing graph operations.

## Features

- **Node and Edge Management**: Create and manage nodes and edges, representing concepts and relationships within the graph.
- **Property Validation**: Define and enforce property schemas to ensure data integrity across nodes and edges.
- **Factories for Nodes and Edges**: Use `NodeFactory` and `EdgeFactory` to streamline the creation of nodes and edges with validated properties.
- **Graph Operations**: Perform operations such as adding, deleting, and updating nodes and edges within the graph.
- **Relationship Types**: Utilize predefined relationship types to establish connections between nodes.

## Getting Started

To get started with this project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd knowledge-graph-project
pip install -r requirements.txt
```

## Project Structure

- **`knowledge_graph/graph.py`**: Manages the nodes and edges of the graph.
- **`knowledge_graph/nodes.py`**: Represents nodes in the graph.
- **`knowledge_graph/edges.py`**: Represents edges in the graph.
- **`knowledge_graph/properties.py`**: Defines property types and schemas for nodes and edges.
- **`knowledge_graph/relationships.py`**: Defines relationship types between nodes.
- **`knowledge_graph/node_factory.py`**: Creates nodes with validated properties.
- **`knowledge_graph/edge_factory.py`**: Creates edges with validated properties.
- **`knowledge_graph/graph_builder.py`**: Provides a builder pattern for constructing complex graphs.
- **`reasoning/query.py`**: Provides methods for querying the graph.
- **`reasoning/rules.py`**: Represents rules that can be applied to nodes in the graph.

## Running Tests

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Test Structure

- **`tests/test_graph.py`**: Tests for `KnowledgeGraph` class operations.
- **`tests/test_nodes.py`**: Tests for `Node` class.
- **`tests/test_edges.py`**: Tests for `Edge` class.
- **`tests/test_properties.py`**: Tests for property schemas and validation.
- **`tests/test_node_factory.py`**: Tests for `NodeFactory` class.
- **`tests/test_edge_factory.py`**: Tests for `EdgeFactory` class.
- **`tests/test_rules.py`**: Tests for `Rule` class.

## License

This project is licensed under the MIT License.