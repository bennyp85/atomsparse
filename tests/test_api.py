# tests/test_api.py
import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from api import app
from knowledge_graph.graph import KnowledgeGraph

@pytest.mark.asyncio
async def test_add_node():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/nodes/", json={"node_id": "A", "node_type": "person", "properties": {"name": "Alice"}})
    assert response.status_code == 200
    assert response.json() == {"message": "Node added successfully"}

@pytest.mark.asyncio
async def test_add_edge():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # Add nodes before adding the edge
        await ac.post("/nodes/", json={"node_id": "A", "node_type": "Person", "properties": {"name": "Alice"}})
        await ac.post("/nodes/", json={"node_id": "B", "node_type": "Person", "properties": {"name": "Bob"}})
        response = await ac.post("/edges/", json={"source_id": "A", "target_id": "B", "relationship": "knows"})
    assert response.status_code == 200
    assert response.json() == {"message": "Edge added successfully"}

@pytest.mark.asyncio
async def test_get_graph():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/graph/")
    assert response.status_code == 200
    assert response.json() == {"nodes": {"A": {"type": "Person", "properties": {"name": "Alice"}}, "B": {"type": "Person", "properties": {"name": "Bob"}}}, "edges": {"A": {"B": {"relationship": "knows"}}}}
    




