# Anomaly Detector Project

This project implements a schema-based anomaly detection system using a knowledge graph. The system is designed to capture various aspects of anomaly detection, including observations, anomalies, thresholds, and patterns, ensuring data consistency and facilitating effective analysis.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Folder Documentation](#folder-documentation)
    - [Schema Directory](./schema/README.md)
    - [Data Directory](./data/README.md)
    - [Source Code Directory](./src/README.md)
    - [Notebooks Directory](./notebooks/README.md)
    - [Tests Directory](./tests/README.md)
- [Usage](#usage)
- [Contributing](#contributing)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Overview

The Anomaly Detector system leverages a well-defined schema to validate and manage data within a knowledge graph. By structuring data into nodes and edges, the system can efficiently identify and analyze anomalies, providing insights into potential issues and patterns.

## Project Structure

```
anomaly_detector_project/
├── README.md                   # Project overview and instructions
├── requirements.txt            # List of Python dependencies
├── schema/
│   ├── anomaly_detection.json  # Schema definition for the anomaly detector
│   └── validation_rules.json   # Schema validation rules
├── data/
│   ├── initial_nodes.json      # Initial dataset for nodes (e.g., Observations, Anomalies)
│   └── initial_edges.json      # Initial dataset for edges (e.g., GENERATES, MATCHES_PATTERN)
├── src/
│   ├── __init__.py             # Init file for the Python package
│   ├── graph_builder.py        # Code to create and manage the knowledge graph
│   ├── validation.py           # Validation functions for nodes, edges, and properties
│   ├── data_loader.py          # Functions to load data into the graph
│   └── queries.py              # Functions to query the knowledge graph
├── notebooks/
│   └── exploratory_analysis.ipynb # Jupyter notebook for exploring the data and graph
└── tests/
        ├── test_graph_builder.py   # Unit tests for graph building functionality
        ├── test_validation.py      # Unit tests for validation rules
        └── test_queries.py         # Unit tests for querying the graph
```

## Folder Documentation

Detailed documentation for each folder is available below:

- [Schema Directory](./schema/README.md)
- [Data Directory](./data/README.md)
- [Source Code Directory](./src/README.md)
- [Notebooks Directory](./notebooks/README.md)
- [Tests Directory](./tests/README.md)

## Usage

1. **Setup Environment**:
        - Install Python dependencies:

                ```bash
                pip install -r requirements.txt
                ```

2. **Initialize the Knowledge Graph**:
        - Use the `data_loader.py` script to load initial data:

                ```python
                from src.data_loader import initialize_graph
                from src.validation import validate_graph

                graph = initialize_graph('data/initial_nodes.json', 'data/initial_edges.json')
                if validate_graph(graph):
                        print("Graph initialized and validated successfully.")
                else:
                        print("Graph validation failed.")
                ```

3. **Explore Data and Perform Analysis**:
        - Open and run the Jupyter notebook:

                ```bash
                jupyter notebook notebooks/exploratory_analysis.ipynb
                ```

4. **Run Queries**:
        - Utilize functions in `queries.py` to extract insights:

                ```python
                from src.queries import find_anomalies

                anomalies = find_anomalies(graph)
                print(anomalies)
                ```

5. **Run Tests**:
        - Execute unit tests to ensure system integrity:

                ```bash
                pytest tests/
                ```

## Contributing

We welcome contributions to enhance the Anomaly Detector system. To contribute:

1. Fork the repository and create a new branch.
2. Implement your changes or new features.
3. Ensure all tests pass and update documentation as needed.
4. Submit a pull request for review.

## Future Enhancements

- **Expand Schema**: Introduce additional node and edge types to capture more complex relationships.
- **Advanced Queries**: Develop more sophisticated query functions for deeper anomaly analysis.
- **Integration**: Connect with external data sources or visualization tools for enhanced functionality.
- **Scalability**: Optimize the system to handle larger datasets and more complex graphs.

## License

This project is licensed under the [MIT License](LICENSE).

---

