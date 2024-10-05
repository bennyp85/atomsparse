# knowledge_graph/interface.py
from knowledge_graph.graph import KnowledgeGraph
from reasoning.query import GraphQuery
from reasoning.rules import RuleEngine
from reasoning.pattern_matcher import PatternMatcher

class KnowledgeGraphAPI:
    def __init__(self):
        self.graph = KnowledgeGraph()
        self.query_engine = GraphQuery(self.graph.graph)
        self.rule_engine = RuleEngine(self.graph.graph)
        self.pattern_matcher = PatternMatcher(self.graph.graph)

    def add_node(self, node_id, node_type, properties=None):
        self.graph.add_node(node_id, node_type, properties)

    def add_edge(self, source_id, target_id, relationship):
        self.graph.add_edge(source_id, target_id, relationship)

    def get_node(self, node_id):
        node_data = self.graph.graph.nodes[node_id]
        return {"type": node_data["type"], "properties": node_data["properties"]}

    def query(self, query):
        nodes = [(node, data) for node, data in self.graph.graph.nodes(data=True)]
        edges = [(source, target, data) for source, target, data in self.graph.graph.edges(data=True)]
        return {"nodes": nodes, "edges": edges}

    # Integrating GraphQuery methods
    def find_nodes_by_type(self, node_type):
        return self.query_engine.find_nodes_by_type(node_type)
    
    def find_nodes_by_property(self, key, value):
        return self.query_engine.find_nodes_by_property(key, value)

    def find_direct_connections(self, node_id):
        return self.query_engine.find_direct_connections(node_id)

    def find_shortest_path(self, start_node_id, end_node_id):
        return self.query_engine.find_shortest_path(start_node_id, end_node_id)
    
    def match_pattern(self, pattern):
        return self.query_engine.match_pattern(pattern)
    
    def perform_advanced_query(self, query):
        return self.query_engine.perform_advanced_query(query)

    def evaluate_rules(self, rules):
        return self.query_engine.evaluate_rules(rules)

    # Integrating RuleEngine methods
    def add_rule(self, rule):
        self.rule_engine.add_rule(rule)

    def apply_rules(self):
        self.rule_engine.apply_rules()

    # Integrating PatternMatcher methods
    def match_node_pattern(self, node_type=None, properties=None):
        return self.pattern_matcher.match_node_pattern(node_type, properties)

    def match_edge_pattern(self, source_type=None, target_type=None, relationship=None):
        return self.pattern_matcher.match_edge_pattern(source_type, target_type, relationship)
    
