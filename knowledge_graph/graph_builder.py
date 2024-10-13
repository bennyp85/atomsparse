from .graph import KnowledgeGraph
from .node_factory import NodeFactory
from .edge_factory import EdgeFactory
from .properties import PropertyOntology, PropertySchema, PropertyType
from .relationships import RelationshipType

class GraphBuilder:
    def __init__(self):
        self.property_ontology = PropertyOntology()
        self.node_factory = NodeFactory(self.property_ontology)
        self.edge_factory = EdgeFactory(self.property_ontology)
        self.graph = KnowledgeGraph()

    def add_property(self, name: str, data_type: PropertyType, description: str = "", required: bool = False):
        schema = PropertySchema(name, data_type, description, required)
        self.property_ontology.register_property(schema)

    def add_node(self, node_id: str, node_type, properties: dict = None):
        node = self.node_factory.create_node(node_id, node_type, properties)
        self.graph.add_node(node)

    def add_edge(self, source_id: str, target_id: str, relationship: RelationshipType, properties: dict = None):
        edge = self.edge_factory.create_edge(source_id, target_id, relationship, properties)
        self.graph.add_edge(edge)

    def build(self) -> KnowledgeGraph:
        return self.graph
