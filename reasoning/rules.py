from typing import Callable, Dict, Any

def apply_rule(rule: Dict[str, Callable], graph: Dict[str, Any], node: str) -> None:
    """Applies a rule to a node in the graph if the rule is applicable."""
    if is_rule_applicable(rule, graph, node):
        rule["action"](graph, node)

def is_rule_applicable(rule: Dict[str, Callable], graph: Dict[str, Any], node: str) -> bool:
    """Checks if a rule is applicable to a node in the graph."""
    return rule["condition"](graph, node)
