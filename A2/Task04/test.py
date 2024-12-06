import unittest
from RedBlackTree import RedBlackTree
from Color import Color
from RBNode import RBNode


class TestRBNode(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n=== Running RBNode Tests ===")

    def setUp(self):
        self.node = RBNode(key=10)

    def test_initialization(self):
        print("\nTesting RBNode initialization")
        self.assertEqual(self.node.key, 10, "The node key should be initialized to 10")
        self.assertIsNone(
            self.node.parent, "The node parent should be None upon initialization"
        )
        self.assertIsNone(
            self.node.left, "The node left child should be None upon initialization"
        )
        self.assertIsNone(
            self.node.right, "The node right child should be None upon initialization"
        )
        self.assertEqual(
            self.node.color, Color.RED, "The node color should be initialized to RED"
        )
        print("RBNode initialization test passed")

    def test_add_child_left(self):
        print("\nTesting add_child method for left child")
        left_child = RBNode(key=5)
        self.assertTrue(
            self.node.add_child(left_child), "Adding a left child should return True"
        )
        self.assertEqual(
            self.node.left, left_child, "The left child should be set correctly"
        )
        self.assertEqual(
            left_child.parent,
            self.node,
            "The parent of the left child should be the current node",
        )
        print("add_child method for left child test passed")

    def test_add_child_right(self):
        print("\nTesting add_child method for right child")
        right_child = RBNode(key=15)
        self.assertTrue(
            self.node.add_child(right_child), "Adding a right child should return True"
        )
        self.assertEqual(
            self.node.right, right_child, "The right child should be set correctly"
        )
        self.assertEqual(
            right_child.parent,
            self.node,
            "The parent of the right child should be the current node",
        )
        print("add_child method for right child test passed")

    def test_add_child_duplicate(self):
        print("\nTesting add_child method for duplicate key")
        duplicate_child = RBNode(key=10)
        self.assertFalse(
            self.node.add_child(duplicate_child),
            "Adding a duplicate child should return False",
        )
        print("add_child method for duplicate key test passed")

    def test_depth(self):
        print("\nTesting depth method")
        left_child = RBNode(key=5)
        self.node.add_child(left_child)
        self.assertEqual(
            self.node.left.depth(), 1, "The depth of the left child should be 1"
        )
        print("depth method test passed")

    def test_height(self):
        print("\nTesting height method")
        left_child = RBNode(key=5)
        self.node.add_child(left_child)
        self.assertEqual(
            self.node.height(),
            1,
            "The height of the node should be 1 after adding a left child",
        )
        print("height method test passed")

    def test_is_leaf(self):
        print("\nTesting is_leaf method")
        self.assertTrue(
            self.node.is_leaf(), "The node should be a leaf if it has no children"
        )
        self.node.add_child(RBNode(key=5))
        self.assertFalse(
            self.node.is_leaf(), "The node should not be a leaf after adding a child"
        )
        print("is_leaf method test passed")

    def test_size(self):
        print("\nTesting size method")
        self.assertEqual(
            self.node.size(),
            1,
            "The size of the node should be 1 when it is a single node",
        )
        self.node.add_child(RBNode(key=5))
        self.assertEqual(
            self.node.size(),
            2,
            "The size of the node should be 2 after adding one child",
        )
        print("size method test passed")


class TestRedBlackTree(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("\n=== Running RedBlackTree Tests ===")
        print("\n\Most test cases use the same default tree defined in setUp method")
        print("Check README for its diagram")

    def setUp(self):
        self.tree = RedBlackTree()
        self.values = [11, 2, 14, 1, 7, 15, 5, 8, 4]
        for value in self.values:
            self.tree.rb_insert(value)

    def test_empty_tree(self):
        print("\nTesting an empty Red-Black Tree")
        empty_tree = RedBlackTree()
        self.assertIsNone(
            empty_tree.root, "The root of an empty Red-Black Tree should be None"
        )
        print("Empty Red-Black Tree test passed")

    def test_single_node_tree(self):
        print("\nTesting a single-node Red-Black Tree")
        single_node_tree = RedBlackTree()
        single_node_tree.rb_insert(10)
        self.assertEqual(
            single_node_tree.root.key,
            10,
            "The root key of a single-node tree should be 10",
        )
        self.assertEqual(
            single_node_tree.root.color,
            Color.BLACK,
            "The root color of a single-node tree should be BLACK",
        )
        print("Single-node Red-Black Tree test passed")

    def test_rb_insert(self):
        print("\nTesting rb_insert method")
        self.tree.rb_insert(10)
        self.assertTrue(
            self._is_valid_red_black_tree(self.tree.root),
            "The tree should maintain Red-Black properties after insertion",
        )
        print("rb_insert method test passed")

    def test_insert_duplicate(self):
        print("\nTesting insertion of duplicate")
        self.assertFalse(
            self.tree.rb_insert(11), "Inserting a duplicate value should return False"
        )
        self.assertTrue(
            self._is_valid_red_black_tree(self.tree.root),
            "The tree should maintain Red-Black properties after attempting duplicate insertion",
        )
        print("Duplicate insertion test passed")

    def test_search(self):
        print("\nTesting search method")
        self.assertEqual(
            self.tree.search(11),
            11,
            "Searching for an existing key should return the key",
        )
        self.assertIsNone(
            self.tree.search(20), "Searching for a non-existing key should return None"
        )
        print("search method test passed")

    def test_traverse(self):
        print("\nTesting traverse method")
        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.tree.traverse()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip().split("\n")
        expected_output = ["1", "2", "4", "5", "7", "8", "11", "14", "15"]
        self.assertEqual(
            output,
            expected_output,
            "The in-order traversal output should match the expected sequence",
        )
        print("traverse method test passed")

    def test_degenerate_tree(self):
        print("\nTesting degenerate tree creation")
        # Create a degenerate tree by inserting elements in sorted order
        degenerate_tree = RedBlackTree()
        for value in range(1, 8):
            degenerate_tree.rb_insert(value)

        self.assertTrue(
            self._is_valid_red_black_tree(degenerate_tree.root),
            "The tree should maintain Red-Black properties even when degenerate",
        )

        expected_height = 6  # For a degenerate tree with 7 nodes, height should be 6
        actual_height = degenerate_tree.root.height()
        self.assertNotEqual(
            actual_height,
            expected_height,
            "The height of the tree should not match the expected height of a degenerate tree",
        )

        # Print the tree to show it's not degenerate
        print("\nTree structure after insertions:")
        degenerate_tree._print_tree()
        print()

        print("degenerate tree test passed")

    def _is_valid_red_black_tree(self, node):
        def black_height(n):
            if n is None:
                return 1
            left_height = black_height(n.left)
            right_height = black_height(n.right)
            if left_height != right_height or left_height == 0:
                return 0
            return left_height + (1 if n.color == Color.BLACK else 0)

        def has_no_consecutive_red(n):
            if n is None:
                return True
            if n.color == Color.RED:
                if (n.left and n.left.color == Color.RED) or (
                    n.right and n.right.color == Color.RED
                ):
                    return False
            return has_no_consecutive_red(n.left) and has_no_consecutive_red(n.right)

        def has_valid_black_height(n):
            return black_height(n) > 0

        return has_no_consecutive_red(node) and has_valid_black_height(node)


if __name__ == "__main__":
    unittest.main(verbosity=0)
