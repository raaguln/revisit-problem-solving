# Preorder
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node):
            if not node:
                return []
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return result

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            # Stack pops from left, so add right first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

# Inorder
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)
        return result

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right
        return result

# Postorder
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
        dfs(root)
        return result

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        last_visited = None

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                # if right child exists and traversing node from left child, move to right child
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    stack.pop()
                    result.append(peek_node.val)
                    last_visited = peek_node

        return result

# Level order
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def bfs(node, level):
            if not node:
                return None
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            # Traverse children
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)
        bfs(root, 0)
        return result

# QUEUE 1
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        output = []
        queue = deque([[root, 1]])
        level = 1
        while queue:
            levelNodes = []
            while queue and queue[0][1] == level:
                node, _ = queue.popleft()
                levelNodes.append(node.val)
                if node.left:
                    queue.append([node.left, level+1])
                if node.right:
                    queue.append([node.right, level+1])
            output.append(levelNodes)
            level += 1
        return output        

# QUEUE 2
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if level == len(result):
                result.append([])
            result[level].append(node.val)
            
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        return result