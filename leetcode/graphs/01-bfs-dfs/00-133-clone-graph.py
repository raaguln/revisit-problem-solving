"""
https://leetcode.com/problems/clone-graph/

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        newNodes = {}

        def dfs(node):
            if not node:
                return None
            if node in newNodes:
                return newNodes[node]
            
            # Create copy and update dictionary
            copy = Node(node.val)
            newNodes[node] = copy

            # Update neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)