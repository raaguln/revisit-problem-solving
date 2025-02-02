# 1. DFS recursion
# Time: O(n)
# Space: O(logn) - recursive stack
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            return 1 + max(
                dfs(node.left),
                dfs(node.right)
            )

        height = dfs(root)
        return height

# DFS Better code
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxLeft = self.maxDepth(root.left)
        maxRight = self.maxDepth(root.right)
        return 1 + max(maxLeft, maxRight)
    
# BFS
# Time: O(n)
# Space: O(k) where k is the maximum number of nodes at a level
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        maxDepth = 0
        while stack:
            node, depth = stack.pop()
            if not node:
                continue
            maxDepth = max(maxDepth, depth)
            stack.extend([
                [node.left, depth + 1],
                [node.right, depth + 1],
            ])
        return maxDepth
            