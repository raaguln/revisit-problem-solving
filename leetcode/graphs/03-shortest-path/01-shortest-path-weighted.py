# Djikstra's & Bellman Ford
# https://youtu.be/j0OUwduDOS0?t=141
#

'''
Djikstra's
- shortest path
- non-negative edges only
- Directed or undirected

Why it fails for -ve edges
- it assumes that once a node’s shortest distance is found, it won’t change
'''
class Solution:
    def dijkstra(self, n: int, edges: list[list[int]], src: int) -> list[int]:
        # 1. Build adjacency list
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))  # If undirected

        # Min-heap: (node, distance)
        heap = [(src, 0)]
        dist = [float('inf')] * n
        dist[src] = 0
        visited = set()

        # Pop the node with the smallest distance
        while heap:
            node, distance = heappop(heap)

            # heap - we pop the min. So once we visit a node - 
            # we will already have the least distance from source
            # so do nothing
            if node in visited:
                continue
            visited.add(node)

            # for all neighbors, update the shortest distance
            for neighbor, weight in graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    heappush(heap, (neighbor, dist[v]))

        return dist


'''
Bellman ford

'''
class Solution:
    def bellmanFord(self, n: int, edges: list[list[int]], src: int) -> list[int]:
        # Step 1: Initialize distance array
        dist = [float('inf')] * n
        dist[src] = 0

        # Step 2: Relax all edges (n - 1) times
        for _ in range(n - 1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Optional: Step 3 - Check for negative weight cycles
        # If we can relax one more time, then a negative cycle exists
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                raise ValueError("Graph contains a negative weight cycle")

        return dist
