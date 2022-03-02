import unittest
from graph import Graph


class GraphTests(unittest.TestCase):
    def test_should_construct_a_graph(self):
        graph = Graph()

        # Expected number of vertices
        expected = 0

        self.assertEqual(graph.numVertices, expected)

    def test_should_add_a_vertex(self):
        graph = Graph()

        graph.addVertex(1)

        # Expected number of vertices
        expected = 1

        self.assertEqual(graph.numVertices, expected)

    def test_should_return_vertex_if_it_exist(self):
        graph = Graph()

        graph.addVertex(1)

        # Expected number of vertices
        expectedVertextId = 1

        actualVertex = graph.getVertex(1)

        self.assertEqual(actualVertex.getId(), expectedVertextId)

    def test_should_return_none_if_vertex_is_not_present(self):
        graph = Graph()

        graph.addVertex(1)

        # Expected number of vertices
        expected = None

        actualVertex = graph.getVertex(2)

        self.assertEqual(actualVertex, expected)

    def test_should_add_an_edge_between_two_vertexes(self):
        graph = Graph()

        graph.addVertex(1)
        graph.addVertex(2)

        graph.addEdge(1, 2)
        # Number of neighbours of Vertex 1
        expected = 1

        self.assertEqual(len(graph.getVertex(1).getConnections()), expected)
