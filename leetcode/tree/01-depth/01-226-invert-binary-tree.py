# https://leetcode.com/problems/invert-binary-tree/description/
'''
DFS
Time - O(n)
- Visits every node exactly once
- `n` is the total number of nodes in the tree

Space - O(h)
- `h` is the height of the tree
- Space used by recursion call stack due to depth-first traversal
- Worst case (skewed tree): O(n)
- Best case (balanced tree): O(log n)
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

'''
BFS
O(n)
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
