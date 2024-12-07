import unittest
from Task01.SelectionSort import selection_sort
from LinkedList.doubly_linked_list import DoublyLinkedList
from LinkedList.singly_linked_list import SinglyLinkedList
import random


class TestSelectionSort(unittest.TestCase):

    def setUp(self):
        self.dll = DoublyLinkedList()
        self.sll = SinglyLinkedList()

    def test_empty_list(self):
        print("Testing selection sort on an empty list")
        selection_sort(self.dll)
        self.assertIsNone(self.dll.head, "The head of an empty list should be None")
        self.assertEqual(len(self.dll), 0, "The length of an empty list should be 0")

        selection_sort(self.sll)
        self.assertIsNone(self.sll.head, "The head of an empty list should be None")
        self.assertEqual(len(self.sll), 0, "The length of an empty list should be 0")
        print("Empty list test passed")

    def test_single_element_list(self):
        print("Testing selection sort on a single-element list")
        self.dll.insert(10)
        selection_sort(self.dll)
        self.assertEqual(
            self.dll.head.value, 10, "The single element should remain unchanged"
        )
        self.assertEqual(len(self.dll), 1, "The length of the list should be 1")

        self.sll.insert(10)
        selection_sort(self.sll)
        self.assertEqual(
            self.sll.head.value, 10, "The single element should remain unchanged"
        )
        self.assertEqual(len(self.sll), 1, "The length of the list should be 1")
        print("Single-element list test passed")

    def test_sorted_list(self):
        print("Testing selection sort on an already sorted list")
        for value in [1, 2, 3, 4, 5]:
            self.dll.insert(value)
            self.sll.insert(value)

        selection_sort(self.dll)
        current = self.dll.head
        for expected_value in [1, 2, 3, 4, 5]:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next

        selection_sort(self.sll)
        current = self.sll.head
        for expected_value in [1, 2, 3, 4, 5]:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next
        print("Sorted list test passed")

    def test_reverse_sorted_list(self):
        print("Testing selection sort on a reverse sorted list")
        for value in [5, 4, 3, 2, 1]:
            self.dll.insert(value)
            self.sll.insert(value)

        selection_sort(self.dll)
        current = self.dll.head
        for expected_value in [1, 2, 3, 4, 5]:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next

        selection_sort(self.sll)
        current = self.sll.head
        for expected_value in [1, 2, 3, 4, 5]:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next
        print("Reverse sorted list test passed")

    def test_unsorted_list(self):
        print("Testing selection sort on an unsorted list")
        for value in [3, 1, 4, 5, 2]:
            self.dll.insert(value)
            self.sll.insert(value)

        selection_sort(self.dll)
        current = self.dll.head
        for expected_value in [1, 2, 3, 4, 5]:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next

        selection_sort(self.sll)
        current = self.sll.head
        for expected_value in [1, 2, 3, 4, 5]:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next
        print("Unsorted list test passed")

    def test_list_with_duplicates(self):
        print("Testing selection sort on a list with duplicates")
        for value in [3, 1, 2, 3, 2, 1]:
            self.dll.insert(value)
            self.sll.insert(value)

        selection_sort(self.dll)
        current = self.dll.head
        for expected_value in [1, 1, 2, 2, 3, 3]:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next

        selection_sort(self.sll)
        current = self.sll.head
        for expected_value in [1, 1, 2, 2, 3, 3]:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next
        print("List with duplicates test passed")

    def test_large_random_list(self):
        print("Testing selection sort on a large list of random numbers")
        random_values = random.sample(range(10000), 1000)
        sorted_values = sorted(random_values)

        for value in random_values:
            self.dll.insert(value)
            self.sll.insert(value)

        selection_sort(self.dll)
        current = self.dll.head
        for expected_value in sorted_values:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next

        selection_sort(self.sll)
        current = self.sll.head
        for expected_value in sorted_values:
            self.assertEqual(
                current.value,
                expected_value,
                f"Expected {expected_value} but got {current.value}",
            )
            current = current.next
        print("Large random list test passed")


if __name__ == "__main__":
    unittest.main(verbosity=2)
