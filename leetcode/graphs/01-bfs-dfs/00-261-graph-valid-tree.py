# 1. DFS - Time: O(V + E) ≈ O(V)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Undirected graph is a valid tree or not - two properties:
        - graph must be connected — all nodes are reachable from any start node
        - graph must be acyclic

        Method 1 - DFS + cycle detection
        '''
        # A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Adjacency list
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        dfs(0)

        if len(visited) == n:
            # Graph is connected
            return True
        else:
            # If not, it means some nodes are isolated
            return False

# 2. Union find - Time: O(E * α(V)) ≈ O(V)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Undirected graph is a valid tree or not - two properties:
        - graph must be connected — all nodes are reachable from any start node
        - graph must be acyclic

        Method 2 - Union find
        '''
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False  # Cycle detected
            parent[rootY] = rootX
            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True  # Connected and acyclic