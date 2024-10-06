# api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from knowledge_graph.interface import KnowledgeGraphAPI

app = FastAPI()
kg_api = KnowledgeGraphAPI()

class Node(BaseModel):
    node_id: str
    node_type: str
    properties: dict

class Edge(BaseModel):
    source_id: str
    target_id: str
    relationship: str

@app.post("/nodes/")
def add_node(node: Node):
    kg_api.add_node(node.node_id, node.node_type, node.properties)
    return {"message": "Node added successfully"}

@app.post("/edges/")
def add_edge(edge: Edge):
    kg_api.add_edge(edge.source_id, edge.target_id, edge.relationship)
    return {"message": "Edge added successfully"}


