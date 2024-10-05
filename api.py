# api.py
from fastapi import FastAPI
from knowledge_graph.graph import Graph

app = FastAPI()
graph = Graph()

@app.post("/nodes/")
def add_node(node_id: str, node_type: str):
    graph.add_node(node_id, node_type)
    return {"message": "Node added successfully"}

@app.post("/edges/")
def add_edge(source_id: str, target_id: str, relationship: str):
    graph.add_edge(source_id, target_id, relationship)
    return {"message": "Edge added successfully"}

@app.get("/nodes/{node_id}")
def get_node(node_id: str):
    node = graph.get_node(node_id)
    return node

@app.get("/query/")
def query_graph(query: str):
    results = graph.query(query)
    return results