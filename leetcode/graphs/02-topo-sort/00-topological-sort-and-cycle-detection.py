'''
Topological  - 
- DFS-  https://www.youtube.com/watch?v=GYmq98CVm2c
- Kahn's - https://www.youtube.com/watch?v=cIBFEhD77b4
- Topological ordering - one graph can have multiple valid ones
- Can be only done for DAG

Use cases - 
1. dependencies, prerequisites, course/event schedules


'''
# Order the nodes of a DAG in a way that every edge
# from u to v, u comes before v in the ordering

# Algo - dfs() and add to stack whenever a node has no more neighbors.
# Pop the entire stack, this is our topological order (or stack[::-1])

'''
DFS Toplogical sort
Time Complexity: O(V + E)  
- Each node is visited once, and each edge is explored once during DFS traversal.

Space Complexity: O(V + E)  
- O(V) for the visited list and recursion stack (in worst case), and O(E) for the adjacency list. 
'''
def topo_sort_dfs(adj):
    n = len(adj)
    visited = [False] * n
    stack = []

    # Postorder traversal
    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        stack.append(u)

    for i in range(n):
        if not visited[i]:
            dfs(i)
    return stack[::-1]


'''
Kahn's algorithm
- in-degree for a node = no of incoming edges to a node
- array to keep track of in-degree of each node
- queue to add and process nodes with no in-degree
'''
def topo_sort_kahn(adj):
    n = len(adj)

    indegree = [0] * n
    for node in adjacency_list:
        for neighbor in adjacency_list[node]:
            indegree[neighbor] += 1

    # Add nodes with 0 in-degree to queue
    q = deque()
    for node in range(n):
        if indegree[node] == 0:
            q.append(node)
    
    ordering = []
    while q:
        node = q.popleft()
        ordering.append(node)

        # Update in-degree and append
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
                
    if len(ordering) == n:
        return ordering
    # return empty if cycle
    return []

# ---------------------------------------------
# Cycle detection
# 1. DFS + 3-color marking
def has_cycle_dfs(adj):
    n = len(adj)
    visited = [0] * n  # 0=unvisited, 1=visiting, 2=visited

    def dfs(node):
        # Node is being visited and encountered again -> cycle detected
        if visited[node] == 1:
            return True

        # Node and its descendants are already fully processed
        if visited[node] == 2:
            return False
        
        visited[node] = 1
        for neighbor in adj[node]:
            if dfs(neighbor):
                return True
        visited[node] = 2
        return False

    # Handle disconnected graphs by running DFS from each unvisited node
    for i in range(n):
        if visited[i] == 0:
            if dfs(i):
                return True  # cycle found

    return False  # no cycle found

# 2. Kahns
def has_cycle_kahn(adj):
    n = len(adj)
    indegree = [0] * n
    for u in adj:
        for v in u:
            indegree[v] += 1

    q = deque(i for i in range(n) if indegree[i] == 0)
    count = 0

    while q:
        u = q.popleft()
        count += 1
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return count != n  # if not all nodes processed → cycle
