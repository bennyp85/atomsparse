# tests/test_api.py
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_add_node():
    response = client.post(
        "/nodes/",
        json={"node_id": "1", "node_type": "Person", "properties": {"name": "John Doe", "age": 30}},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Node added successfully"}

def test_add_edge():
    # First, ensure the nodes do not already exist by deleting them if they do
    client.delete("/nodes/1")
    client.delete("/nodes/2")

    # Add the nodes that the edge will connect
    client.post(
        "/nodes/",
        json={"node_id": "1", "node_type": "Person", "properties": {"name": "John Doe", "age": 30}},
    )
    client.post(
        "/nodes/",
        json={"node_id": "2", "node_type": "Person", "properties": {"name": "Jane Doe", "age": 25}},
    )

    # Now, add the edge
    response = client.post(
        "/edges/",
        json={"source_id": "1", "target_id": "2", "relationship": "knows"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Edge added successfully"}