# Time: O(n)
# Space: O(logn) - recursive stack
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        acceptableDiff = True
        def dfs(node):
            if not node:
                return 0
            nonlocal acceptableDiff
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left - right) > 1:
                acceptableDiff = False
            return 1 + max(left, right)
        
        dfs(root)
        return acceptableDiff
