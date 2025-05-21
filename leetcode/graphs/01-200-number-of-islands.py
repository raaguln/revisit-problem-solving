# Time: O(V + E) -> each node (V) is visited once and each edge (E) is visited once
# Space: O(V) -> queue is O(V), seen set is O(V)
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        visited = set()
        islands = 0
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            while queue:
                row, col = queue.popleft()
                visited.add((i, j))
                for di, dj in directions:
                    r, c = row+di, col+dj
                    if (
                        0 <= r < m and
                        0 <= c < n and
                        grid[r][c] == "1" and
                        (r, c) not in visited
                    ):
                        queue.append((r, c))
                        visited.add((r, c))
                        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands

                        
'''
Memory optimized - instead of using visited, store it in the grid itself
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0
        # visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            while queue:
                i, j = queue.popleft()
                # visited.add((i, j))
                grid[i][j] = "0"
                for di, dj in directions:
                    r, c = i + di, j + dj
                    if (0 <= r < m and
                        0 <= c < n and
                        grid[r][c] == "1"):
                        queue.append((r, c))
                        # visited.add((r, c))
                        grid[r][c] = "0"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1

        return islands


