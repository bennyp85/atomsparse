# tests/test_api.py
import pytest
from httpx import AsyncClient, ASGITransport
from api import app

@pytest.mark.asyncio
async def test_add_node():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/nodes/", json={"node_id": "1", "node_type": "Person", "properties": {"name": "John Doe", "age": 30}})
    assert response.status_code == 200
    assert response.json() == {"message": "Node added successfully"}

@pytest.mark.asyncio
async def test_add_edge():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        await ac.post("/nodes/", json={"node_id": "1", "node_type": "Person", "properties": {"name": "John Doe", "age": 30}})
        await ac.post("/nodes/", json={"node_id": "2", "node_type": "Pet", "properties": {"name": "Rex", "species": "Dog"}})
        response = await ac.post("/edges/", json={"source_id": "1", "target_id": "2", "relationship": "owns"})
    assert response.status_code == 200
    assert response.json() == {"message": "Edge added successfully"}

@pytest.mark.asyncio
async def test_get_node():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        await ac.post("/nodes/", json={"node_id": "1", "node_type": "Person", "properties": {"name": "John Doe", "age": 30}})
        response = await ac.get("/nodes/1")
    assert response.status_code == 200
    assert response.json() == {"type": "Person", "properties": {"name": "John Doe", "age": 30}}

@pytest.mark.asyncio
async def test_query_graph():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        await ac.post("/nodes/", json={"node_id": "1", "node_type": "Person", "properties": {"name": "John Doe", "age": 30}})
        await ac.post("/nodes/", json={"node_id": "2", "node_type": "Pet", "properties": {"name": "Rex", "species": "Dog"}})
        await ac.post("/edges/", json={"source_id": "1", "target_id": "2", "relationship": "owns"})
        response = await ac.get("/query/?query=some_query")
    assert response.status_code == 200
    expected_response = {
        "results": {
            "nodes": [
                ["1", {"type": "Person", "properties": {"name": "John Doe", "age": 30}}],
                ["2", {"type": "Pet", "properties": {"name": "Rex", "species": "Dog"}}]
            ],
            "edges": [
                ["1", "2", {"relationship": "owns"}]
            ]
        }
    }
    assert response.json() == expected_response