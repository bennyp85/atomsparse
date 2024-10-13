# Tests for Knowledge Graph Project

This directory contains unit tests for the `knowledge_graph` module, ensuring that all components function as expected. The tests cover various aspects of the module, including node and edge creation, property validation, and graph operations.

## Running Tests

To run all tests, use the following command from the root directory of the project:

```bash
python -m unittest discover tests
```

## Test Structure

- `test_properties.py`: Tests for property schemas and validation.
- `test_nodes.py`: Tests for node creation and property management.
- `test_edges.py`: Tests for edge creation and property management.
- `test_graph.py`: Tests for graph operations such as adding and deleting nodes and edges.
- `test_node_factory.py` and `test_edge_factory.py`: Tests for the node and edge factories.

## Adding New Tests

To add new tests, create a new test file in this directory and follow the structure of existing tests. Ensure that all new tests are covered by the `unittest` framework.
