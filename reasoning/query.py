# reasoning/query.py

class GraphQuery:
    
    def __init__(self, graph):
        self.graph = graph

    def find_nodes_by_type(self, node_type):
        """Find and return all nodes of a given type."""
        pass
    
    def find_nodes_by_property(self, key, value):
        """Find and return nodes that have a specific property key-value pair."""
        pass

    def find_direct_connections(self, node_id):
        """Find and return all nodes directly connected to a given node."""
        pass

    def find_shortest_path(self, start_node_id, end_node_id):
        """Find and return the shortest path between two nodes."""
        pass
    
    def match_pattern(self, pattern):
        """Perform pattern matching based on a given pattern and return matching subgraphs."""
        pass
    
    def perform_advanced_query(self, query):
        """
        Execute complex queries which might involve multiple conditions or sub-queries.
        This could be a DSL (Domain Specific Language) or rely on another query language.
        """
        pass

    def evaluate_rules(self, rules):
        """Evaluate a set of rules against the graph to infer new information."""
        pass
