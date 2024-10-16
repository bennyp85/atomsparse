import unittest
from reasoning.rules import apply_rule, is_rule_applicable
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
        self.rule = {
            "condition": lambda graph, node: graph.nodes[node].node_type == NodeType.CHARACTER,
            "action": lambda graph, node: graph.nodes[node].properties.update({"is_alive": True})
        }

    def test_rule_applicability(self):
        # Assert that the rule is applicable
        self.assertTrue(is_rule_applicable(self.rule, self.graph, self.node))
        
        # Modify the node type to make the rule inapplicable
        self.graph.nodes["1"].node_type = NodeType.LITERARY_DEVICE  # Use a valid NodeType
        self.assertFalse(is_rule_applicable(self.rule, self.graph, self.node))

    def test_apply_rule(self):
        # Apply the rule
        apply_rule(self.rule, self.graph, self.node)
        
        # Assert that the property has been added
        self.assertTrue("is_alive" in self.graph.nodes["1"].properties)
        self.assertTrue(self.graph.nodes["1"].properties["is_alive"])

    def test_invalid_rule_structure_applicability(self):
        invalid_rule = {}  # Missing 'condition'
        with self.assertRaises(KeyError):
            is_rule_applicable(invalid_rule, self.graph, self.node)

    def test_invalid_rule_structure_apply(self):
        invalid_rule = {"condition": lambda graph, node: True}  # Missing 'action'
        with self.assertRaises(KeyError):
            apply_rule(invalid_rule, self.graph, self.node)

if __name__ == '__main__':
    unittest.main()