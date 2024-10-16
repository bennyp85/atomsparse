import unittest
from reasoning.rules import Rule
from knowledge_graph.graph import KnowledgeGraph
from knowledge_graph.nodes import Node, NodeType
from knowledge_graph.properties import PropertyOntology

class TestRules(unittest.TestCase):
    def setUp(self):
        # Create a mock graph and node for testing
        self.graph = KnowledgeGraph()
        self.graph.nodes = {"1": Node(node_id="1", node_type=NodeType.CHARACTER, property_ontology=PropertyOntology())}
        self.node = "1"
        
        # Define a simple rule for testing
        self.rule = Rule(
            condition=lambda graph, node: graph.nodes[node].node_type == NodeType.CHARACTER,
            action=lambda graph, node: graph.nodes[node].properties.update({"is_alive": True})
        )

    def test_rule_applicability(self):
        # Assert that the rule is applicable
        self.assertTrue(self.rule.is_applicable(self.graph, self.node))
        
        # Modify the node type to make the rule inapplicable
        self.graph.nodes["1"].node_type = NodeType.LITERARY_DEVICE  # Use a valid NodeType
        self.assertFalse(self.rule.is_applicable(self.graph, self.node))

    def test_apply_rule(self):
        # Apply the rule
        self.rule.apply(self.graph, self.node)
        
        # Assert that the property has been added
        self.assertTrue("is_alive" in self.graph.nodes["1"].properties)
        self.assertTrue(self.graph.nodes["1"].properties["is_alive"])

    def test_invalid_rule_structure_applicability(self):
        invalid_rule = Rule(condition=lambda graph, node: True, action=None)  # Invalid rule with None action
        with self.assertRaises(TypeError):
            invalid_rule.apply(self.graph, self.node)

    def test_invalid_rule_structure_apply(self):
        invalid_rule = Rule(condition=None, action=lambda graph, node: True)  # Invalid rule with None condition
        with self.assertRaises(TypeError):
            invalid_rule.is_applicable(self.graph, self.node)

if __name__ == '__main__':
    unittest.main()