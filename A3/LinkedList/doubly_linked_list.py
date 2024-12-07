from .linked_list_base import LinkedList, LLNode


class DLLNode(LLNode):
    def __init__(self, value):
        """
        Initializes a node in a doubly linked list.

        Args:
            value: The value to be stored in the node.
        """
        super().__init__(value)
        self.next = None
        self.prev = None

    def __repr__(self):
        """
        Returns a string representation of the node.

        Returns:
            str: A string representation of the node.
        """
        return str(self.value) + " next-" + str(self.next) + " prev-" + str(self.prev)


class DoublyLinkedList(LinkedList):
    def __init__(self):
        """
        Initializes an empty doubly linked list.
        """
        super().__init__()
        self.tail = None

    def insert(self, value, index=None):
        """
        Inserts a value into the doubly linked list at a specified index.

        Args:
            value: The value to insert.
            index (int, optional): The index at which to insert the value. If None or out of bounds, inserts at the tail.
        """
        if index is not None and index < 0:
            raise IndexError("Negative index encountered")
        if index is None or index >= self.count:
            self._insert_at_tail(value)
        else:
            self._insert_by_index(value, index)
        self.count += 1

    def _insert_at_tail(self, value):
        """
        Inserts a value at the tail of the doubly linked list.

        Args:
            value: The value to insert.
        """
        new_node = DLLNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = self.tail.next

    def _insert_by_index(self, value, index):
        """
        Inserts a value at a specified index in the doubly linked list.

        Args:
            value: The value to insert.
            index (int): The index at which to insert the value.
        """
        new_node = DLLNode(value)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node

    def delete(self, node=None, value=None, index=None):
        """
        Deletes a node from the doubly linked list by node, value, or index.

        Args:
            node (optional): The node to delete.
            value (optional): The value to delete.
            index (int, optional): The index of the value to delete.
        """
        if self.head is None:
            raise ValueError("List is empty")
        if self.count == 1:
            self.head = None
            self.tail = None
            self.count = 0
            return
        if node is not None:
            self._delete_by_node(node)
        elif index is not None:
            if index < 0 or index >= self.count:
                raise IndexError("Index out of bounds")
            self._delete_by_index(index)
        elif value is not None:
            self._delete_by_value(value)
        else:
            raise ValueError("Either node, value, or index must be provided")

    def _delete_by_node(self, node):
        """
        Deletes a specified node in the doubly linked list.

        Args:
            node: The node to delete.
        """
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        self.count -= 1

    def _delete_by_index(self, index):
        """
        Deletes a node at a specified index in the doubly linked list.

        Args:
            index (int): The index of the node to delete.
        """
        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self.count -= 1
            return

        current = self.head
        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current.next is not None:
            current.next = current.next.next
            if current.next is not None:
                current.next.prev = current
            self.count -= 1

    def _delete_by_value(self, value):
        """
        Deletes a node with a specified value in the doubly linked list.

        Args:
            value: The value of the node to delete.
        """
        if self.head.value == value:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self.count -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is not None:
                    current.next.prev = current
                self.count -= 1
                return
            current = current.next
        raise ValueError("Value not found in the list")

    def rotate(self, r):
        """
        Rotates the doubly linked list by r positions.

        Args:
            r (int): The number of positions to rotate the list.
        """
        if self.head is None:
            raise ValueError("List is empty")
        if r < 0:
            raise ValueError("Rotation count must be a positive integer")
        if self.head == self.tail:
            raise ValueError("List contains only one element")
        r = r % self.count
        if r == 0:
            return

        new_tail = self.head
        for _ in range(r - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        self.head.prev = self.tail
        self.tail.next = self.head

        new_tail.next = None
        new_head.prev = None
        self.head = new_head
        self.tail = new_tail

    def reverse(self):
        """
        Reverses the doubly linked list.
        """
        if self.head is None:
            raise ValueError("List is empty")

        current = self.head
        while current is not None:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = temp

        self.head, self.tail = self.tail, self.head
