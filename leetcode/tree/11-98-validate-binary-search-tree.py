'''
Solution 1: Wrong answer
This does not work for the case where the left child of the root is greater than the root.
It only checks for immediate children.
Time: O(n) - DFS, goes through all nodes
Space: O(h) - recursion depth
    - Balanced tree: O(logn)
    - Skewed tree: O(n)
    5
   / \
  1   6
     / \
    4   7
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True
            if node.left and node.left.val >= node.val:
                return False
            if node.right and node.right.val <= node.val:
                return False
            return (
                dfs(node.left) and
                dfs(node.right)
            )
        return dfs(root)
    

'''
Solution 2: DFS - Recursion
Time: O(n) - DFS, goes through all nodes
Space: O(h) - recursion depth
    - Balanced tree: O(logn)
    - Skewed tree: O(n)
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True
            if not(left < node.val < right):
                return False
            return (
                dfs(node.left, left, node.val) and
                dfs(node.right, node.val, right)
            )
        return dfs(root, float('-inf'), float('inf'))


'''
Solution 3: DFS - Stack based
Helps avoid recursion depth errors in constrained systems
Time: O(n) - DFS, goes through all nodes
Space: O(h) - stack space
    - Balanced tree: O(logn)
    - Skewed tree: O(n)
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, left, right = stack.pop()
            if not node:
                continue
            if not(left < node.val < right):
                return False
            stack.append((node.left, left, node.val))
            stack.append((node.right, node.val, right))
        return True