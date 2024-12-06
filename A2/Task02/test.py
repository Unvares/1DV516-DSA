import unittest
from BinaryTree import BinaryTree


class TestBinaryTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Most test cases use the same default tree defined in setUp method")
        print("Check README for its diagram")

    def setUp(self):
        print("\nSetting up the binary tree structure for tests")
        self.root = BinaryTree(1)
        self.root.insert(2)
        self.root.insert(3)
        self.root.insert(4)
        self.root.insert(5)
        self.root.insert(6)
        self.root.insert(7)

    def test_empty_tree(self):
        print("Testing an empty tree")
        empty_tree = BinaryTree()
        self.assertIsNone(empty_tree.root, "The root of an empty tree should be None")
        self.assertEqual(empty_tree.size(), 0, "The size of an empty tree should be 0")
        print("Empty tree test passed")

    def test_single_node_tree(self):
        print("Testing a single-node tree")
        single_node_tree = BinaryTree(10)
        self.assertEqual(single_node_tree.root, 10, "The root of the tree should be 10")
        self.assertTrue(
            single_node_tree.is_leaf(),
            "The root node should be a leaf if it's the only node in the tree",
        )
        self.assertEqual(
            single_node_tree.size(),
            1,
            "The tree size should be 1 after inserting a single node",
        )
        print("Single-node tree test passed")

    def test_insert(self):
        print("Testing insert method")
        self.root.insert(8)
        self.assertEqual(
            self.root.left.left.root, 4, "The left-left child of the root should be 4"
        )
        self.assertEqual(
            self.root.left.right.root, 5, "The left-right child of the root should be 5"
        )
        self.assertEqual(
            self.root.right.left.root, 6, "The right-left child of the root should be 6"
        )
        self.assertEqual(
            self.root.right.right.root,
            7,
            "The right-right child of the root should be 7",
        )
        self.assertEqual(
            self.root.left.left.left.root,
            8,
            "The left-left-left child of the root should be 8",
        )
        print("insert method passed")

    def test_insert_duplicate(self):
        print("Testing insert method with duplicate values")
        self.assertFalse(
            self.root.insert(3), "Inserting duplicate value 3 should return False"
        )
        self.assertEqual(
            self.root.size(),
            7,
            "The size of the tree should remain 7 after attempting to insert a duplicate",
        )
        print("insert duplicate test passed")

    def test_depth(self):
        print("Testing depth method")
        self.assertEqual(self.root.depth(), 0, "The depth of the root should be 0")
        self.assertEqual(
            self.root.left.depth(), 1, "The depth of the left child should be 1"
        )
        self.assertEqual(
            self.root.left.left.depth(),
            2,
            "The depth of the left-left child should be 2",
        )
        print("depth method passed")

    def test_height(self):
        print("Testing height method")
        self.assertEqual(self.root.height(), 2, "The height of the root should be 2")
        self.assertEqual(
            self.root.left.height(), 1, "The height of the left child should be 1"
        )
        self.assertEqual(
            self.root.left.left.height(),
            0,
            "The height of the left-left child should be 0",
        )
        print("height method passed")

    def test_is_leaf(self):
        print("Testing is_leaf method")
        self.assertFalse(self.root.is_leaf(), "The root should not be a leaf")
        self.assertFalse(
            self.root.left.is_leaf(), "The left child should not be a leaf"
        )
        self.assertTrue(
            self.root.left.left.is_leaf(), "The left-left child should be a leaf"
        )
        print("is_leaf method passed")

    def test_size(self):
        print("Testing size method")
        self.assertEqual(self.root.size(), 7, "The size of the tree should be 7")
        self.assertEqual(
            self.root.left.size(), 3, "The size of the left subtree should be 3"
        )
        self.assertEqual(
            self.root.right.size(), 3, "The size of the right subtree should be 3"
        )
        print("size method passed")

    def test_traverse(self):
        print("Testing traverse method")
        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.root.traverse()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip().split("\n")
        expected_output = ["4", "2", "5", "1", "6", "3", "7"]
        self.assertEqual(
            output, expected_output, "The in-order traversal output is incorrect"
        )
        print("traverse method passed")


if __name__ == "__main__":
    unittest.main(verbosity=0)
