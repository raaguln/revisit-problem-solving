# https://leetcode.com/problems/diameter-of-binary-tree/
# DFS
# Time: O(n)
# Space: O(logn) - recursive stack
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal maxDiameter
            left = dfs(node.left)
            right = dfs(node.right)
            maxDiameter = max(maxDiameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return maxDiameter
    
# BFS
