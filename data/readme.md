# Data Directory

This directory holds the initial datasets for nodes and edges used in the Anomaly Detector system. These datasets serve as the foundational data upon which the anomaly detection logic operates.

## Contents

- **`initial_nodes.json`**: Contains the initial set of nodes, including `Observations`, `Anomalies`, `Thresholds`, and `Patterns`. Each node includes necessary attributes as defined in the schema.
- **`initial_edges.json`**: Contains the initial set of edges defining relationships between nodes, such as `GENERATES`, `TRIGGERS`, `MATCHES_PATTERN`, and `ASSOCIATED_WITH`.

## Structure

### Nodes (`initial_nodes.json`)

Each node entry includes:
- **`id`**: Unique identifier.
- **`timestamp`**: Date and time of the observation or anomaly.
- **Other attributes**: Depending on the node type (e.g., `value` for `Observation`, `severity` for `Anomaly`).

### Edges (`initial_edges.json`)

Each edge entry includes:
- **`from`**: Source node ID.
- **`to`**: Target node ID.
- **Other attributes**: Depending on the edge type (e.g., `probability` for `GENERATES`).

## Usage

- **Loading Data**: Use the `data_loader.py` script in the `src/` directory to load these initial datasets into the knowledge graph.
- **Updating Data**: To add more nodes or edges, update the respective JSON files following the schema definitions.

## Contributing

To add or modify data:

1. Ensure that any new nodes or edges comply with the schema defined in the `schema/` directory.
2. Update `initial_nodes.json` or `initial_edges.json` accordingly.
3. Validate the JSON files using the validation scripts or tools.
4. Submit changes through a pull request for review.

## Best Practices

- **Consistency**: Maintain consistent formatting and adhere to the schema to prevent validation errors.
- **Version Control**: Keep track of changes to the data files to manage updates and rollback if necessary.
- **Documentation**: Document any significant changes or additions to the datasets for future reference.

## Future Enhancements

- Introduce additional datasets for different environments or use cases.
- Automate data updates through scripts or data pipelines.
- Implement data versioning to manage historical data changes.

---

