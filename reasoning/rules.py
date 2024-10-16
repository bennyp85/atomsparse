from typing import Callable, Dict, Any

def is_rule_applicable(rule: Dict[str, Callable], graph: Dict[str, Any], node: str) -> bool:
    """Checks if a rule is applicable to a node in the graph."""
    if "condition" not in rule:
        raise KeyError("The rule must contain a 'condition' key.")
    return rule["condition"](graph, node)

def apply_rule(rule: Dict[str, Callable], graph: Dict[str, Any], node: str) -> None:
    """Applies a rule to a node in the graph if the rule is applicable."""
    if "condition" not in rule or "action" not in rule:
        raise KeyError("The rule must contain both 'condition' and 'action' keys.")
    if is_rule_applicable(rule, graph, node):
        rule["action"](graph, node)