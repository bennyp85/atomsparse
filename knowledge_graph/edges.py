class Edge:
    def __init__(self, source, target, relationship):
        self.source = source
        self.target = target
        self.relationship = relationship

    def __repr__(self):
        return f"Edge({self.source}, {self.target}, {self.relationship})"