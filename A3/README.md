# 1DV516 A3

Name: Rihards Okmanis  
Email: ro222ij@student.lnu.se

I copied the list classes from A1 directly into the A3/LinkedList/ directory.

To run the tests, execute them as Python modules from the root directory using the following commands:

- `python -m Task01.test`
- `python -m Task02.test`
- `python -m Task03_04.test`

Note: Running a Python file using VSCode UI won't work due to how Python handles relative imports.

# Task 01

I chose to swap values instead of pointers because it's a simpler approach, leading to a consistent implementation for both singly and doubly linked lists.

# Task 02

I explored both Lomuto and Hoare partitioning methods and chose to implement Hoare partitioning for the following reasons:

- It offers better learning outcomes for this assignment due to being more complex and less intuitive
- It has a better time complexity than Lomuto partitioning, thus being a more attractive choice from an algorithmical perspective.

For pivot selection, I used the median-of-three approach, which is generally efficient for this sorting algorithm. However, it's important to note that while this method has O(1) complexity for arrays, it results in O(n) complexity for linked lists due to the need to traverse to the middle of the list to find the median value. The only way to avoid this, to my knowledge, is by using merge sort, which is more compatible with linked lists. Despite the O(n) time complexity for pivot selection, I believe it's worthwhile as it reduces the overall algorithmic complexity from O(n^2) to O(n*log(n)). Even in the best-case scenario for quick sort, the algorithmic complexity remains greater than O(n), so this can be overlooked. I believe this holds true for small datasets as well, as the reduction from O(n^2) to O(n*log(n)) is still beneficial.

# Task 03

For this task, I chose an adjacency list for the following reasons:

- While an edge list offers slightly better space complexity, its algorithmic complexity is less favorable.
- Edge list implementations are not ideal for search algorithms because they lack a sequential representation of relationships between vertices. You can't start at a vertex and traverse through its edges; instead, you must examine every edge in the graph to find those connected to the current vertex, making the time complexity for search algorithms unattractive.

Let's also consider an adjacency matrix. Adjacency matrices work well for dense graphs. However, since the assignment doesn't specify whether the graphs are dense or sparse, we should efficiently handle both types. An adjacency list is a good compromise for this. Moreover, adjacency matrices have poor time complexity for search algorithms. Like traversing an entire edge list, we would need to check every vertex at each step. This results in a complexity of O(V^2) because the matrix allocates memory for all possible edges, not just the existing ones, leading to unnecessary checks when edges don't exist.
