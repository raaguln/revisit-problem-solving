# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# LCA in Binary Search Tree
# Note - this applies only cauz it is a BST

# Time: O(logn) - half the tree is discarded at each step
# Space: O(logn) - recursive stack
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        4 possible scenarios
        1. root == p == q -> root is the LCA
        2. both p and q > root -> since BST, both will be on right
        3. both p and q < root -> both will be on left
        4. p > root > q, or q > root > p -> both will be on opposite sides

        In above scenarios - 
        1. - root is LCA
        4. - since both are opposite sides, root will again always be the LCA
        2&3. - either go left or right and set the node as root (2 or 8), and then it is
        a recursive pattern of 4
        eg: p&q are on right, so you set 8 as root node
            - if p&q are 8, then 8 is the LCA (1.)
            - if p&q are on opposite sides, then 8 is the LCA (4.)
            - if p&q are greater than 8, then 2. again
            - if p&q are less than 8, then 3. again
        '''
        current = root
        while current:
            if p.val > current.val and q.val > current.val:
                current = current.right
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                return current


        