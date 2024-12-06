from Color import Color
from RBNode import RBNode


class RedBlackTree:
    def __init__(self, root=None):
        """
        Initialize a Red-Black Tree.

        :param root: The root node of the tree, defaults to None.
        """
        self.root = None

    def rb_insert(self, x):
        """
        Insert a new node with the given value into the Red-Black Tree.

        :param x: The value to be inserted into the tree.
        :return: False if a duplicate value is found and insertion is aborted, otherwise None.
        """
        if self.root is None:
            self.root = RBNode(key=x, color=Color.BLACK)
            return

        if self._find_last(x).key == x:
            print("Duplicate value found, insertion aborted.")
            return False

        x = RBNode(key=x)
        self._insert(x)
        self._fix_violations(x)
        self.root.color = Color.BLACK

    def _fix_violations(self, x):
        """
        Fix violations of Red-Black Tree properties after insertion.

        :param x: The node to start fixing from.
        """
        while x != self.root and x.parent.color == Color.RED:
            parent = x.parent
            grandparent = parent.parent
            uncle = (
                grandparent.right if parent == grandparent.left else grandparent.left
            )

            if uncle and uncle.color == Color.RED:
                self._recolor(parent, uncle, grandparent)
                x = grandparent
            else:
                if self._is_LR(x):
                    x = self._handle_LR(x)
                elif self._is_RL(x):
                    x = self._handle_RL(x)

                if self._is_LL(x):
                    self._handle_LL(x)
                elif self._is_RR(x):
                    self._handle_RR(x)
                break

    def _is_LR(self, x):
        """
        Check if the node x is in a Left-Right configuration.

        :param x: The node to check.
        :return: True if x is in a Left-Right configuration, otherwise False.
        """
        return x == x.parent.right and x.parent == x.parent.parent.left

    def _is_LL(self, x):
        """
        Check if the node x is in a Left-Left configuration.

        :param x: The node to check.
        :return: True if x is in a Left-Left configuration, otherwise False.
        """
        return x == x.parent.left and x.parent == x.parent.parent.left

    def _is_RL(self, x):
        """
        Check if the node x is in a Right-Left configuration.

        :param x: The node to check.
        :return: True if x is in a Right-Left configuration, otherwise False.
        """
        return x == x.parent.left and x.parent == x.parent.parent.right

    def _is_RR(self, x):
        """
        Check if the node x is in a Right-Right configuration.

        :param x: The node to check.
        :return: True if x is in a Right-Right configuration, otherwise False.
        """
        return x == x.parent.right and x.parent == x.parent.parent.right

    def _handle_LR(self, x):
        """
        Handle a Left-Right rotation for the node x.

        :param x: The node to rotate.
        :return: The node after rotation.
        """
        x = x.parent
        self._left_rotate(x)
        return x

    def _handle_RL(self, x):
        """
        Handle a Right-Left rotation for the node x.

        :param x: The node to rotate.
        :return: The node after rotation.
        """
        x = x.parent
        self._right_rotate(x)
        return x

    def _handle_LL(self, x):
        """
        Handle a Left-Left rotation for the node x.

        :param x: The node to rotate.
        """
        x.parent.color = Color.BLACK
        x.parent.parent.color = Color.RED
        self._right_rotate(x.parent.parent)

    def _handle_RR(self, x):
        """
        Handle a Right-Right rotation for the node x.

        :param x: The node to rotate.
        """
        x.parent.color = Color.BLACK
        x.parent.parent.color = Color.RED
        self._left_rotate(x.parent.parent)

    def _recolor(self, parent, uncle, grandparent):
        """
        Recolor the nodes during insertion to maintain Red-Black Tree properties.

        :param parent: The parent node.
        :param uncle: The uncle node.
        :param grandparent: The grandparent node.
        """
        parent.color = Color.BLACK
        uncle.color = Color.BLACK
        grandparent.color = Color.RED

    def _insert(self, new_node):
        """
        Insert a new node into the tree.

        :param new_node: The new node to be inserted.
        :return: The result of adding the new node as a child.
        """
        parent_node = self._find_last(new_node.key)
        return parent_node.add_child(new_node)

    def _find_last(self, value):
        """
        Find the last node in the path where the new node should be added.

        :param value: The value to be added.
        :return: The last node in the path where the new node should be added.
        """
        current = self.root
        prev = None
        while current is not None:
            if value < current.key:
                prev = current
                current = current.left
            elif value > current.key:
                prev = current
                current = current.right
            else:
                return current
        return prev

    def _left_rotate(self, x):
        """
        Perform a left rotation on the node x.

        :param x: The node to rotate.
        """
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        """
        Perform a right rotation on the node x.

        :param x: The node to rotate.
        """
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, value):
        """
        Find a node with the given value in the binary search tree.

        :param value: The value to search for in the tree.
        :return: The node with the specified value, or None if not found.
        """
        current = self.root
        while current is not None:
            if value < current.key:
                current = current.left
            elif value > current.key:
                current = current.right
            else:
                return current.key
        return None

    def traverse(self):
        """
        Perform an in-order traversal of the tree and print the value of each node.
        """

        def _in_order_traversal(node):
            if node is not None:
                _in_order_traversal(node.left)
                print(node.key)
                _in_order_traversal(node.right)

        _in_order_traversal(self.root)

    def _print_tree(self, node=None, level=0):
        """
        Print a description of the tree structure for debugging purposes.

        :param node: The current node to print, defaults to the root.
        :param level: The current level in the tree, defaults to 0.
        """
        if node is None:
            node = self.root

        description = f"Level {level}: Node {node.key} ({node.color.name})"
        if node.parent:
            description += f", Parent {node.parent.key}"
        if node.left:
            description += f", Left Child {node.left.key}"
        if node.right:
            description += f", Right Child {node.right.key}"

        print(description)

        if node.left is not None:
            self._print_tree(node.left, level + 1)
        if node.right is not None:
            self._print_tree(node.right, level + 1)
