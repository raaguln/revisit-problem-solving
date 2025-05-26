# https://leetcode.com/problems/recover-binary-search-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        - Inorder traversal - two elements out of order
        - either one or two inversions
            1. adjacent nodes
                - previous node > current node at one point
            2. not adjacent nodes
                - previous node > current node at two points
        '''
        prev = None
        n1, n2 = None, None

        def inorder(node):
            if not node:
                return

            nonlocal prev, n1, n2

            inorder(node.left)

            # Check prev
            if prev and prev.val > node.val:
                if not n1:
                    n1 = prev
                n2 = node

            # Set prev to current node for next iter
            prev = node

            inorder(node.right)
        
        inorder(root)

        n1.val, n2.val = n2.val, n1.val

        