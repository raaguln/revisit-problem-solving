"""
https://leetcode.com/problems/network-delay-time/description/

If all edges had the same weight (e.g., 1 unit of time each), BFS would work fine.
It would find the minimum number of hops, which corresponds to shortest travel time.
"""

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        
        heap = [(0, k)]  # (time, node)
        
        while heap:
            time, node = heappop(heap)
            if time > dist[node]:
                continue
            for neighbor, w in graph[node]:
                new_time = time + w
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heappush(heap, (new_time, neighbor))
        
        max_delay = max(dist[1:])  # ignore index 0 since nodes start from 1
        return max_delay if max_delay != float('inf') else -1
