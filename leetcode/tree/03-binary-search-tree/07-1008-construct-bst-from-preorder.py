'''
- Preorder -> root, left, right
- When we construct, we also need to make sure that the BST properties are satisfied

- bound -> restricts the maximum value a node in the current subtree
- For the left child, this bound is the parent node’s value (must be less than it).
- For the right child, it keeps the previous bound from above (must be less than that).
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index = 0

        def makeBST(maxValAllowed):
            nonlocal index
            # Base case
            if index == len(preorder):
                return None

            # If the value violates BST property
            # add to next subtree
            if preorder[index] > maxValAllowed:
                return None

            value = preorder[index]
            # index update needs to happen here, else inf recursion
            index += 1
            node = TreeNode(val=value)
            # maxValAllowed is current node's value
            node.left = makeBST(value)
            # keeps maxValAllowed from parent
            node.right = makeBST(maxValAllowed)
            
            return node

        return makeBST(float("inf"))