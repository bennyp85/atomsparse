# file: /home/ben/atomsparse/tests/test_valuation.py
import pytest
from knowledge_graph.valuation import evaluate_node
from knowledge_graph.nodes import Node
from knowledge_graph.properties import Property

class TestValuation:
    def test_evaluate_node(self):
        # Create properties for the node
        properties = [
            Property(name="name", value="Node1", data_type=str),
            Property(name="type", value="TypeA", data_type=str),
            Property(name="description", value="This is a test node.", data_type=str),
            Property(name="category", value="Category1", data_type=str)
        ]
        
        # Create a node with the properties and a node_id
        node = Node(node_id="node_1", properties=properties)
        
        # Evaluate the node
        score = evaluate_node(node)
        
        # Assert the expected score
        expected_score = (1.5 + 1.2 + 1.0 + 0.8) / 4  # Simplified expected score calculation
        assert score == pytest.approx(expected_score, rel=1e-2)

    def test_evaluate_node_invalid(self):
        with pytest.raises(TypeError, match="Expected node to be of type 'Node'"):
            evaluate_node("invalid_node")  # Pass 
            evaluate_node(123)
            evaluate_node(3.14)
            evaluate_node(True)
            evaluate_node(None)
            evaluate_node([1, 2, 3])

            