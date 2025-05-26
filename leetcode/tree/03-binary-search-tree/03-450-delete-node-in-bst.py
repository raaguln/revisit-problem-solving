'''
https://leetcode.com/problems/delete-node-in-a-bst/description/

Deletion has 3 main cases:
1. Node to delete is a leaf (no children) → just remove it.
2. Node has one child → replace node with that child.
3. Node has two children → replace node’s value with its 
    inorder successor (smallest node in right subtree), then delete the successor node.
'''

'''
Time: O(h), where h = height of tree (O(log n) for balanced BST)
Space: O(1) (no recursion stack)
'''
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        # Node to delete is on left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        # Node to delete is on left
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # Node to delete is current
        else:
            # Case 1: no children:
            if not root.left and not root.right:
                return None

            # Case 2: Has only 1 subtree
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Case 3: Node with two children
            # Find the inorder successor
            successor = self.getMin(root.right)
            root.val = successor.val
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node