import unittest
from Task03_04.ALGraph import ALGraph


class TestALGraph(unittest.TestCase):

    def setUp(self):
        self.graph = ALGraph(5)

    def test_add_node(self):
        self.graph.addNode(3)
        self.assertTrue(self.graph.hasNode(3), "Node 3 should exist in the graph")

        self.graph.addNode(5)
        self.assertTrue(self.graph.hasNode(5), "Node 5 should be added to the graph")

    def test_add_edge(self):
        self.graph.addEdge(0, 1)
        self.assertTrue(self.graph.hasEdge(0, 1), "Edge between 0 and 1 should exist")
        self.assertTrue(self.graph.hasEdge(1, 0), "Edge between 1 and 0 should exist")

    def test_remove_node(self):
        self.graph.addNode(2)
        self.graph.removeNode(2)
        self.assertFalse(
            self.graph.hasNode(2), "Node 2 should be removed from the graph"
        )

    def test_remove_edge(self):
        self.graph.addEdge(0, 1)
        self.graph.removeEdge(0, 1)
        self.assertFalse(
            self.graph.hasEdge(0, 1), "Edge between 0 and 1 should be removed"
        )
        self.assertFalse(
            self.graph.hasEdge(1, 0), "Edge between 1 and 0 should be removed"
        )

    def test_dfs(self):
        self.graph.addEdge(0, 1)
        self.graph.addEdge(0, 2)
        self.graph.addEdge(1, 3)
        self.graph.addEdge(2, 4)
        self.assertEqual(
            self.graph.DFS(4, 0), True, "DFS should find the node 4 from node 0"
        )

    def test_edge_cases(self):
        # Test edge case: adding an edge to a non-existent node
        with self.assertRaises(IndexError):
            self.graph.addEdge(0, 10)

        # Test edge case: removing an edge from a non-existent node
        with self.assertRaises(IndexError):
            self.graph.removeEdge(0, 10)

        # Test edge case: removing a non-existent node
        self.graph.removeNode(10)  # Should not raise an error


if __name__ == "__main__":
    unittest.main(verbosity=2)
