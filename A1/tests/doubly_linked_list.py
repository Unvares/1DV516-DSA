from doubly_linked_list import DoublyLinkedList


def test_doubly_linked_list():
    print("Testing DoublyLinkedList")

    # Test insert at tail
    print("Testing insert at tail")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    print("Inserted values: 1, 2, 3")
    assert dll.get(0).value == 1, "Failed at insert at tail: index 0"
    assert dll.get(1).value == 2, "Failed at insert at tail: index 1"
    assert dll.get(2).value == 3, "Failed at insert at tail: index 2"
    assert dll.get(0).next == dll.get(1), "Failed at insert at tail: next link 0->1"
    assert dll.get(1).next == dll.get(2), "Failed at insert at tail: next link 1->2"
    assert dll.get(2).next is None, "Failed at insert at tail: next link 2->None"
    assert dll.get(1).prev == dll.get(0), "Failed at insert at tail: prev link 1->0"
    assert dll.get(2).prev == dll.get(1), "Failed at insert at tail: prev link 2->1"

    print()

    # Test insert at index
    print("Testing insert at index")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4, 1)
    print("Inserted values: 1, 2, 3, and 4 at index 1")
    assert dll.get(1).value == 4, "Failed at insert at index: index 1"
    assert dll.get(2).value == 2, "Failed at insert at index: index 2"
    assert dll.get(0).next == dll.get(1), "Failed at insert at index: next link 0->1"
    assert dll.get(1).next == dll.get(2), "Failed at insert at index: next link 1->2"
    assert dll.get(2).next == dll.get(3), "Failed at insert at index: next link 2->3"
    assert dll.get(1).prev == dll.get(0), "Failed at insert at index: prev link 1->0"
    assert dll.get(2).prev == dll.get(1), "Failed at insert at index: prev link 2->1"
    assert dll.get(3).prev == dll.get(2), "Failed at insert at index: prev link 3->2"

    print()

    # Test delete by value
    print("Testing delete by value")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    dll.delete(value=4)
    print("Deleted value: 4")
    assert dll.search(4) is False, "Failed at delete by value: search 4"
    assert dll.get(2).value == 3, "Failed at delete by value: index 2"
    assert dll.get(2).next is None, "Failed at delete by value: next link 2->None"

    print()

    # Test delete by index
    print("Testing delete by index")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.delete(index=1)
    print("Deleted value at index: 1")
    assert dll.get(1).value == 3, "Failed at delete by index: index 1"
    assert dll.get(0).next == dll.get(1), "Failed at delete by index: next link 0->1"
    assert dll.get(1).prev == dll.get(0), "Failed at delete by index: prev link 1->0"

    print()

    # Test delete by node (head)
    print("Testing delete by node (head)")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    node_to_delete = dll.get(0)
    dll.delete(node=node_to_delete)
    print("Deleted head node")
    assert dll.get(0).value == 2, "Failed at delete by node (head): index 0"
    assert dll.get(0).next == dll.get(
        1
    ), "Failed at delete by node (head): next link 0->1"
    assert dll.get(1).prev == dll.get(
        0
    ), "Failed at delete by node (head): prev link 1->0"

    print()

    # Test delete by node (tail)
    print("Testing delete by node (tail)")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    node_to_delete = dll.get(3)
    dll.delete(node=node_to_delete)
    print("Deleted tail node")
    assert dll.get(2).value == 3, "Failed at delete by node (tail): index 2"
    assert dll.get(2).next is None, "Failed at delete by node (tail): next link 2->None"

    print()

    # Test delete by node (middle)
    print("Testing delete by node (middle)")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    node_to_delete = dll.get(1)
    dll.delete(node=node_to_delete)
    print("Deleted middle node at index 1")
    assert dll.get(1).value == 3, "Failed at delete by node (middle): index 1"
    assert dll.get(0).next == dll.get(
        1
    ), "Failed at delete by node (middle): next link 0->1"
    assert dll.get(1).next == dll.get(
        2
    ), "Failed at delete by node (middle): next link 1->2"
    assert dll.get(1).prev == dll.get(
        0
    ), "Failed at delete by node (middle): prev link 1->0"
    assert dll.get(2).prev == dll.get(
        1
    ), "Failed at delete by node (middle): prev link 2->1"

    print()

    # Test search
    print("Testing search")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    print("Inserted values: 1, 2, 3")
    assert dll.search(1) is True, "Failed at search: value 1"
    assert dll.search(4) is False, "Failed at search: value 4"

    print()

    # Test empty
    print("Testing empty")
    dll = DoublyLinkedList()
    assert dll.empty() is True, "Failed at empty: list should be empty"
    dll.insert(1)
    dll.insert(2)
    dll.delete(index=0)
    dll.delete(index=0)
    print("Inserted values: 1, 2 and then deleted both")
    assert dll.empty() is True, "Failed at empty: list should be empty after deletions"

    print()

    # Test rotate
    print("Testing rotate")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.rotate(1)
    print("Rotated list by 1 position")
    assert dll.get(0).value == 2, "Failed at rotate: index 0"
    assert dll.get(1).value == 3, "Failed at rotate: index 1"
    assert dll.get(2).value == 1, "Failed at rotate: index 2"
    assert dll.get(0).prev is None, "Failed at rotate: prev link 0->None"
    assert dll.get(0).next == dll.get(1), "Failed at rotate: next link 0->1"
    assert dll.get(1).prev == dll.get(0), "Failed at rotate: prev link 1->0"
    assert dll.get(1).next == dll.get(2), "Failed at rotate: next link 1->2"
    assert dll.get(2).prev == dll.get(1), "Failed at rotate: prev link 2->1"
    assert dll.get(2).next is None, "Failed at rotate: next link 2->None"

    print()

    # Test reverse
    print("Testing reverse")
    dll = DoublyLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.reverse()
    print("Reversed list")
    assert dll.get(0).value == 3, "Failed at reverse: index 0"
    assert dll.get(1).value == 2, "Failed at reverse: index 1"
    assert dll.get(2).value == 1, "Failed at reverse: index 2"
    assert dll.get(0).prev is None, "Failed at reverse: prev link 0->None"
    assert dll.get(0).next == dll.get(1), "Failed at reverse: next link 0->1"
    assert dll.get(1).prev == dll.get(0), "Failed at reverse: prev link 1->0"
    assert dll.get(1).next == dll.get(2), "Failed at reverse: next link 1->2"
    assert dll.get(2).prev == dll.get(1), "Failed at reverse: prev link 2->1"
    assert dll.get(2).next is None, "Failed at reverse: next link 2->None"

    print()

    # Test __len__
    print("Testing __len__")
    dll = DoublyLinkedList()
    assert len(dll) == 0, "Failed at __len__: length should be 0"
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    print("Inserted values: 1, 2, 3")
    assert len(dll) == 3, "Failed at __len__: length should be 3"
    dll.delete(index=0)
    assert len(dll) == 2, "Failed at __len__: length should be 2 after deletion"
    dll.delete(index=0)
    assert len(dll) == 1, "Failed at __len__: length should be 1 after deletion"

    print()
