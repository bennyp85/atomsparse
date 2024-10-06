# Schema Directory

This directory contains the schema definitions and validation rules for the Anomaly Detector system. The schemas ensure that the data structures for nodes and edges adhere to the required formats and constraints, facilitating consistent and accurate anomaly detection.

## Contents

- **`anomaly_detection.json`**: Defines the structure of nodes (`Observation`, `Anomaly`, `Threshold`, `Pattern`) and edges (`GENERATES`, `TRIGGERS`, `MATCHES_PATTERN`, `ASSOCIATED_WITH`) used in the anomaly detection system.
- **`validation_rules.json`**: Specifies the rules and constraints for validating the nodes and edges defined in the schema. This includes data types, required fields, enumerations, and value ranges.

## Usage

- **Schema Definition**: Modify `anomaly_detection.json` to add or update node and edge types as needed.
- **Validation Rules**: Update `validation_rules.json` to enforce new constraints or adjust existing ones to maintain data integrity.

## Contributing

To contribute to the schema definitions or validation rules:

1. Fork the repository and create a new branch.
2. Update the relevant JSON files with your changes.
3. Ensure that all validation rules are correctly defined.
4. Submit a pull request for review.

## Tools

- **JSON Schema Validators**: Use tools like [AJV](https://ajv.js.org/) or [jsonschema](https://pypi.org/project/jsonschema/) for validating JSON data against the defined schemas.

## Future Enhancements

- Introduce additional node and edge types to capture more complex relationships.
- Implement versioning for schemas to manage changes over time.
- Integrate automated schema validation into the CI/CD pipeline.

---

