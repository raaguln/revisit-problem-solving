# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        1. best path through node - left + node.val + right
        2. when returning to parent - we cannot have both left and right, only
        the best part because we can't have loops
            - so return node.val + max(left, right)
        '''
        maxSum = float("-inf")

        # returns max gain for a node
        def dfs(node):
            if not node:
                return 0

            # Only consider positive gains
            leftGain = max(dfs(node.left), 0)
            rightGain = max(dfs(node.right), 0)

            # Check if max path is just upto this node
            nonlocal maxSum
            nodeGain = node.val + leftGain + rightGain
            maxSum = max(maxSum, nodeGain)

            # Check if max path is this node and above
            # Parent -> can either have left only or right only
            # so pass the max value up top
            parentGain = node.val + max(leftGain, rightGain)
            return parentGain
        
        dfs(root)
        return maxSum
        