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

# Example usage
if __name__ == "__main__":
    kg = KnowledgeGraph()
    rule_engine = RuleEngine(kg.graph)

    # Adding nodes and relationships
    kg.graph.add_node("1", type="Person", properties={"name": "Alice"})
    kg.graph.add_node("2", type="Person", properties={"name": "Bob"})
    kg.graph.add_node("3", type="Person", properties={"name": "Charlie"})
    kg.graph.add_edge("1", "2", relationship="knows")
    kg.graph.add_edge("2", "3", relationship="knows")

    # Add and apply rule
    rule_engine.add_rule(friends_of_friends_rule)
    rule_engine.apply_rules()

    # Inspect results
    for node in kg.graph.nodes(data=True):
        print(node)
    for edge in kg.graph.edges(data=True):
        print(edge)