"""
https://leetcode.com/problems/find-eventual-safe-states/description/

A node is a terminal node if there are no outgoing edges. 
A node is a safe node if every possible path starting 
from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of 
the graph. The answer should be sorted in ascending order.
"""

"""
DFS + 3 coloring

The problem is really about detecting cycles.
If a node is part of a cycle or can reach a cycle, it's not safe.
If a node has no outgoing edges (terminal node), it’s safe.
If all its children are safe, then the node itself is safe.
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n          # 0 = unvisited, 1 = visiting, 2 = safe
        
        def dfs(u: int) -> bool:
            """
            Returns True if node u is safe, False if it can reach a cycle.
            Side effect: colors nodes as we go.
            """
            # back-edge → cycle
            if color[u] == 1:          
                return False
            # already proven safe
            if color[u] == 2:
                return True
            
            color[u] = 1         # mark as visiting
            for v in graph[u]:
                if not dfs(v):   # any child that’s unsafe → u unsafe
                    return False
            color[u] = 2         # all children safe → u safe
            return True
        
        # run DFS for every node
        safe_nodes = []
        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
        return safe_nodes


"""
Kahn's - takes way more time and space
"""
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        outdegree = [0] * n

        # Build reverse graph and count out-degrees
        for u in range(n):
            outdegree[u] = len(graph[u])
            for v in graph[u]:
                reverse_graph[v].append(u)

        # Terminal nodes (outdegree 0)
        q = deque([i for i in range(n) if outdegree[i] == 0])

        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True  # This node is safe
            for prev in reverse_graph[node]:
                outdegree[prev] -= 1
                if outdegree[prev] == 0:
                    q.append(prev)

        # Return all nodes marked safe
        return [i for i in range(n) if safe[i]]
