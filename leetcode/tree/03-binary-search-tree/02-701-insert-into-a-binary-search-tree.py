# https://leetcode.com/problems/insert-into-a-binary-search-tree/
'''
This problem guarantees that the value will not already exist in BST.
So we will always insert at leaf=None positions

i.e The only place where this can be done without breaking structure 
is at a leaf position (i.e., where a child would be None).

If duplicates were allowed, use count = n and update that field for that node
'''

# Recursive
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root

# Iterative
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        current = root
        while True:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
        
        return root