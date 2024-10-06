# Anomaly Detector Schema

This document defines the schema used for validating nodes and edges in an anomaly detection system. The schema is designed to capture different aspects of anomaly detection, including observations, anomalies, thresholds, and patterns.

## Overview

The schema is divided into two main sections: nodes and edges.

- **Nodes** represent entities such as `Observation`, `Anomaly`, `Threshold`, and `Pattern`.
- **Edges** define relationships between nodes, such as `GENERATES`, `TRIGGERS`, `MATCHES_PATTERN`, and `ASSOCIATED_WITH`.

## Project Structure

```
anomaly_detector_project/
│
├── README.md                       # Project overview and instructions
├── requirements.txt                # List of Python dependencies
├── schema/
│   ├── anomaly_detection.json      # Schema definition for the anomaly detector
│   └── validation_rules.json       # Schema validation rules
├── data/
│   ├── initial_nodes.json          # Initial dataset for nodes (e.g., Observations, Anomalies)
│   └── initial_edges.json          # Initial dataset for edges (e.g., GENERATES, MATCHES_PATTERN)
├── src/
│   ├── __init__.py                 # Init file for the Python package
│   ├── graph_builder.py            # Code to create and manage the knowledge graph
│   ├── validation.py               # Validation functions for nodes, edges, and properties
│   ├── data_loader.py              # Functions to load data into the graph
│   └── queries.py                  # Functions to query the knowledge graph
├── notebooks/
│   └── exploratory_analysis.ipynb  # Jupyter notebook for exploring the data and graph
└── tests/
    ├── test_graph_builder.py       # Unit tests for graph building functionality
    ├── test_validation.py          # Unit tests for validation rules
    └── test_queries.py             # Unit tests for querying the graph
```

## Nodes

### Observation
- **id**: Unique identifier for the observation. (Type: `string`, Required: `true`, Unique: `true`)
- **timestamp**: The time at which the observation was made. (Type: `datetime`, Required: `true`)
- **value**: The recorded value of the observation. (Type: `float`, Required: `true`)
- **type**: The type of observation. (Type: `string`, Enum: `["sensor", "log", "metric"]`, Required: `true`)

### Anomaly
- **id**: Unique identifier for the anomaly. (Type: `string`, Required: `true`, Unique: `true`)
- **timestamp**: The time at which the anomaly was detected. (Type: `datetime`, Required: `true`)
- **severity**: Severity level of the anomaly, ranging from 0.0 to 1.0. (Type: `float`, Required: `true`, Min: `0.0`, Max: `1.0`)
- **description**: Additional information about the anomaly. (Type: `string`, Required: `false`)

### Threshold
- **id**: Unique identifier for the threshold. (Type: `string`, Required: `true`, Unique: `true`)
- **value**: The threshold value used for anomaly detection. (Type: `float`, Required: `true`)
- **metric**: The metric associated with the threshold. (Type: `string`, Required: `true`)
- **direction**: Indicates whether the threshold is for values `above` or `below`. (Type: `string`, Enum: `["above", "below"]`, Required: `true`)

### Pattern
- **id**: Unique identifier for the pattern. (Type: `string`, Required: `true`, Unique: `true`)
- **description**: Description of the pattern. (Type: `string`, Required: `true`)
- **type**: The type of pattern, either `temporal` or `correlation`. (Type: `string`, Enum: `["temporal", "correlation"]`, Required: `true`)

## Edges

### GENERATES
- Defines the relationship between an `Observation` and an `Anomaly`.
- **from**: `Observation`
- **to**: `Anomaly`
- **probability**: Probability that the observation generated the anomaly. (Type: `float`, Required: `true`, Min: `0.0`, Max: `1.0`)

### TRIGGERS
- Defines the relationship between a `Threshold` and an `Anomaly`.
- **from**: `Threshold`
- **to**: `Anomaly`

### MATCHES_PATTERN
- Defines the relationship between an `Observation` and a `Pattern`.
- **from**: `Observation`
- **to**: `Pattern`
- **confidence**: Confidence level that the observation matches the pattern. (Type: `float`, Required: `true`, Min: `0.0`, Max: `1.0`)

### ASSOCIATED_WITH
- Defines the relationship between an `Anomaly` and a `Pattern`.
- **from**: `Anomaly`
- **to**: `Pattern`

## Usage

This schema can be used to validate data inputs and relationships in an anomaly detection system. The schema helps ensure consistency and correctness in data, allowing for effective identification and analysis of anomalies.

## Future Enhancements

- Adding more node types to capture additional features, such as actions taken in response to anomalies.
- Expanding edge definitions to include more complex relationships between nodes.

Feel free to contribute or suggest improvements to make the anomaly detection schema more comprehensive and effective.