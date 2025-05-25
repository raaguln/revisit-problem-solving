# https://leetcode.com/problems/diameter-of-binary-tree/
# DFS
'''
Time - O(n)
- Each node is visited exactly once during the DFS traversal
- n is the number of nodes in the tree

Space - O(h)
- h is the height of the tree, representing the maximum recursion depth
- In the worst case (skewed tree), h can be n
- In the best case (balanced tree), h is O(log n)
- Space is used by the call stack due to recursion
'''
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
