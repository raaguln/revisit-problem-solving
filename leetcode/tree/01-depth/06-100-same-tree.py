# DFS
"""
Time - O(n)
- Each node in both trees is visited exactly once
- n is the total number of nodes in the smaller of the two trees (assuming both trees are of similar size)

Space - O(h)
- h is the height of the trees, representing the maximum recursion depth
- In the worst case (skewed trees), h can be n
- In the best case (balanced trees), h is O(log n)
- Space is used by the call stack due to recursion
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False 
        return (
            p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )
    
# BFS
# Time: O(n)
# Space: O(logn) - recursive stack
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            n1, n2 = q1.popleft(), q2.popleft()
            if not n1 and not n2:
                continue
            if (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
                return False
            q1.extend([n1.left, n1.right])
            q2.extend([n2.left, n2.right])
        return True


        