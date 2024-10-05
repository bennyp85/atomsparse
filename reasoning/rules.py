# reasoning/rules.py

from knowledge_graph.graph import KnowledgeGraph

class RuleEngine:
    def __init__(self, graph):
        """
        Initialize the RuleEngine with a reference to a Knowledge Graph,
        which will be used to apply and store inferred knowledge.
        """
        self.graph = graph
        self.rules = []

    def add_rule(self, rule):
        """
        Add a new rule to the engine. Each rule should be a callable that
        takes the graph and performs inference.
        """
        if callable(rule):
            self.rules.append(rule)
        else:
            raise ValueError("Rule must be a callable function.")

    def apply_rules(self):
        """
        Apply all rules in the engine to the knowledge graph.
        """
        for rule in self.rules:
            rule(self.graph)

# Example rule functions

def friends_of_friends_rule(graph):
    """
    A simple rule that adds a 'knows' relationship for 'friends of friends'.
    If A knows B and B knows C, then A knows C.
    """
    nodes = graph.nodes()
    
    for node in nodes:
        friends = set(edge[1] for edge in graph.edges(node, data=True) if edge[2]['relationship'] == 'knows')
        for friend in friends:
            friends_of_friend = set(edge[1] for edge in graph.edges(friend, data=True) if edge[2]['relationship'] == 'knows')
            for f_of_f in friends_of_friend:
                if f_of_f != node and not graph.has_edge(node, f_of_f):
                    graph.add_edge(node, f_of_f, relationship='knows')
