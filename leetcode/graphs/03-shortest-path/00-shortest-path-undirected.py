# https://takeuforward.org/data-structure/shortest-path-in-undirected-graph-with-unit-distance-g-28/
from collections import deque, defaultdict

def shortest_path(n, edges, src=0):
    # Step 1: Create adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)  # Because the graph is undirected

    # Step 2: Initialize distance array
    dist = [-1] * n
    dist[src] = 0  # Distance to source is 0

    # Step 3: BFS from the source
    queue = deque([src])

    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return dist

# Example usage
n = 9
edges = [[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
result = shortest_path(n, edges, src=0)
print(" ".join(map(str, result)))
