'''
Inorder traversal gives you the sorted order of the elements in the BST.
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sortedArr.append(node.val)
            inorder(node.right)
        inorder(root)
        return sortedArr[k-1]
    

'''
Inorder traversal without recursion
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArr = []
        
        stack = []
        curr = root
        while stack or curr:
            # Reach the left most node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Add the left most element
            curr = stack.pop()
            sortedArr.append(curr.val)

            # Process the right side of the same level
            curr = curr.right

        return sortedArr[k-1]
    
'''
Inorder traversal without recursion - early stopping
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArr = []
        
        stack = []
        curr = root
        i = 0
        while stack or curr:
            # Reach the left most node
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Add the left most element
            curr = stack.pop()
            i += 1
            if i == k:
                return curr.val
            # sortedArr.append(curr.val)

            # Process the right side of the same level
            curr = curr.right