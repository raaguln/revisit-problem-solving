'''
Time - O(n)
- Each node is visited exactly once during the DFS traversal
- n is the number of nodes in the tree
- At each leaf node, a path (of length at most h) is copied to the result, and the total number of such copies across all leaves is O(n) in the worst case

Space - O(h)
- h is the height of the tree, representing the maximum depth of the recursion stack and the length of the `path` list
- In the worst case (skewed tree), h can be n
- In the best case (balanced tree), h is O(log n)
- The `result` list can store up to O(n) node values across all paths, but the auxiliary space (excluding output) is O(h)
'''

'''
How it works
Start at root 1:
path = [1]

Go left to 2:
path = [1, 2]

It's a leaf → save [1, 2] to result

Backtrack: remove 2
path = [1]

Go right to 3:
path = [1, 3]

It's a leaf → save [1, 3] to result

Backtrack: remove 3
path = [1]

Backtrack from root:
path = []
'''
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[List[int]]:
        result = []
        path = []  # Global (outer) variable shared across all recursive calls

        def dfs(node):
            if not node:
                return

            path.append(node.val)

            # This is a leaf node, add to results
            if not node.left and not node.right:
                result.append(path.copy())

            dfs(node.left)
            dfs(node.right)

            path.pop()  # Backtrack

        dfs(root)
        return result