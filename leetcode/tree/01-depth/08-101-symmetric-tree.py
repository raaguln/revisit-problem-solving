# https://leetcode.com/problems/symmetric-tree/
'''
Time - O(n)
- Each node is visited exactly once in a mirrored DFS traversal
- n is the number of nodes in the tree

Space - O(h)
- h is the height of the tree, representing the maximum recursion depth
- In the worst case (skewed tree), h can be n
- In the best case (balanced tree), h is O(log n)
- Space is used by the call stack due to recursion
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )
        
        return isMirror(root.left, root.right) if root else True