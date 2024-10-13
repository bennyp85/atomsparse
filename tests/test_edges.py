# tests/test_edges.py

import unittest
from unittest.mock import MagicMock
from knowledge_graph.graph_builder import GraphBuilder
from knowledge_graph.properties import PropertyOntology
from knowledge_graph.properties import NodeType, PropertyType
from knowledge_graph.relationships import RelationshipType
from knowledge_graph.edge_factory import EdgeFactory
