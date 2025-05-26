# https://leetcode.com/problems/subtree-of-another-tree/description/
# DFS
# Time: O(n)
# Space: O(logn) - recursive stack


# A = big tree, B = small tree (which can be subroot of A)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (
                p.val == q.val and
                isSameTree(p.left, q.left) and
                isSameTree(p.right, q.right)
            )
        
        # if no A - B can't be subtree of A
        if not root:
            return False
        # If no B - empty node is always a subtree of A
        if not subRoot:
            return True
        # Check root
        if isSameTree(root, subRoot):
            return True
        # Check left and right subtrees
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )
