n = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

# Create an adjacency list
from collections import defaultdict
adj_list = defaultdict(list)
for a, b in A:
    adj_list[a].append(b)
    # For undirected graph
    # adj_list[b].append(a)
print(adj_list)

# Create an adjacency matrix
adj_matrix = [[0] * n for _ in range(n)]
for a, b in A:
    adj_matrix[a][b] = 1
    # For undirected graph
    # adj_matrix[b][a] = 1
# print(adj_matrix)

'''
DFS Recursive (with adjacency list)
Time: O(V + E) -> each node (V) is visited once and each edge (E) is visited once
Space: O(V) -> recursive call stack is O(V), seen set is O(V)
'''
def dfs(node):
    seen.add(node)
    for neighbor in adj_list[node]:
        if neighbor not in seen:
            dfs(neighbor)
    return list(seen)


seen = set()
dfs(0)
print(seen)


'''
Iterative DFS (with adjacency list)
Time: O(V + E) -> each node (V) is visited once and each edge (E) is visited once
Space: O(V) -> stack is O(V), seen set is O(V)
'''
stack = [0]
seen = set()
while stack:
    node = stack.pop()
    seen.add(node)
    for neighbor in adj_list[node]:
        if neighbor not in seen:
            stack.append(neighbor)
print(list(seen))

'''
BFS (with adjacency list)
Time: O(V + E) -> each node (V) is visited once and each edge (E) is visited once
Space: O(V) -> queue is O(V), seen set is O(V)
'''
from collections import deque

queue = deque([0])
seen = set()
while queue:
    node = queue.popleft()
    seen.add(node)
    for neighbor in adj_list[node]:
        if neighbor not in seen:
            queue.append(neighbor)
print(list(seen))