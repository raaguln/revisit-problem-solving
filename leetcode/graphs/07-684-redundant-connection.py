# https://leetcode.com/problems/redundant-connection/description/
'''
Disjoint Set Union (by size)
Time Complexity: O(E * α(n))
- With path compression + union by rank/size:
    Amortized O(α(n)) per union/find (α = inverse Ackermann, practically constant)
- For E edges: O(E * α(n))

Space Complexity: O(n)
- Stores arrays parent[] and rank[] or size[] of size n:
'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        - The edge to be removed - is redundant edge
        - redundant edge - connects two nodes that are already connected
          through a longer route
        - how do we detect it? Union Find
            - everytime we process an edge, we decrease components
              from n
            - we reach reach tree status when component=1
            - edge after that - gets triggered in the `rootX == rootY`
              because those two nodes are already connected
            - in graph -> it ends up forming the loop (redundant connection)
        '''
        n = len(edges) + 1
        parent = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            # Already connected
            if rootX == rootY:
                return False

            # Add connection
            if size[rootX] < size[rootY]:
                parent[rootX] = rootY
                size[rootY] += size[rootX]
            else:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
