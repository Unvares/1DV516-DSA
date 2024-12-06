from Color import Color


class RBNode:
    def __init__(self, key=None, parent=None, left=None, right=None, color=Color.RED):
        """
        Initialize a red-black tree node.

        :param key: The value or key of the node.
        :param parent: The parent node of the current node.
        :param left: The left child of the current node.
        :param right: The right child of the current node.
        :param color: The color of the node, default is red.
        """
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    def add_child(self, new_node):
        """
        Add a new node as a child of the current node.

        :param new_node: The new node to be added.
        :return: True if the node was added successfully, False if the node already exists.
        """
        if new_node.key < self.key:
            self.left = new_node
            new_node.parent = self
            return True
        elif new_node.key > self.key:
            self.right = new_node
            new_node.parent = self
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

    def size(self):
        """
        Calculate the total number of nodes in the subtree rooted at
        the current node.

        :return: The size of the subtree.
        """
        size = 1
        if self.left is not None:
            size += self.left.size()
        if self.right is not None:
            size += self.right.size()
        return size
