'''
https://leetcode.com/problems/inorder-successor-in-bst/description/
285. Inorder Successor in BST

Given the root of a binary search tree and a node p in it, 
return the in-order successor of that node in the BST. 
If the given node has no in-order successor in the tree, return null.

- in-order -> Left → Node → Right
- next node in the in-order traversal, i.e., 
  the smallest node that is greater than the given node.

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
'''
# Solution1 - sorted list, and then find the next index
# O(n) traversal, O(n) search
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inorder_nodes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_nodes.append(node)
            inorder(node.right)

        inorder(root)

        for i in range(len(inorder_nodes)):
            if inorder_nodes[i].val == p.val:
                return inorder_nodes[i+1] if i + 1 < len(inorder_nodes) else None


# Full tree traversal - inefficient
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

# Using BST properties
# O(h) - which is usually O(log n) since BST is balanced
# p - is the node in the tree (it will have its left and right values)
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