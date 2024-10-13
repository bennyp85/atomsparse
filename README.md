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

## Running Tests

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License.
