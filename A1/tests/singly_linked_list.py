from singly_linked_list import SinglyLinkedList


def test_singly_linked_list():
    print("Testing SinglyLinkedList")

    # Test insert at tail
    print("Testing insert at tail")
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    print("Inserted values: 1, 2, 3")
    assert sll.get(0).value == 1, "Failed at insert at tail: index 0"
    assert sll.get(1).value == 2, "Failed at insert at tail: index 1"
    assert sll.get(2).value == 3, "Failed at insert at tail: index 2"
    assert sll.get(0).next == sll.get(1), "Failed at insert at tail: next link 0->1"
    assert sll.get(1).next == sll.get(2), "Failed at insert at tail: next link 1->2"
    assert sll.get(2).next is None, "Failed at insert at tail: next link 2->None"

    print()

    # Test insert at index
    print("Testing insert at index")
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.insert(4, 1)
    print("Inserted values: 1, 2, 3, and 4 at index 1")
    assert sll.get(1).value == 4, "Failed at insert at index: index 1"
    assert sll.get(2).value == 2, "Failed at insert at index: index 2"
    assert sll.get(0).next == sll.get(1), "Failed at insert at index: next link 0->1"
    assert sll.get(1).next == sll.get(2), "Failed at insert at index: next link 1->2"
    assert sll.get(2).next == sll.get(3), "Failed at insert at index: next link 2->3"

    print()

    # Test delete by value
    print("Testing delete by value")
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.insert(4)
    sll.delete(value=4)
    print("Deleted value: 4")
    assert sll.search(4) is False, "Failed at delete by value: search 4"
    assert sll.get(2).value == 3, "Failed at delete by value: index 2"
    assert sll.get(2).next is None, "Failed at delete by value: next link 2->None"

    print()

    # Test delete by index
    print("Testing delete by index")
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.delete(index=1)
    print("Deleted value at index: 1")
    assert sll.get(1).value == 3, "Failed at delete by index: index 1"
    assert sll.get(0).next == sll.get(1), "Failed at delete by index: next link 0->1"

    print()

    # Test delete by node (head)
    print("Testing delete by node (head)")
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    node_to_delete = sll.get(0)
    sll.delete(node=node_to_delete)
    print("Deleted head node")
    assert sll.get(0).value == 2, "Failed at delete by node (head): index 0"
    assert sll.get(0).next == sll.get(
        1
    ), "Failed at delete by node (head): next link 0->1"

    print()

    # Test delete by node (tail)
    print("Testing delete by node (tail)")
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.insert(4)
    node_to_delete = sll.get(3)
    sll.delete(node=node_to_delete)
    print("Deleted tail node")
    assert sll.get(2).value == 3, "Failed at delete by node (tail): index 2"
    assert sll.get(2).next is None, "Failed at delete by node (tail): next link 2->None"

    print()

    # Test delete by node (middle)
    print("Testing delete by node (middle)")
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    sll.insert(4)
    node_to_delete = sll.get(1)
    sll.delete(node=node_to_delete)
    print("Deleted middle node at index 1")
    assert sll.get(1).value == 3, "Failed at delete by node (middle): index 1"
    assert sll.get(0).next == sll.get(
        1
    ), "Failed at delete by node (middle): next link 0->1"
    assert sll.get(1).next == sll.get(
        2
    ), "Failed at delete by node (middle): next link 1->2"

    print()

    # Test search
    print("Testing search")
    sll = SinglyLinkedList()
    sll.insert(1)
    sll.insert(2)
    sll.insert(3)
    print("Inserted values: 1, 2, 3")
    assert sll.search(1) is True, "Failed at search: value 1"
    assert sll.search(4) is False, "Failed at search: value 4"

    print()

    # Test empty
    print("Testing empty")
    sll = SinglyLinkedList()
    assert sll.empty() is True, "Failed at empty: list should be empty"
    sll.insert(1)
    sll.insert(2)
    sll.delete(index=0)
    sll.delete(index=0)
    print("Inserted values: 1, 2 and then deleted both")
    assert sll.empty() is True, "Failed at empty: list should be empty after deletions"

    print()

    # Test __len__
    print("Testing __len__")
    sll = SinglyLinkedList()
    assert len(sll) == 0, "Failed at __len__: length should be 0"
    sll.insert(1)
    sll.insert(2)
    print("Inserted values: 1, 2")
    assert len(sll) == 2, "Failed at __len__: length should be 2"
    sll.delete(index=0)
    assert len(sll) == 1, "Failed at __len__: length should be 1 after deletion"

    print()
