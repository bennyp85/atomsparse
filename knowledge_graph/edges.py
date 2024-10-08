# knowledge_graph/edges.py

class Edge:
    def __init__(self, source_id, target_id, relationship):
        self.source_id = source_id
        self.target_id = target_id
        self.relationship = relationship

    @staticmethod
    def create_edge(source_id, target_id, relationship):
        if not source_id or not target_id or not relationship:
            raise ValueError("source_id, target_id, and relationship are required")
        return Edge(source_id, target_id, relationship)

    def __repr__(self):
        return f"Edge(source={self.source_id}, target={self.target_id}, relationship={self.relationship})"
