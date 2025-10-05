'''
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

key insight is that stones connected by row or column form connected components, 
and the maximum stones removable is total stones minus number of connected components.

Because row and column values both come from the same integer range 
(e.g., 0 to 10,000), just using x and y directly as node ids would 
cause collisions — for example, row 3 and column 3 would both be 
represented as 3, causing ambiguity.

Time - O(M) - m is edges
'''

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        n = len(stones)
        
        parent = {}
        rank = {}
        
        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            
            if rank.get(rootX, 0) > rank.get(rootY, 0):
                parent[rootY] = rootX
            elif rank.get(rootX, 0) < rank.get(rootY, 0):
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] = rank.get(rootX, 0) + 1
            return True
        
        # Important trick:
        # Use "row" and "col + 10000" as unique ids to avoid collision
        # This way, stones on same row or same column get unioned correctly
        for x, y in stones:
            union(x, y + 10000)
        
        # Count unique connected components roots
        # collects all distinct root parents of both row nodes and column nodes into one set.
        unique_roots = set()
        for x, y in stones:
            unique_roots.add(find(x))
            unique_roots.add(find(y + 10000))
        
        # Number of stones removable = total stones - number of connected components
        return n - len(unique_roots)
