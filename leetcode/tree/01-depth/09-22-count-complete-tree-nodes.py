# DFS
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1 + left + right
        return dfs(root)

# BFS
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return count