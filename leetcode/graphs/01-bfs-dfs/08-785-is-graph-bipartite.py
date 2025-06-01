'''
https://leetcode.com/problems/is-graph-bipartite/description/

check if a graph is bipartite is to try to 2-color it using BFS (or DFS). 
If we can assign colors to nodes such that no two adjacent 
nodes share the same color, the graph is bipartite.

Time - O(V + E)
- Each node is processed once in the BFS traversal
- Each edge is examined once when checking neighbors
- Total time is proportional to the sum of vertices and edges in the graph

Space - O(V)
- Color array stores the color state for each vertex: O(V)
- Queue can hold up to O(V) nodes in the worst case during BFS
- No additional significant space used

'''
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 means uncolored, 0 and 1 are two colors
        
        for start in range(n):
            if color[start] == -1:  # not colored yet, so new component
                queue = deque([start])
                color[start] = 0
                
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == -1:
                            color[neighbor] = 1 - color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            # Adjacent nodes have the same color - not bipartite
                            return False
        return True
