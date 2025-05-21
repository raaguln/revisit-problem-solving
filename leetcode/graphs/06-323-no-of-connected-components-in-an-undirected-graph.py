# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
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
import numpy as np
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjacency list
        adjacency_list = {i: [] for i in range(n)}
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            if n1 not in adjacency_list:
                adjacency_list[n1] = []
            if n2 not in adjacency_list:
                adjacency_list[n2] = []
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
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # tries to merge the groups of x and y
        def union(x, y):
            rootX, rootY = find(x), find(y)
            # Already in the same group
            if rootX == rootY:
                return False
            
            # Merge the smaller tree into the larger one (via rank)
            
            # X is a smaller tree, merge into Y
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            # Equal heights - merge either
            elif rank[rootX] == rank[rootY]:
                parent[rootY] = rootX
                rank[rootX] += 1
            # Y is a smaller tree, merge into X
            else:
                parent[rootY] = rootX
            return True

        connected_components = n
        for u, v in edges:
            # Only decrement when a new merge happens
            if union(u, v):
                connected_components -= 1  
        return connected_components


'''
Disjoint Set Union (by size)
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
            
            # 2. Merge the smaller tree into the larger one (via rank)
            # X is a smaller tree, merge into Y
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
                rank[rootY] += rank[rootX]
            # Equal heights or Y is smaller the smaller tree - merge into X
            else:
                parent[rootY] = rootX
                rank[rootX] += rank[rootY]
            return True

        connected_components = n
        for u, v in edges:
            # Only decrement when a new merge happens
            if union(u, v):
                connected_components -= 1  
        return connected_components