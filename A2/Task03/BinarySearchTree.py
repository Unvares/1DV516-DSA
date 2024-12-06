class BinarySearchTree:
    def __init__(self, root=None, parent=None, left=None, right=None):
        """
        Initialize a binary tree node.

        :param root: The value or key of the node.
        :param parent: The parent node of the current node.
        :param left: The left child of the current node.
        :param right: The right child of the current node.
        """
        self.root = root
        self.parent = parent
        self.left = left
        self.right = right

    def insert(self, value):
        """
        Add a new node with the given value to the binary search tree.

        :param value: The value or key of the node to be added.
        :return: True if the node was added successfully, False if the node already exists.
        """
        if self.root is None:
            self.root = value
            return True

        parent_node = self._find_last(value)
        return self._add_child(
            parent_node, BinarySearchTree(root=value, parent=parent_node)
        )

    def _find_last(self, value):
        """
        Find the last node in the path where the new node should be added.

        :param value: The value or key of the node to be added.
        :return: The last node in the path where the new node should be added.
        """
        current = self
        prev = None
        while current is not None:
            if value < current.root:
                prev = current
                current = current.left
            elif value > current.root:
                prev = current
                current = current.right
            else:
                return current
        return prev

    def _add_child(self, parent_node, new_node):
        """
        Add a new node as a child of the specified parent node.

        :param parent_node: The parent node to which the new node will be added.
        :param new_node: The new node to be added.
        :return: True if the node was added successfully, False if the node already exists.
        """
        if parent_node is None:
            self.root = new_node.root
            self.left = new_node.left
            self.right = new_node.right
            return True
        elif new_node.root < parent_node.root:
            parent_node.left = new_node
            return True
        elif new_node.root > parent_node.root:
            parent_node.right = new_node
            return True
        else:
            return False

    def depth(self):
        """
        Calculate the depth of the node in the tree.

        :return: The depth of the node, which is the number of edges
                 from the node to the tree's root node.
        """
        count = 0
        current = self.parent
        while current is not None:
            current = current.parent
            count += 1
        return count

    def height(self):
        """
        Calculate the height of the subtree rooted at the current node.

        :return: The height of the subtree, which is the number of edges
                 on the longest path from the node to a leaf.
        """
        left_height = self.left.height() if self.left else -1
        right_height = self.right.height() if self.right else -1
        return 1 + max(left_height, right_height)

    def is_leaf(self):
        """
        Check if the node is a leaf node.

        :return: True if the node is a leaf (has no children), False otherwise.
        """
        return self.left is None and self.right is None

    def search(self, value):
        """
        Find a node with the given value in the binary search tree.

        :param value: The value to search for in the tree.
        :return: The node with the specified value, or None if not found.
        """
        current = self
        while current is not None:
            if value < current.root:
                current = current.left
            elif value > current.root:
                current = current.right
            else:
                return current.root
        return None

    def size(self):
        """
        Calculate the total number of nodes in the subtree rooted at
        the current node.

        :return: The size of the subtree.
        """
        if self.root is None:
            return 0
        size = 1
        if self.left is not None:
            size += self.left.size()
        if self.right is not None:
            size += self.right.size()
        return size

    def traverse(self):
        """
        Perform an in-order traversal of the subtree rooted at the
        current node and print the value of each node.
        """
        if self.root is None:
            return
        if self.left is not None:
            self.left.traverse()
        print(self.root)
        if self.right is not None:
            self.right.traverse()
