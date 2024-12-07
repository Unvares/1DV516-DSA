def selection_sort(list):
    """
    Sorts a linked list using the selection sort algorithm.

    This function iterates over the linked list, selecting the minimum element
    from the unsorted portion and swapping it with the first unsorted element.

    Args:
        list: A linked list
    """
    if len(list) < 2:
        return
    curr = list.head
    for i in range(list.count):
        min_node = curr
        curr_compare = curr.next
        for j in range(i + 1, list.count):
            if curr_compare.value < min_node.value:
                min_node = curr_compare
            curr_compare = curr_compare.next
        curr.value, min_node.value = min_node.value, curr.value
        curr = curr.next


def print_list(list):
    """
    Prints the elements of a linked list in order.

    This function traverses the linked list from the head to the end,
    printing each element's value followed by an arrow.

    Args:
        list: A linked list object
    """
    current = list.head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
