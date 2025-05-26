'''
https://leetcode.com/problems/inorder-successor-in-bst/description/
285. Inorder Successor in BST

Given the root of a binary search tree and a node p in it, 
return the in-order successor of that node in the BST. 
If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
'''
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None

        while root:
            if p.val < root.val:
                # Possible successor; go left for smaller one
                successor = root
                root = root.left
            else:
                # Too small or equal; go right to find larger
                root = root.right

        return successor


class Solution:
    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node
    
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        # Case 1: If p has right subtree, successor is min in right subtree
        if p.right:
            return self.getMin(p.right)
        
        # Case 2: No right subtree, look from root down to p
        successor = None
        while root:
            if p.val < root.val:
                successor = root  # Potential successor
                root = root.left
            elif p.val >= root.val:
                root = root.right
        return successor