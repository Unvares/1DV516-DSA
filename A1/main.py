from tests.singly_linked_list import test_singly_linked_list
from tests.doubly_linked_list import test_doubly_linked_list


if __name__ == "__main__":
    print("=" * 40)
    print("Running Singly Linked List Tests")
    print("=" * 40)

    test_singly_linked_list()

    print("\n" + "=" * 40)
    print("Running Doubly Linked List Tests")
    print("=" * 40)
    test_doubly_linked_list()

    print("\n" + "=" * 40)
    print("All tests passed.")
    print("=" * 40)
