# knowledge_graph/edges.py

class Edge:
    def __init__(self, source, target, relationship):
        self.source = source
        self.target = target
        self.relationship = relationship

    @staticmethod
    def add_edge(graph, source, target, relationship):
        if source not in graph.nodes or target not in graph.nodes:
            raise ValueError("Source and target nodes must exist in the graph.")
        graph.add_edge(source, target, relationship=relationship)

    def __repr__(self):
        return f"Edge({self.source}, {self.target}, {self.relationship})"