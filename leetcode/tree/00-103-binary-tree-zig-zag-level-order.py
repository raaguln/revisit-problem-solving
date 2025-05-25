# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''
Time - O(n)
- Each node is visited exactly once and added to the result
- Reversing `levelNodes` takes O(k) time per level, where k is the number of nodes at that level
- Total cost of all reversals across levels is O(n)
- Overall time complexity is O(n), where n is the number of nodes in the tree

Space - O(n)
- The queue stores nodes level by level, with at most O(n) nodes in the worst case
- The result list also stores all node values: O(n)
- Temporary `levelNodes` list stores at most one level's worth of nodes: O(w), where w is the max width, which is O(n) in the worst case
'''
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        level = 1
        queue = deque([(root, level)])
        fromLeft = True
        while queue:
            levelNodes = []
            while queue and queue[0][1] == level:
                node, local_level = queue.popleft()
                levelNodes.append(node.val)
                if node.left:
                    queue.append((node.left, local_level+1))
                if node.right:
                    queue.append((node.right, local_level+1))
            levelNodes
            if not fromLeft:
                levelNodes = levelNodes[::-1]
            
            result.append(levelNodes)
            fromLeft = not fromLeft
            level += 1
        return result