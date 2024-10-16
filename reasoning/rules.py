from typing import Callable, Dict, Any

"""
Example Rules:
1. If a node represents a "Person" and has an "age" property greater than 18, then add a property "is_adult" with the value True.
2. If a node represents a "Car" and has a "fuel" property equal to "empty", then add a property "needs_refuel" with the value True.
3. If a node represents a "Student" and has a "grade" property less than 50, then add a property "needs_tutoring" with the value True.
"""

class Rule:
    def __init__(self, condition: Callable[[Dict[str, Any], str], bool], action: Callable[[Dict[str, Any], str], None]):
        self.condition = condition
        self.action = action

    def is_applicable(self, graph: Dict[str, Any], node: str) -> bool:
        """Checks if the rule is applicable to a node in the graph."""
        return self.condition(graph, node)

    def apply(self, graph: Dict[str, Any], node: str) -> None:
        """Applies the rule to a node in the graph if the rule is applicable."""
        if self.is_applicable(graph, node):
            self.action(graph, node)

# Example usage:
# Define a condition and an action
def example_condition(graph: Dict[str, Any], node: str) -> bool:
    # Example condition logic
    return node in graph

def example_action(graph: Dict[str, Any], node: str) -> None:
    # Example action logic
    graph[node] = "updated"

# Create a rule
rule = Rule(condition=example_condition, action=example_action)

# Example graph and node
graph = {"node1": "value1"}
node = "node1"

# Apply the rule
rule.apply(graph, node)
print(graph)  # Output: {'node1': 'updated'}