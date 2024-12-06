class BinaryTree:
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

    def insert(self, value):
        """
        Insert a new node with the given value into the binary tree
        using level-order insertion.

        :param value: The value or key of the node to be inserted.
        :return: False if a duplicate value is found, otherwise True.
        """
        if self.root is None:
            self.root = value
            return True

        queue = [self]

        while queue:
            current = queue.pop(0)
            if current.root == value:
                return False
            if current.left is None:
                current.left = BinaryTree(root=value, parent=current)
                return True
            else:
                queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(root=value, parent=current)
                return True
            else:
                queue.append(current.right)

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
