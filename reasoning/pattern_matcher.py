# reasoning/pattern_matcher.py

from knowledge_graph.graph import KnowledgeGraph

class PatternMatcher:
    def __init__(self, graph):
        """
        Initialize the PatternMatcher with a reference to a Knowledge Graph,
        allowing access to the graph's nodes and edges.
        """
        self.graph = graph

    def match_node_pattern(self, node_type=None, properties=None):
        """
        Match nodes based on type and properties.
        
        :param node_type: The type of node to match.
        :param properties: A dictionary of properties to match.
        :return: A list of matching node IDs.
        """
        matching_nodes = []
        for node_id, node_data in self.graph.nodes(data=True):
            if node_type and node_data.get("type") != node_type:
                continue
            if properties:
                if not all(item in node_data.get("properties", {}).items() for item in properties.items()):
                    continue
            matching_nodes.append(node_id)
        return matching_nodes

    def match_edge_pattern(self, source_type=None, target_type=None, relationship=None):
        """
        Match edges based on source type, target type, and relationship.
        
        :param source_type: The type of source node.
        :param target_type: The type of target node.
        :param relationship: The relationship type of the edge.
        :return: A list of matching edge tuples (source_id, target_id).
        """
        matching_edges = []
        for source, target, edge_data in self.graph.edges(data=True):
            source_data = self.graph.nodes[source]
            target_data = self.graph.nodes[target]
            
            if source_type and source_data.get("type") != source_type:
                continue
            if target_type and target_data.get("type") != target_type:
                continue
            if relationship and edge_data.get("relationship") != relationship:
                continue
            matching_edges.append((source, target))
        return matching_edges

# Example usage
if __name__ == "__main__":
    from knowledge_graph.graph import KnowledgeGraph

    kg = KnowledgeGraph()
    pattern_matcher = PatternMatcher(kg.graph)

    # Adding nodes and relationships
    kg.graph.add_node("1", type="Person", properties={"name": "Alice"})
    kg.graph.add_node("2", type="Person", properties={"name": "Bob"})
    kg.graph.add_node("3", type="Pet", properties={"name": "Rex", "species": "Dog"})
    kg.graph.add_edge("1", "3", relationship="owns")
    kg.graph.add_edge("2", "3", relationship="owns")

    # Match patterns
    person_nodes = pattern_matcher.match_node_pattern(node_type="Person")
    pet_owners = pattern_matcher.match_edge_pattern(source_type="Person", relationship="owns")

    print("Person Nodes:", person_nodes)
    print("Pet Owners:", pet_owners)