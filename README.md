# Simplified Knowledge Graph Project

This project aims to create a simplified version of a knowledge graph system, which represents concepts as nodes and relationships as edges. The goal is to support basic operations for adding nodes and edges, querying the graph, and reasoning about relationships between nodes using simple rules. The project now includes a robust property validation system to ensure data integrity.

## Project Structure

```
.
├── knowledge_graph/
│   ├── __init__.py                   # Initialize the knowledge graph module.
│   ├── graph.py                      # Main file for creating and manipulating the graph (using NetworkX).
│   ├── nodes.py                      # Functions for adding and managing nodes in the graph.
│   ├── edges.py                      # Functions for adding and managing edges (relationships) between nodes.
│   ├── properties.py                 # Property validation system and schema management.
│   ├── valuation.py                  # Logic for managing values like confidence or probabilities for nodes/relationships.
│   └── interface.py                  # API for interacting with the knowledge graph.
├── reasoning/
│   ├── __init__.py                   # Initialize the reasoning module.
│   ├── rules.py                      # Define rules for basic reasoning (e.g., forward chaining, inheritance).
│   ├── pattern_matcher.py            # Functions for pattern matching queries in the graph.
│   └── query.py                      # Basic functions to query nodes, edges, or perform searches in the graph.
├── examples/
│   ├── add_pets.py                   # Example script to add some nodes and edges representing pets and their owners.
│   └── simple_queries.py             # Example script for running simple queries like "Who owns a pet?".
├── tests/
│   ├── __init__.py                   # Initialize the tests module.
│   ├── test_graph.py                 # Unit tests for the knowledge graph creation, manipulation, and property validation.
│   ├── test_reasoning.py             # Unit tests for the rule-based reasoning system.
│   └── test_queries.py               # Unit tests for graph querying.
├── requirements.txt                  # List dependencies like NetworkX or any other libraries used.
├── README.md                         # Overview of the project and instructions for setup and use.
└── main.py                           # Entry point to demonstrate how the knowledge graph can be created and used.
```

## Features
- **Knowledge Graph Representation**: Represent concepts as nodes and relationships as edges using Python.
- **Basic Graph Operations**: Add nodes, edges, and properties to represent information in a structured manner.
- **Property Validation System**: Define and enforce property schemas to ensure data integrity.
- **Rule-Based Reasoning**: Define simple rules to perform inferences on the knowledge graph.
- **Pattern Matching and Queries**: Perform basic pattern matching queries on the graph to locate information and relationships.

## Getting Started

### Prerequisites
- Python 3.8+
- NetworkX for graph manipulation

Install the required dependencies:
```sh
pip install -r requirements.txt
```

### Running the Project

1. **Create and Manipulate Graph**
   - You can use `main.py` to create a simple knowledge graph and interact with it.

   ```sh
   python main.py
   ```

2. **Examples**
   - Run example scripts in the `examples/` directory to learn more about how to add nodes, edges, and query the graph.

   ```sh
   python examples/add_pets.py
   python examples/simple_queries.py
   ```

3. **Run Tests**
   - To ensure everything is functioning correctly, run the tests provided in the `tests/` directory.

   ```sh
   python -m unittest discover tests
   ```

## Usage

### Creating a Knowledge Graph

```python
from knowledge_graph.interface import KnowledgeGraphAPI
from knowledge_graph.properties import PropertyType

# Create a new knowledge graph
kg_api = KnowledgeGraphAPI()

# Define property schemas
kg_api.add_property_schema("name", PropertyType.STRING, "Name of the entity")
kg_api.add_property_schema("age", PropertyType.INTEGER, "Age of the person")
kg_api.add_property_schema("species", PropertyType.STRING, "Species of the pet")

# Add nodes with properties
kg_api.add_node("1", "Person", {"name": "John Doe", "age": 30})
kg_api.add_node("2", "Pet", {"name": "Rex", "species": "Dog"})

# Add an edge
kg_api.add_edge("1", "2", "owns")

# Update a property
kg_api.update_node_property("1", "age", 31)

# Get the graph data
nodes, edges = kg_api.get_graph()
print(nodes)
print(edges)
```

This project is intended for educational purposes, as a stepping stone to understand the basics of knowledge graphs, how relationships can be represented, and how simple inferences can be made. You can extend it further by integrating more complex rule engines or scaling it up to use databases like Neo4j.

## Contributing
Feel free to submit issues or pull requests if you have ideas to improve this project or want to add more features.

## License
This project is licensed under the MIT License.
