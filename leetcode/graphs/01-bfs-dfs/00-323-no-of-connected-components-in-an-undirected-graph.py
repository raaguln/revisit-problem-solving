'''
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

323. Number of Connected Components in an Undirected Graph

You have a graph of n nodes. You are given an integer n and an array edges 
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.
'''


'''
Time Complexity: O(n + e)
Building the adjacency list: O(e) for e edges.
DFS traversal:
- Each node is visited once: O(n)
- Each edge is considered twice (once from each node in an undirected graph): O(2e) ⇒ still O(e).

Total time complexity: O(n + e), where n = number of nodes, e = number of edges.

Space Complexity: O(n + e)
Adjacency list: stores each edge twice ⇒ O(e) space.
Visited set: up to n nodes ⇒ O(n)
Call stack (DFS recursion): up to O(n) in the worst case (if the graph is a single chain).

Total space complexity: O(n + e)
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list (undirected)
        adjacency_list = defaultdict(list)
        for n1, n2 in edges:
            adjacency_list[n1].append(n2)
            adjacency_list[n2].append(n1)

        visited = set()
        connected_components = 0

        def dfs(node):
            for neighbor in adjacency_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        # For each node, perform DFS and find CC
        for node in range(n):
            if node in visited:
                continue
            visited.add(node)
            connected_components += 1
            dfs(node)

        return connected_components

'''
Disjoint Set Union (by rank)
Time Complexity: O(E * α(n))
- With path compression + union by rank/size:
    Amortized O(α(n)) per union/find (α = inverse Ackermann, practically constant)
- For E edges: O(E * α(n))

Space Complexity: O(n)
- Stores arrays parent[] and rank[] or size[] of size n:
'''
import numpy as np
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # parent, rank
        parent = [i for i in range(n)]
        rank = [1] * n

        # returns the root of the group to which x belongs
        # very slow growing, runs in practically constant time
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # tries to merge the groups of x and y
        def union(x, y):
            # Find roots
            rootX, rootY = find(x), find(y)

            # Already in same group
            if rootX == rootY:
                return False

            # Merge smaller tree into bigger tree
            if rank[rootX] > rank[rootY]:
                # Y is a smaller tree, merge into X
                parent[rootY] = rootX
            else:
                # X is a smaller tree, merge into Y
                parent[rootX] = rootY
                rank[rootX] += 1
            return True

        # Each node starts off as its own component
        # total components = n when we start
        connected_components = n
        for u, v in edges:
            # Only decrement when a new merge happens
            if union(u, v):
                connected_components -= 1  
        return connected_components


'''
Disjoint Set Union (by size)
Time Complexity: O(E * α(n))
- With path compression + union by size:
    Amortized O(α(n)) per union/find (α = inverse Ackermann, practically constant)
- For E edges: O(E * α(n))

Space Complexity: O(n)
- Stores arrays parent[] and size[] of size n:
'''
import numpy as np
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # parent, size
        parent = [i for i in range(n)]
        size = [1] * n
        
        # returns the root of the group to which x belongs
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # tries to merge the groups of x and y
        def union(x, y):
            rootX, rootY = find(x), find(y)
            # 1. Already in the same group
            if rootX == rootY:
                return False
            
            # 2. Merge the smaller tree into the larger one (via size)
            # X is a smaller tree, merge into Y
            if size[rootX] < size[rootY]:
                parent[rootX] = rootY
                size[rootY] += size[rootX]
            # Equal heights or Y is smaller the smaller tree - merge into X
            else:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            return True

        connected_components = n
        for u, v in edges:
            # Only decrement when a new merge happens
            if union(u, v):
                connected_components -= 1  
        return connected_components