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
        # both p and q are root node 
        if p.val == q.val == root.val:
            return root.val
        def dfs(node):
            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node
            left, right = dfs(node.left), dfs(node.right)
            if (left and right):
                return node
            if left:
                return left
            if right:
                return right
        return dfs(root)