# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# 1. DFS recursion
'''
Time - O(n)
- Each node in the binary tree is visited exactly once during the DFS traversal
- n is the number of nodes in the tree

Space - O(h)
- h is the height of the tree, representing the maximum recursion depth
- In the worst case (skewed tree), h can be n
- In the best case (balanced tree), h is O(log n)
- Space is used by the call stack due to recursion
'''
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
    
'''
Time - O(n)
- Each node is pushed and popped from the stack exactly once
- n is the number of nodes in the tree

Space - O(h)
- h is the height of the tree, representing the maximum number of nodes stored in the stack at once
- In the worst case (skewed tree), h can be n
- In the best case (balanced tree), h is O(log n)
- Space is used by the stack storing nodes and their depths
'''
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
            