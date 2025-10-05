'''
https://leetcode.com/problems/number-of-operations-to-make-network-connected/submissions/1660731339/

Time - O(m) - m is no of edges
find operation: Amortized almost O(1) (Inverse Ackermann function, practically constant).
union operation: Also amortized almost O(1).

'''

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        # If there are fewer connections than n-1, it's impossible to connect all computers
        if len(connections) < n - 1:
            return -1
        
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            
            # Union by rank (attach smaller tree under larger tree)
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True

        connected_components = n

        for u, v in connections:
            if union(u, v):
                connected_components -= 1
        
        # To connect all components, need (connected_components - 1) operations
        return connected_components - 1
