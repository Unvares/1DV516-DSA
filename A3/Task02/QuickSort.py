from LinkedList.doubly_linked_list import DoublyLinkedList


def quick_sort(list, start=None, end=None, verbose_print=False):
    """
    Sorts a doubly linked list using the quick sort algorithm.

    This function recursively sorts the list by partitioning it around a pivot
    using Hoare's partitioning scheme and sorting the sublists before and after
    the partition point.

    Args:
        list: A doubly linked list to be sorted.
        start: The starting node of the sublist to sort. Defaults to None.
        end: The ending node of the sublist to sort. Defaults to None.
        verbose_print: If True, prints detailed debug information. Defaults to False.
    """
    if list.count < 2:
        return

    if start is None or end is None:
        start = list.head
        end = list.tail

    if start == end:
        return

    partition_node = partition(list, start, end, verbose_print)

    quick_sort(list, start, partition_node, verbose_print=verbose_print)
    quick_sort(list, partition_node.next, end, verbose_print=verbose_print)


def partition(list, start, end, verbose_print=True):
    """
    Partitions the sublist around a pivot using Hoare's partitioning scheme.

    This function rearranges the nodes in the sublist such that all nodes
    with values less than or equal to the pivot come before the partition point,
    and all nodes with values greater than or equal to the pivot come after it.
    It returns the node where the partition is made.

    Args:
        list: The doubly linked list containing the sublist to partition.
        start: The starting node of the sublist.
        end: The ending node of the sublist.
        verbose_print: If True, prints detailed debug information. Defaults to True.

    Returns:
        The node where the partition is made.
    """
    pivot = get_pivot(list, start, end)
    if verbose_print:
        print(
            f"--- Sorting Sublist from {start.value} to {end.value} with pivot {pivot} ---"
        )
        print("Sublist before sorting:")
        sublist = get_sublist(list, start, end)
        print_list(sublist)

    i = start
    j = end

    while True:
        if verbose_print:
            print()
        while i.value < pivot:
            i = i.next
        if verbose_print:
            print(f"Left pointer moved to node with value {i.value}")

        while j.value > pivot:
            j = j.prev
        if verbose_print:
            print(f"Right pointer moved to node with value {j.value}")

        if i == j or i.prev == j:
            if verbose_print:
                print(f"Pointers met. Returning partition node with value {j.value}")
            break

        if i.value == j.value:
            if verbose_print:
                print(f"Duplicate values found with values {i.value}. Skipping swap.")
            i = i.next
            j = j.prev
            continue

        if verbose_print:
            print(f"Swapping nodes with values {i.value} and {j.value}")

        i.value, j.value = j.value, i.value
        i = i.next
        j = j.prev
        if verbose_print:
            print("List after swapping:")
            sublist = get_sublist(list, start, end)
            print_list(sublist)

    if verbose_print:
        print(f"On pivot {pivot}, list after sorting is:")
        print_list(list)
        print()

    return j


def get_pivot(list, start, end):
    """
    Determines the pivot value for the quick sort partitioning.

    This function uses the median-of-three method to select a pivot value
    from the start, middle, and end nodes of the sublist.

    Args:
        list: The doubly linked list containing the sublist.
        start: The starting node of the sublist.
        end: The ending node of the sublist.

    Returns:
        The pivot value.
    """
    middle = get_middle(list, start, end)
    return median_of_three(start.value, middle.value, end.value)


def get_middle(list, start, end):
    """
    Finds the middle node of the sublist.

    This function uses the slow and fast pointer technique to find the middle
    node of the sublist between the start and end nodes.

    Args:
        list: The doubly linked list containing the sublist.
        start: The starting node of the sublist.
        end: The ending node of the sublist.

    Returns:
        The middle node of the sublist.
    """
    slow = start
    fast = start
    while fast != end and fast.next != end:
        slow = slow.next
        fast = fast.next.next
    return slow


def median_of_three(a, b, c):
    """
    Computes the median of three values.

    Args:
        a: The first value.
        b: The second value.
        c: The third value.

    Returns:
        The median value among the three provided.
    """
    return sorted([a, b, c])[1]


def get_sublist(list, start, end):
    """
    Extracts a sublist from the doubly linked list.

    This function creates a new doubly linked list containing the nodes
    from the start to the end node, inclusive.

    Args:
        list: The original doubly linked list.
        start: The starting node of the sublist.
        end: The ending node of the sublist.

    Returns:
        A new doubly linked list containing the sublist.
    """
    sublist = DoublyLinkedList()
    current = start
    while current != end.next:
        sublist.insert(current.value)
        current = current.next
    return sublist


def print_list(list):
    """
    Prints the elements of a doubly linked list in order.

    This function traverses the doubly linked list from the head to the end,
    printing each element's value followed by an arrow.

    Args:
        list: A doubly linked list object.
    """
    current = list.head
    while current is not None:
        print(current.value, end=" -> " if current.next is not None else "")
        current = current.next
    print()
