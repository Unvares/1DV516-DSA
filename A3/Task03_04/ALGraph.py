class ALGraph:
    def __init__(self, n):
        """
        Initializes an adjacency list graph with n nodes.

        Args:
            n (int): The number of nodes in the graph.
        """
        self.adj = [[] for i in range(n)]

    def addNode(self, u):
        """
        Adds a node to the graph. If the node index is greater than the current
        size of the adjacency list, it extends the list. If the node already
        exists but is marked as None, it reinitializes it.

        Args:
            u (int): The index of the node to add.
        """
        if u >= len(self.adj):
            self.adj.append([])
        elif self.adj[u] is None:
            self.adj[u] = []

    def addEdge(self, u, v):
        """
        Adds an undirected edge between nodes u and v.

        Args:
            u (int): The index of the first node.
            v (int): The index of the second node.

        Raises:
            IndexError: If either node index is out of boundaries.
        """
        if (u < 0 or u >= len(self.adj)) or (v < 0 or v >= len(self.adj)):
            raise IndexError("Node index out of boundaries")
        if self.hasNode(u) and self.hasNode(v) and not self.hasEdge(u, v):
            self.adj[u].append(v)
            self.adj[v].append(u)

    def removeNode(self, u):
        """
        Removes a node from the graph by setting its adjacency list to None.

        Args:
            u (int): The index of the node to remove.
        """
        if u < len(self.adj):
            self.adj[u] = None

    def removeEdge(self, u, v):
        """
        Removes an undirected edge between nodes u and v.

        Args:
            u (int): The index of the first node.
            v (int): The index of the second node.

        Raises:
            IndexError: If either node index is out of boundaries.
        """
        if (u < 0 or u >= len(self.adj)) or (v < 0 or v >= len(self.adj)):
            raise IndexError("Node index out of boundaries")
        if self.hasEdge(u, v):
            self.adj[u].remove(v)
            self.adj[v].remove(u)

    def hasNode(self, u):
        """
        Checks if a node exists in the graph.

        Args:
            u (int): The index of the node to check.

        Returns:
            bool: True if the node exists, False otherwise.
        """
        if u < len(self.adj):
            return self.adj[u] is not None
        return False

    def hasEdge(self, u, v):
        """
        Checks if an undirected edge exists between nodes u and v.

        Args:
            u (int): The index of the first node.
            v (int): The index of the second node.

        Returns:
            bool: True if the edge exists, False otherwise.
        """
        if self.hasNode(u) and self.hasNode(v):
            return v in self.adj[u]
        return False

    def DFS(self, u, v, visited=[]):
        """
        Performs a Depth-First Search (DFS) from node v to node u.

        Args:
            u (int): The target node index.
            v (int): The starting node index.
            visited (list, optional): The list of visited nodes. Defaults to an empty list.

        Returns:
            list: The list of visited nodes if the target node is found.
            bool: False if the target node is not found.
        """
        visited.append(v)

        if v == u:
            return visited

        for vertex in self.adj[v]:
            if vertex not in visited:
                if self.DFS(u, vertex, visited.copy()):
                    return True

        return False
