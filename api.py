# api.py
from fastapi import FastAPI
from pydantic import BaseModel
from knowledge_graph.interface import KnowledgeGraphAPI

app = FastAPI()
kg_api = KnowledgeGraphAPI()

class Node(BaseModel):
    node_id: str
    node_type: str

class Edge(BaseModel):
    source_id: str
    target_id: str
    relationship: str

@app.post("/nodes/")
def add_node(node: Node):
    kg_api.add_node(node.node_id, node.node_type)
    return {"message": "Node added successfully"}

@app.post("/edges/")
def add_edge(edge: Edge):
    kg_api.add_edge(edge.source_id, edge.target_id, edge.relationship)
    return {"message": "Edge added successfully"}

@app.get("/nodes/{node_id}")
def get_node(node_id: str):
    node = kg_api.get_node(node_id)
    return node

@app.get("/query/")
def query_graph(query: str):
    results = kg_api.query(query)
    return {"results": results}