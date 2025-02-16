# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Slightly innefficient cauz we pass the entire path
# Time: O(n) - height of the tree and comparison is log n
# Space: O(logn + k)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        path = []
        goodNodes = 0
        def dfs(node, path):
            nonlocal goodNodes
            if not node:
                return

            if all(node.val >= val for val in path):
                goodNodes += 1

            path.append(node.val)
            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, path)
        return goodNodes
    
# Time: O(n)
# Space: O(log n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodesCount = 0

        def dfs(node, maxVal):
            if not node:
                return None
            nonlocal goodNodesCount
            if node.val >= maxVal:
                goodNodesCount += 1
                maxVal = node.val
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        
        # initially passed 0 here, hidden test case had node values with -ve,
        # so didnt' work
        dfs(root, root.val)
        return self.goodNodesCount