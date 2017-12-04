from pybio.tools.graph import Graph

import pytest
import random

@pytest.fixture
def graph():
    return Graph()

@pytest.fixture
def graph_123(graph):
    n1, n2, n3 = [graph.nodes.add(i) for i in [1, 2, 3]]
    graph.edges[n1, n2] = True
    graph.edges[n2, n3] = True
    graph.edges[n3, n1] = True

    return graph

@pytest.fixture
def graph_112(graph):
    n1, n2 = [graph.nodes.add(i) for i in [1, 1]]
    graph.edges[n1, n2] = True

    graph_112 = Graph()
    graph_112.edges[graph, 2] = True

    return graph_112


class TestGraph():
    def test_add_1(self, graph):
        graph.nodes.add(1)
        assert set(graph.nodes.itervalues()) == {1}

    def test_add_1_to_graph_123(self, graph_123):
        node = graph_123.nodes.add(1)
        assert node in graph_123.nodes

    def test_add_node_1_to_graph_1(self, graph):
        node_1 = graph.nodes.add(1)
        graph.nodes.add(node_1)
        assert len(graph.nodes) == 1

    def test_iter(self, graph_123):
        assert next(iter(graph_123.nodes))() == 1

    def test_1_in_nodes(self, graph_123):
        assert 1 in graph_123.nodes

    def test_discard_1(self, graph_123):
        n1, n2, n3 = graph_123.nodes
        graph_123.nodes.discard(n1)

        assert graph_123.nodes == {n2, n3}
        assert (n1, n2) not in graph_123

    def test_len(self, graph_123):
        assert len(graph_123) == 3

    def test_connect(self, graph):
        graph.edges[1, 1] = 1
        nodes = frozenset(graph.nodes)

        assert len(graph.nodes) == 2
        assert dict(graph.edges) == {nodes: 1}

    def test_edges_getitem(self, graph):
        graph.edges[1, 2] = 3
        nodes = frozenset(graph.nodes)
        assert graph.edges[nodes] == 3

    def test_edges_iter(self, graph_123):
        n1, n2, n3 = graph_123.nodes
        edges = set(iter(graph_123.edges))
        fs = frozenset
        assert edges == {fs((n1, n2)), fs((n2, n3)), fs((n3, n1))}

    def test_edges_len(self, graph_123):
        assert len(graph_123.edges) == 3

    def test_edges_delitem(self, graph_123):
        n1, n2, n3 = graph_123.nodes
        del graph_123.edges[n1, n2]

        assert len(graph_123.edges) == 2

    def test_walk(self, graph_123):
        n1, n2, n3 = graph_123.nodes
        del graph_123.edges[n3, n1]

        assert list(graph_123.walk(n1)) == [1, 2, 3]

    def test_walk_recursive(self, graph_112):
        n11, n2 = graph_112.nodes

        if n2() != 2:
            n11, n2 = n2, n11

        assert list(graph_112.walk(n2)) == [2, 1, 1]
