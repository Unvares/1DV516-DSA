import unittest
from LCRSNode import LCRSNode


class TestLCRSNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Most test cases use the same default tree defined in setUp method")
        print("Check README for its diagram")

    def setUp(self):
        print("\nSetting up the tree structure for tests")
        self.root = LCRSNode(1)
        self.child1 = self.root.add_child(2)
        self.child2 = self.root.add_child(3)
        self.child3 = self.root.add_child(4)
        self.grandchild1 = self.child1.add_child(5)
        self.grandchild2 = self.child1.add_child(6)
        self.grandchild3 = self.child2.add_child(7)
        self.grandchild4 = self.child3.add_child(8)

    def test_empty_tree(self):
        print("Testing an empty tree")
        empty_node = LCRSNode()
        self.assertIsNone(empty_node.key, "The key of an empty node should be None")
        self.assertTrue(empty_node.is_leaf(), "An empty node should be a leaf")
        self.assertEqual(empty_node.degree(), 0, "An empty node should have a degree of 0")
        self.assertEqual(empty_node.height(), 0, "An empty node should have a height of 0")
        self.assertEqual(empty_node.size(), 1, "An empty node should have a size of 1")
        print("Empty tree test passed")

    def test_single_node_tree(self):
        print("Testing a single-node tree")
        single_node = LCRSNode(10)
        self.assertEqual(single_node.key, 10, "The key of the single node should be 10")
        self.assertTrue(single_node.is_leaf(), "A single node should be a leaf")
        self.assertEqual(single_node.degree(), 0, "A single node should have a degree of 0")
        self.assertEqual(single_node.height(), 0, "A single node should have a height of 0")
        self.assertEqual(single_node.size(), 1, "A single node should have a size of 1")
        print("Single-node tree test passed")

    def test_add_child(self):
        print("Testing add_child method")
        new_child = self.root.add_child(9)
        self.assertEqual(new_child.key, 9, "The new child should have a key of 9")
        self.assertEqual(
            self.root.leftChild.rightSibling.rightSibling.rightSibling.key, 9,
            "The last child of the root should have a key of 9"
        )
        print("add_child method passed")

    def test_degree(self):
        print("Testing degree method")
        self.assertEqual(self.root.degree(), 3, "The root should have a degree of 3")
        self.assertEqual(self.child1.degree(), 2, "Child1 should have a degree of 2")
        self.assertEqual(self.child2.degree(), 1, "Child2 should have a degree of 1")
        self.assertEqual(self.child3.degree(), 1, "Child3 should have a degree of 1")
        self.assertEqual(self.grandchild1.degree(), 0, "Grandchild1 should have a degree of 0")
        print("degree method passed")

    def test_height(self):
        print("Testing height method")
        self.assertEqual(self.root.height(), 2, "The root should have a height of 2")
        self.assertEqual(self.child1.height(), 1, "Child1 should have a height of 1")
        self.assertEqual(self.child2.height(), 1, "Child2 should have a height of 1")
        self.assertEqual(self.child3.height(), 1, "Child3 should have a height of 1")
        self.assertEqual(self.grandchild1.height(), 0, "Grandchild1 should have a height of 0")
        print("height method passed")

    def test_is_leaf(self):
        print("Testing is_leaf method")
        self.assertFalse(self.root.is_leaf(), "The root should not be a leaf")
        self.assertFalse(self.child1.is_leaf(), "Child1 should not be a leaf")
        self.assertFalse(self.child2.is_leaf(), "Child2 should not be a leaf")
        self.assertFalse(self.child3.is_leaf(), "Child3 should not be a leaf")
        self.assertTrue(self.grandchild1.is_leaf(), "Grandchild1 should be a leaf")
        self.assertTrue(self.grandchild2.is_leaf(), "Grandchild2 should be a leaf")
        self.assertTrue(self.grandchild3.is_leaf(), "Grandchild3 should be a leaf")
        self.assertTrue(self.grandchild4.is_leaf(), "Grandchild4 should be a leaf")
        print("is_leaf method passed")

    def test_size(self):
        print("Testing size method")
        self.assertEqual(self.root.size(), 8, "The root should have a size of 8")
        self.assertEqual(self.child1.size(), 3, "Child1 should have a size of 3")
        self.assertEqual(self.child2.size(), 2, "Child2 should have a size of 2")
        self.assertEqual(self.child3.size(), 2, "Child3 should have a size of 2")
        self.assertEqual(self.grandchild1.size(), 1, "Grandchild1 should have a size of 1")
        print("size method passed")

    def test_walk(self):
        print("Testing walk method")
        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.root.walk()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip().split("\n")
        expected_output = ["1", "2", "5", "6", "3", "7", "4", "8"]
        self.assertEqual(output, expected_output, "The walk method output is incorrect")
        print("walk method passed")


if __name__ == "__main__":
    unittest.main(verbosity=0)
