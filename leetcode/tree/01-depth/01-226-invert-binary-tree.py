# https://leetcode.com/problems/invert-binary-tree/description/
'''
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