# DON'T - IT IS GENERAL TREE
'''
Time - O(n)
- In the worst case, all nodes are visited (e.g., unbalanced or degenerate tree)
- Does not take advantage of BST properties (searches both left and right)

Space - O(h)
- h is the height of the tree, representing the maximum recursion depth
- In the worst case (skewed tree), h can be n
- In the best case (balanced tree), h is O(log n)
- Space is used by the call stack due to recursion
'''
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        return (
            self.searchBST(root.left, val) or 
            self.searchBST(root.right, val)
        )

# USE THIS
'''
Time - O(h)
- h is the height of the BST
- At each step, the algorithm eliminates half the tree by following BST properties
- In the worst case (unbalanced tree), h can be n
- In the best case (balanced tree), h is O(log n)

Space - O(h)
- h is the height of the tree, representing the maximum recursion depth
- In the worst case (skewed tree), h can be n
- In the best case (balanced tree), h is O(log n)
- Space is used by the call stack due to recursion
'''
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)