# Tests Directory

This directory contains unit tests for the Anomaly Detector system. The tests ensure that each component of the system functions correctly and adheres to the defined schemas and requirements.

## Contents

- **`test_graph_builder.py`**: Tests the graph building functionalities, ensuring nodes and edges are correctly added and managed within the knowledge graph.
- **`test_validation.py`**: Validates that the schema validation functions correctly identify valid and invalid data structures.
- **`test_queries.py`**: Tests the query functions to ensure accurate retrieval and analysis of data from the knowledge graph.

## Running Tests

1. **Prerequisites**:
    - Ensure all dependencies are installed as per `requirements.txt`.
    - Install `pytest` if not already installed:

        ```bash
        pip install pytest
        ```

2. **Execute Tests**:
    - Navigate to the project root directory.
    - Run all tests using pytest:

        ```bash
        pytest tests/
        ```

    - To run a specific test file:

        ```bash
        pytest tests/test_graph_builder.py
        ```

## Writing Tests

When adding new features or modules:

1. **Create a Test File**: Follow the naming convention `test_<module_name>.py`.
2. **Write Test Cases**:
    - Use descriptive names for test functions to indicate what they are testing.
    - Cover edge cases and typical use cases.
    - Use fixtures to set up common test data if necessary.

3. **Example Test Structure**:

    ```python
    import pytest
    from src.graph_builder import create_graph, add_node

    def test_add_node():
        graph = create_graph()
        node = {"id": "obs_1", "timestamp": "2024-10-07T12:00:00Z", "value": 100.0, "type": "sensor"}
        add_node(graph, node)
        assert graph.has_node("obs_1")
        assert graph.nodes["obs_1"]["value"] == 100.0
    ```

## Continuous Integration

Integrate tests into the CI/CD pipeline to ensure that all tests pass before merging changes. Tools like GitHub Actions, Travis CI, or Jenkins can be configured to run tests automatically on each commit or pull request.

## Best Practices

- **Isolation**: Ensure that tests are independent and do not rely on each other.
- **Clarity**: Write clear and concise test cases with descriptive names.
- **Coverage**: Strive for high test coverage, especially for critical functionalities.
- **Documentation**: Comment on complex test cases to explain their purpose.

## Future Enhancements

- Implement integration tests to assess the interaction between different modules.
- Use mock objects to simulate external dependencies or complex scenarios.
- Incorporate test coverage tools like `coverage.py` to monitor and improve test coverage.

---

