from collections import deque

# BFS
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        rightView = []
        queue = deque([[root, 0]])
        level = 0
        while queue:
            lastNode = None
            while queue and queue[0][1] == level:
                lastNode, _ = queue.popleft()
                if lastNode.left:
                    queue.append([lastNode.left, level+1])
                if lastNode.right:
                    queue.append([lastNode.right, level+1])
            rightView.append(lastNode.val)
            level += 1
        return rightView
            

# DFS
class Solution:
    # THIS CODE PRINTS THE RIGHT MOST VALUES
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def dfs(node, depth):
            if not node:
                return
            if len(output) == depth:
                output.append(node.val)
            # What we need to modify - the order of the traversal
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            

        dfs(root, 0)
        return output
            