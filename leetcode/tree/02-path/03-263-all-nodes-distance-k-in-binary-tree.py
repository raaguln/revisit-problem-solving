'''
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

Time - O(n)
- Building the adjacency list visits each node once: O(n)
- BFS traversal also visits each node at most once: O(n)
- Overall time complexity is O(n), where n is the number of nodes in the tree

Space - O(n)
- The adjacency list stores edges for each node: O(n)
- The queue and visited set store nodes during BFS: O(n)
- The recursion stack for `buildGraph` is O(h), with h being tree height, but this is dominated by O(n) overall space
'''
from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        '''
        Since both directions are allowed - 
        1. convert to graph
        2. do bfs and find all nodes
        '''
        adjacencyList = defaultdict(list)
        def buildGraph(node, parent):
            if not node:
                return
            if parent:
                adjacencyList[parent.val].append(node.val)
                adjacencyList[node.val].append(parent.val)
            buildGraph(node.left, node)
            buildGraph(node.right, node)
            
        buildGraph(root, None)

        # node, distance
        queue = deque([(target.val, 0)])
        visited = set()
        results = []
        while queue:
            node, distance = queue.popleft()
            
            if node in visited:
                continue
            visited.add(node)

            if distance == k:
                results.append(node)
            
            if distance < k:
                for neighbor in adjacencyList[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, distance + 1))
        
        return results