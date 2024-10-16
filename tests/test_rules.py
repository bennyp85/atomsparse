import unittest
from reasoning.rules import apply_rule, is_rule_applicable
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node
from knowledge_graph.properties import PropertyOntology

class TestRules(unittest.TestCase):
    def test_rule_applicability(self):
        # Define a simple rule for testing
        rule = {
            "condition": lambda graph, node: graph.nodes[node].node_type == "character",
            "action": lambda graph, node: graph.nodes[node].properties.update({"is_alive": True})
        }
        
        # Create a mock graph and node for testing
        graph = KnowledgeGraph()
        graph.nodes = {"1": Node(node_id="1", node_type="character", property_ontology=PropertyOntology())}
        node = "1"
        
        # Assert that the rule is applicable
        self.assertTrue(is_rule_applicable(rule, graph, node))
        
        # Modify the node type to make the rule inapplicable
        graph.nodes["1"].node_type = "object"
        self.assertFalse(is_rule_applicable(rule, graph, node))

    def test_apply_rule(self):
        # Define a simple rule for testing
        rule = {
            "condition": lambda graph, node: graph.nodes[node].node_type == "character",
            "action": lambda graph, node: graph.nodes[node].properties.update({"is_alive": True})
        }
        
        # Create a mock graph and node for testing
        graph = KnowledgeGraph()
        graph.nodes = {"1": Node(node_id="1", node_type="character", property_ontology=PropertyOntology())}
        node = "1"
        
        # Apply the rule
        apply_rule(rule, graph, node)
        
        # Assert that the property has been added
        self.assertTrue("is_alive" in graph.nodes["1"].properties)
        self.assertTrue(graph.nodes["1"].properties["is_alive"])
