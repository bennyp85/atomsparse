# Source Code Directory
This directory contains the source code for the Anomaly Detector system. The modules here are responsible for building and managing the knowledge graph, validating data, loading datasets, and executing queries. The structured organization ensures maintainability, scalability, and ease of collaboration.

## Contents

- **`__init__.py`**: Initializes the Python package.
- **`graph_builder.py`**: Functions to create and manage the knowledge graph, including adding nodes and edges.
- **`validation.py`**: Validation functions to ensure nodes, edges, and their properties adhere to the defined schema.
- **`data_loader.py`**: Functions to load data from JSON files into the knowledge graph.
- **`queries.py`**: Functions to perform queries on the knowledge graph for analysis and anomaly detection.

## Module Overview

### `graph_builder.py`

- **Purpose**: Handles the creation and manipulation of the knowledge graph.
- **Key Functions**:
    - `create_graph()`: Initializes a new knowledge graph instance.
    - `add_node(graph, node)`: Adds a node to the graph.
    - `add_edge(graph, edge)`: Adds an edge to the graph.
    - `remove_node(graph, node_id)`: Removes a node from the graph.
    - `remove_edge(graph, from_id, to_id)`: Removes an edge from the graph.

### `validation.py`

- **Purpose**: Ensures data integrity by validating nodes and edges against the schema.
- **Key Functions**:
    - `validate_node(node)`: Validates a single node.
    - `validate_edge(edge)`: Validates a single edge.
    - `validate_graph(graph)`: Validates the entire graph structure.
- **Utilities**:
    - Schema loading and caching mechanisms for efficient validation.

### `data_loader.py`

- **Purpose**: Facilitates loading of initial datasets into the knowledge graph.
- **Key Functions**:
    - `load_nodes(file_path)`: Loads nodes from a JSON file.
    - `load_edges(file_path)`: Loads edges from a JSON file.
    - `initialize_graph(nodes_file, edges_file)`: Initializes the graph with nodes and edges.
    - `update_graph(graph, nodes_file, edges_file)`: Updates the graph with new data.

### `queries.py`

- **Purpose**: Provides mechanisms to query the knowledge graph for insights and anomaly detection.
- **Key Functions**:
    - `find_anomalies(graph)`: Retrieves anomalies from the graph.
    - `get_related_observations(anomaly_id)`: Fetches observations related to a specific anomaly.
    - `pattern_analysis(graph)`: Analyzes patterns within the graph.
    - `export_graph(graph, format)`: Exports the graph in specified formats (e.g., JSON, GraphML).

## Usage

### Setting Up the Graph

```python
from src.graph_builder import create_graph, add_node, add_edge
from src.data_loader import load_nodes, load_edges, initialize_graph
from src.validation import validate_graph

# Initialize the graph with initial data
graph = initialize_graph('data/initial_nodes.json', 'data/initial_edges.json')

# Validate the graph
if validate_graph(graph):
        print("Graph is valid.")
else:
        print("Graph validation failed.")
```

### Running Queries

```python
from src.queries import find_anomalies, get_related_observations

# Find all anomalies in the graph
anomalies = find_anomalies(graph)
for anomaly in anomalies:
        observations = get_related_observations(anomaly['id'])
        print(f"Anomaly {anomaly['id']} is related to observations: {observations}")
```

### Updating the Graph

```python
from src.data_loader import update_graph

# Update the graph with new nodes and edges
update_graph(graph, 'data/new_nodes.json', 'data/new_edges.json')

# Re-validate after update
if validate_graph(graph):
        print("Graph updated and validated successfully.")
else:
        print("Graph validation failed after update.")
```

## Dependencies

Ensure all dependencies listed in `requirements.txt` are installed. Key dependencies include:

- `networkx`: For graph operations.
- `jsonschema`: For validating JSON data against schemas.
- `pandas`: For data manipulation and analysis.

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Testing

- **Unit Tests**: Located in the `tests/` directory, covering all modules and functionalities.
- **Running Tests**: Navigate to the project root. Execute all tests using `pytest`:

```bash
pytest tests/
```

To run a specific test file:

```bash
pytest tests/test_graph_builder.py
```

## Contributing

We welcome contributions to enhance the source code. To contribute:

1. **Fork the Repository**: Create a personal copy of the repository.
2. **Create a New Branch**: Use a descriptive name for your branch.

        ```bash
        git checkout -b feature/your-feature-name
        ```

3. **Implement Changes**: Modify or add new features in the appropriate module.
4. **Write Tests**: Ensure new functionalities are covered by tests.
5. **Commit Changes**: Provide clear and concise commit messages.

        ```bash
        git commit -m "Add feature X to graph_builder"
        ```

6. **Push to GitHub**:

        ```bash
        git push origin feature/your-feature-name
        ```

7. **Submit a Pull Request**: Describe your changes and submit for review.

## Best Practices

- **Code Quality**: Follow PEP 8 guidelines for Python code.
- **Documentation**: Document functions and modules using docstrings.
- **Modularity**: Keep functions and modules focused on single responsibilities.
- **Version Control**: Commit changes frequently with meaningful messages.

## Future Enhancements

- **Advanced Query Functions**: Develop more sophisticated queries for deeper anomaly analysis.
- **Performance Optimization**: Optimize graph operations for large-scale datasets.
- **Integration with Visualization Tools**: Connect with tools like GraphQL or D3.js for visual insights.
- **Real-time Data Processing**: Implement streaming data capabilities for real-time anomaly detection.
- **API Development**: Create APIs for interacting with the knowledge graph externally.

## License

This project is licensed under the MIT License.