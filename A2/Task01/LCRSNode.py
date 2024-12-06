class LCRSNode:
    def __init__(self, key=None, leftChild=None, rightSibling=None):
        """
        Initialize a node in the Left-Child Right-Sibling (LCRS) tree.

        :param key: The value or key of the node.
        :param leftChild: The left child of the node.
        :param rightSibling: The right sibling of the node.
        """
        self.key = key
        self.leftChild = leftChild
        self.rightSibling = rightSibling

    def add_child(self, key):
        """
        Add a child node with the given key to the current node.

        :param key: The value or key of the child node to be added.
        :return: The newly added child node.
        """
        if self.leftChild is None:
            self.leftChild = LCRSNode(key)
            return self.leftChild
        else:
            current = self.leftChild
            while current.rightSibling is not None:
                current = current.rightSibling
            current.rightSibling = LCRSNode(key)
            return current.rightSibling

    def degree(self):
        """
        Return the degree of the node, which is the number of its immediate children.

        :return: The degree of the node.
        """
        counter = 0
        current = self.leftChild
        while current is not None:
            counter += 1
            current = current.rightSibling
        return counter

    def height(self):
        """
        Return the height of the subtree rooted at the current node.

        :return: The height of the subtree.
        """
        if self.is_leaf():
            return 0
        else:
            current = self.leftChild
            max_height = 0
            while current is not None:
                max_height = max(max_height, current.height())
                current = current.rightSibling
            return 1 + max_height

    def is_leaf(self):
        """
        Check if the node is a leaf node (i.e., it has no children).

        :return: True if the node is a leaf, False otherwise.
        """
        return self.leftChild is None

    def size(self):
        """
        Return the size of the subtree rooted at the current node,
        which is the total number of nodes in the subtree.

        :return: The size of the subtree.
        """
        size = 1
        current = self.leftChild
        while current:
            size += current.size()
            current = current.rightSibling
        return size

    def walk(self):
        """
        Perform a pre-order traversal of the subtree rooted at
        the current node, printing the key of each node.
        """
        print(self.key)
        if self.leftChild is not None:
            self.leftChild.walk()
        if self.rightSibling is not None:
            self.rightSibling.walk()
