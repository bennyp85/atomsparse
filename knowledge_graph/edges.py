from typing import Optional

class Edge:
    def __init__(self, source_id: Optional[int], target_id: Optional[int], relationship: Optional[str]) -> None:
        self.source_id: Optional[int] = source_id
        self.target_id: Optional[int] = target_id
        self.relationship: Optional[str] = relationship

    @staticmethod
    def create_edge(source_id: Optional[int], target_id: Optional[int], relationship: Optional[str]) -> 'Edge':
        if not source_id or not target_id or not relationship:
            raise ValueError("source_id, target_id, and relationship are required")
        return Edge(source_id, target_id, relationship)

    def __repr__(self) -> str:
        return f"Edge(source={self.source_id}, target={self.target_id}, relationship={self.relationship})"

