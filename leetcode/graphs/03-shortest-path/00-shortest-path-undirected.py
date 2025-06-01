# https://takeuforward.org/data-structure/shortest-path-in-undirected-graph-with-unit-distance-g-28/


'''
1. The shortest distance (between any node)
- undirected graph, edge = 1
Literally, nodes with the least number of nodes
Method - BFS

Time Complexity Discussion:  
- Building the adjacency list takes O(E), where E is the number of edges.  
- BFS visits each node once, so O(V), and explores all edges once, O(E).  
- Overall BFS traversal is O(V + E).

Space Complexity Discussion:  
- Adjacency list uses O(V + E) space.  
- The queue and visited set can hold up to O(V) elements.  

Final Complexity:  
Time Complexity: O(V + E)  
Space Complexity: O(V + E)
'''
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int, destination: int) -> int:
        # 1. Construct adj_list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        queue = deque([(src, 0)])  # (node, distance)
        visited = set()

        while queue:
            node, dist = queue.popleft()
            if node == destination:
                return dist

            for neighbor in adj_list[node]:
                if not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))

        return -1  # destination not reachable


'''
2. The shortest distance between source and each node
- undirected graph, edge = 1
- BFS

Time Complexity Discussion:  
- Building adjacency list: O(E), where E = number of edges.  
- BFS visits each node once and processes each edge once: O(V + E).  

Space Complexity Discussion:  
- Adjacency list uses O(V + E) space.  
- Distance array uses O(V) space.  
- Queue can hold up to O(V) elements.  

Final Complexity:  
Time Complexity: O(V + E)  
Space Complexity: O(V + E)
'''
class Solution:
    def shortestDistances(self, n: int, edges: list[list[int]], src: int) -> list[int]:
        # 1. Construct adj_list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)  # undirected graph

        dist = [-1] * n  # -1 means node not reachable
        dist[src] = 0

        queue = deque([src])
        while queue:
            node = queue.popleft()

            for neighbor in adj_list[node]:
                if dist[neighbor] == -1:  # not visited
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)

        return dist