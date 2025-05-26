# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        1. root = p = q -> root is the LCA
        2. p&q are in left -> each node, check if node = p or node = q, if so return node value (one of our elements), else return None. Two cases - 
            - p=7, q=4, on recursion 2 receives both values - then that is our LCA
            - p=7, q=2, on recursion 2 receives one value - again that is our LCA
        3. p&q are in right -> same as above
        4. p&q are split -. root is the LCA
        '''
        '''
        - If the root itself matches both `p` and `q` (i.e., they are the same node), it returns the root directly.
        - If the current node is `None`, it returns `None`.
        - If the current node matches either `p` or `q`, it returns the current node (found one of the targets).
        - It then recursively searches the left and right subtrees.
        - If **both** left and right subtrees return non-null results, it means:
        - `p` was found in one subtree and `q` in the other.
        - Hence, the current node is their **lowest common ancestor**.
        - If only one side returns a non-null result, it bubbles that result up — meaning both `p` and `q` are in that subtree.
        '''
        # both p and q are root node 
        if p.val == q.val == root.val:
            return root.val
        def dfs(node):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if (left and right):
                return node
            if left:
                return left
            if right:
                return right
        return dfs(root)