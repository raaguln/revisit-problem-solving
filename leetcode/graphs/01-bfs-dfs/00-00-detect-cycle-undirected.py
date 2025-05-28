'''
DFS based approach
Time - O(V + E)
- Each node `V` is visited once due to the `seen` set preventing revisits
- Each edge `E` is explored once in each direction (undirected graph), hence visited twice overall
- Total time complexity is linear in the number of vertices and edges

Space - O(V)
- The `seen` set stores up to `V` nodes in the worst case
- Recursion stack depth can reach `V` in a linear graph (e.g., a straight chain of nodes)
- No other significant data structures used
'''
def has_cycle(node, parent):
    seen.add(node)
    for neighbor in adj_list[node]:
        # unvisited node
        if neighbor not in seen:
            if has_cycle(neighbor, node):
                return True
        # already visited node
        else:
            # reverse connection, not a cycle (0 -> <-1)
            if neighbor == parent:
                return False
            # Already visited, and not parent, so cycle!
            if neighbor != parent:
                return True
    return False

# Simplifies to
def has_cycle(node, parent):
    seen.add(node)
    for neighbor in adj_list[node]:
        if neighbor not in seen:
            if has_cycle(neighbor, node):
                return True
        elif neighbor != parent:
            return True
    return False

adj_list = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2]
}
seen = set()
# Run the check
cycle_found = has_cycle(0, -1)

'''
BFS
Time - O(V + E)
- Each node (V) is visited once
- Each edge (E) is examined once in an undirected graph
- Overall traversal takes linear time relative to the graph size

Space - O(V)
- The `visited` set stores up to V nodes
- The queue can hold up to O(V) nodes in the worst case
- No additional space beyond the queue and visited set
'''
def has_cycle_bfs(start):
    queue = deque()
    queue.append((start, -1))  # (node, parent)

    while queue:
        node, parent = queue.popleft()
        seen.add(node)

        for neighbor in adj_list[node]:
            if neighbor not in seen:
                queue.append((neighbor, node))
                seen.add(neighbor)  # mark as seen when enqueued
            elif neighbor != parent:
                # Seen before and not the parent => cycle
                return True
    return False

# Handle disconnected graphs
cycle_found = False
for node in adj_list:
    if node not in seen:
        if has_cycle_bfs(node):
            cycle_found = True
            break
