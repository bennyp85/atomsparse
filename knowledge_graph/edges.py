# knowledge_graph/edges.py

class Edge:
    def __init__(self, source, target, relationship):
        self.source = source
        self.target = target
        self.relationship = relationship

    @staticmethod
    def add_edge(graph, source_id, target_id, relationship):
        if source_id not in graph or target_id not in graph:
            raise KeyError("One or both nodes do not exist in the graph")
        graph.add_edge(source_id, target_id, relationship=relationship)

    def __repr__(self):
        return f"Edge({self.source}, {self.target}, {self.relationship})"