from abc import ABC, abstractmethod


class LinkedList(ABC):
    """
    Abstract base class for a linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None
        self.count = 0

    def __len__(self):
        """
        Returns the number of elements in the linked list.
        """
        return self.count

    def empty(self):
        """
        Checks if the linked list is empty.

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.head is None

    def search(self, value):
        """
        Searches for a value in the linked list.

        Args:
            value: The value to search for.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        if value is None:
            raise ValueError("Search value cannot be None")
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def get(self, index):
        """
        Retrieves the value at a specific index in the linked list.

        Args:
            index (int): The index of the value to retrieve.

        Returns:
            The value at the specified index, or None if the index is out of bounds.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    @abstractmethod
    def insert(self, value, index):
        """
        Inserts a value into the linked list at a specified index.

        Args:
            value: The value to insert.
            index (int): The index at which to insert the value.
        """
        pass

    @abstractmethod
    def delete(self, value, index):
        """
        Deletes a value from the linked list by value or index.

        Args:
            value: The value to delete.
            index (int): The index of the value to delete.
        """
        pass


class LLNode(ABC):
    """
    Abstract base class for a node in a linked list.
    """

    def __init__(self, value):
        """
        Initializes a node with a given value.

        Args:
            value: The value to store in the node.
        """
        if value is None:
            raise ValueError("Node value cannot be None")
        self.value = value

    @abstractmethod
    def __repr__(self):
        """
        Returns a string representation of the node.
        """
        pass
