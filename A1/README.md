# 1DV516 A1

Name: Rihards Okmanis  
Email: ro222ij@student.lnu.se

I created a base abstract class for both the linked list and the linked list node, which includes the following methods:

- `search`
- `get`
- `empty`
- `__len__`

Next, I implemented the singly linked list and doubly linked list, each with the following methods:

- `insert`
- `delete`

Finally, I added two methods specifically for the doubly linked list as required by the assignment:

- `rotate`
- `reverse`

To enhance clarity and organization, I separated the classes and methods into different files and included docstrings.

## Task 1

This method shifts all values in a doubly linked list by `r`, wrapping elements that get shifted beyond the bounds. It updates the current head and tail pointers to connect the end and the beginning of the list, then shifts the `self.head` and `self.tail` pointers by `r` and breaks the list there.

To calculate runtime, I copied the code from `doubly_linked_list.py` and added comments describing the number of operations required for each line.

Most operations are constant, with only the loop traversing to the new tail being dependent on the input size. Big O runtime focuses on the dominant term as the input size approaches infinity, allowing us to discard constant terms and focus on the main loop.

Before the main loop, `r` is reduced to the list size `n`, and the algorithm runs for any `r` that is not zero. The worst-case scenario is when `r = n - 1`, corresponding to linear growth O(n).

Important! Runtime is not O(r) because `r` is capped to the list size. O(r) plateaus at input size `n`, making the runtime linearly dependent on the list size `n`.

```python
def rotate(self, r):

    if self.head is None:                                               # 1 operation
        raise ValueError("List is empty")                               # 1 operation
    if r < 0:                                                           # 1 operation
        raise ValueError("Rotation count must be a positive integer")   # 1 operation
    if self.head == self.tail:                                          # 1 operation
        raise ValueError("List contains only one element")              # 1 operation
    r = r % self.count                                                  # 1 operation
    if r == 0:                                                          # 1 operation
        return                                                          # 1 operation

    new_tail = self.head                                                # 1 operation
    for _ in range(r - 1):                                              # at max n - 1 operations
        new_tail = new_tail.next                                        # at max n - 1 operations

    new_head = new_tail.next                                            # 1 operation

    self.head.prev = self.tail                                          # 1 operation
    self.tail.next = self.head                                          # 1 operation

    new_tail.next = None                                                # 1 operation
    new_head.prev = None                                                # 1 operation
    self.head = new_head                                                # 1 operation
    self.tail = new_tail                                                # 1 operation
```

## Task 2, Task 3, Task 4

Tests for these tasks are located in `main.py` alongside tests for the rotate method from task 1.
