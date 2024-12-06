import unittest
from BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Most test cases use the same default tree defined in setUp method")
        print("Check README for its diagram")

    def setUp(self):
        print("\nSetting up the binary search tree structure for tests")
        self.root = BinarySearchTree(4)
        self.root.insert(2)
        self.root.insert(6)
        self.root.insert(1)
        self.root.insert(3)
        self.root.insert(5)
        self.root.insert(7)

    def test_empty_tree(self):
        print("Testing an empty tree")
        empty_tree = BinarySearchTree()
        self.assertIsNone(empty_tree.root, "The root of an empty tree should be None")
        self.assertEqual(empty_tree.size(), 0, "The size of an empty tree should be 0")
        print("Empty tree test passed")

    def test_single_node_tree(self):
        print("Testing a single-node tree")
        single_node_tree = BinarySearchTree(10)
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
        self.assertTrue(self.root.insert(8), "Inserting 8 should return True")
        self.assertFalse(
            self.root.insert(4), "Inserting duplicate value 4 should return False"
        )
        self.assertEqual(
            self.root.right.right.right.root,
            8,
            "The right-right-right child of the root should be 8",
        )
        print("insert method passed")

    def test_insert_into_empty_tree(self):
        print("Testing insert into an empty tree")
        empty_tree = BinarySearchTree()
        self.assertTrue(
            empty_tree.insert(10), "Inserting 10 into an empty tree should return True"
        )
        self.assertEqual(
            empty_tree.root, 10, "The root of the tree should be 10 after insertion"
        )
        print("insert into empty tree test passed")

    def test_degenerate_tree(self):
        print("Testing degenerate tree creation")

        # Create a degenerate tree by inserting elements in sorted order
        degenerate_root = BinarySearchTree(1)
        for value in range(2, 8):
            degenerate_root.insert(value)

        # Check the height of the tree
        expected_height = 6  # For a degenerate tree with 7 nodes, height should be 6
        self.assertEqual(
            degenerate_root.height(),
            expected_height,
            "The height of a degenerate tree with 7 nodes should be 6",
        )

        print("degenerate tree test passed")

    def test_search(self):
        print("Testing search method")
        self.assertEqual(self.root.search(4), 4, "Searching for 4 should return 4")
        self.assertEqual(self.root.search(1), 1, "Searching for 1 should return 1")
        self.assertEqual(self.root.search(7), 7, "Searching for 7 should return 7")
        self.assertIsNone(self.root.search(10), "Searching for 10 should return None")
        print("search method passed")

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
        expected_output = ["1", "2", "3", "4", "5", "6", "7"]
        self.assertEqual(
            output,
            expected_output,
            "The in-order traversal output should match the expected sequence",
        )
        print("traverse method passed")


if __name__ == "__main__":
    unittest.main(verbosity=0)
