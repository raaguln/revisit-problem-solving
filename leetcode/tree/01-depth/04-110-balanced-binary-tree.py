# https://leetcode.com/problems/balanced-binary-tree/
'''
Time - O(n)
- Each node is visited once in the DFS traversal
- n is the number of nodes in the tree

Space - O(h)
- h is the height of the tree, representing the maximum recursion depth
- In the worst case (skewed tree), h can be n
- In the best case (balanced tree), h is O(log n)
- Space is used by the call stack due to recursion
'''
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
