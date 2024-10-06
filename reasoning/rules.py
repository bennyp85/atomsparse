# reasoning/rules.py

class RuleEngine:
    def __init__(self, knowledge_graph):
        """
        Initialize the RuleEngine with a reference to a Knowledge Graph.
        
        :param knowledge_graph: A KnowledgeGraph instance that the engine will manipulate.
        """
        self.knowledge_graph = knowledge_graph
        self.rules = {}

    def add_rule(self, rule_name, rule_fn):
        """
        Add a new rule to the engine.
        
        :param rule_name: The name of the rule.
        :param rule_fn: A callable function that implements the rule logic.
        """
        if not callable(rule_fn):
            raise ValueError("rule_fn must be a callable function")
        self.rules[rule_name] = rule_fn

    def apply_rules(self):
        """
        Apply all registered rules to the knowledge graph.
        Calls each rule function, passing the knowledge graph as an argument.
        """
        for rule_name, rule_fn in self.rules.items():
            print(f"Applying rule: {rule_name}")
            rule_fn(self.knowledge_graph)

# Example rule function
def friends_of_friends_rule(graph):
    """
    A simple rule to add a 'knows' relationship for 'friends of friends'.
    If A knows B and B knows C, then A potentially knows C.
    
    :param graph: An instance of KnowledgeGraph.
    """
    for node in graph.graph.nodes():
        # Get direct neighbors of node
        neighbors = set(graph.graph.neighbors(node))
        for neighbor in neighbors:
            # Get second-level neighbors
            second_neighbors = set(graph.graph.neighbors(neighbor)) - {node}
            for second_neighbor in second_neighbors:
                # Add 'knows' relationship if not already present
                if not graph.graph.has_edge(node, second_neighbor):
                    print(f"Adding 'knows' relationship: {node} -> {second_neighbor}")
                    graph.graph.add_edge(node, second_neighbor, relationship='knows')
