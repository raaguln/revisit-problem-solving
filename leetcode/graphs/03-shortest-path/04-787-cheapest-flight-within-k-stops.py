'''

1. Djikstras with k stops
- k stops -> k+1 edges
- Most optimal

you need to track both cost and stops since the 
normal Dijkstra doesn’t handle constraints like number of stops.
'''

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        # [from, to, price]
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Min heap: (cost_so_far, current_city, stops_so_far)
        heap = [(0, src, 0)]
        
        # To track the minimum stops reached for each city (pruning)
        visited = dict()
        
        while heap:
            cost, city, stops = heappop(heap)
            
            # If reached destination, return cost
            if city == dst:
                return cost
            
            # If stops exceed limit, skip
            if stops > k:
                continue
            
            # If we've already visited city with fewer or equal stops, prune
            if city in visited and visited[city] <= stops:
                continue
            
            visited[city] = stops
            
            for nei, price in graph[city]:
                heappush(heap, (cost + price, nei, stops + 1))
        
        return -1

'''
2. Bellman Ford
- Handles it easily using the k+1, but not optimal always
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize distances with infinity
        dist = [float('inf')] * n
        dist[src] = 0
        
        # Relax edges up to k+1 times (because k stops means k+1 edges max)
        for i in range(k + 1):
            temp_dist = dist[:]  # copy current distances to update in this iteration
            for u, v, w in flights:
                if dist[u] == float('inf'):
                    continue
                # Relax the edge if better cost is found
                if dist[u] + w < temp_dist[v]:
                    temp_dist[v] = dist[u] + w
            dist = temp_dist
        
        return dist[dst] if dist[dst] != float('inf') else -1