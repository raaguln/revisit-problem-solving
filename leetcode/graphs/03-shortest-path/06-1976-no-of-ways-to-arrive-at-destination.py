"""
https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/

Use a modified Dijkstra’s algorithm with two arrays/lists:
dist[node] = shortest distance to node.
ways[node] = number of shortest paths to node.

Algorithm steps:
Initialize dist with infinity except dist[0] = 0.
Initialize ways with 0 except ways[0] = 1 (one way to start at node 0).
Use a min-heap priority queue to pick the next node with the smallest distance.
For each neighbor:
    If a shorter distance is found, update dist and reset ways.
    If a distance equal to the shortest is found, add ways count.
"""
class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        dist = [float('inf')] * n
        dist[0] = 0
        
        ways = [0] * n
        ways[0] = 1
        
        heap = [(0, 0)]  # (distance, node)
        
        while heap:
            curr_dist, node = heappop(heap)
            
            if curr_dist > dist[node]:
                continue
            
            for neighbor, time in graph[node]:
                new_dist = curr_dist + time
                
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    ways[neighbor] = ways[node]
                    heappush(heap, (new_dist, neighbor))
                elif new_dist == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n-1] % MOD
