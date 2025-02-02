# Time: O(n)
# Space: O(n)

from collections import deque

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

# Recursive preorder traversal (Root, Left, Right)
def preorder_traversal(root):
    if root is not None:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)  

# Recursive inorder traversal (Left, Root, Right)
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Recursive postorder traversal (Left, Right, Root)
def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")