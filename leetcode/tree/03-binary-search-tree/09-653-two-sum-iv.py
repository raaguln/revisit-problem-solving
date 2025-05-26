# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        '''
        Method 1 - 
            - do inorder traversal, and then two pointer
            - Time and space - O(n)
        Method 2 - 
            - hashset while DFS
            - O(n) space as well but traverses tree 
              once without building an explicit array
        '''
        seen = set()
        
        def dfs(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        