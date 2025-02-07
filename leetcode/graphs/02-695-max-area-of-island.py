# Time: O(V + E) -> each node (V) is visited once and each edge (E) is visited once
# Space: O(V) -> queue is O(V), seen set is O(V)
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        def bfs(i, j):
            queue = deque()
            # Consider the current land
            queue.append((i, j))
            visited.add((i, j))
            area = 1
            
            # Check adjacent lands
            while queue:
                row, col = queue.popleft()
                for di, dj in directions:
                    r, c = row + di, col + dj
                    if (
                        0 <= r < m and
                        0 <= c < n and
                        grid[r][c] == 1 and
                        (r, c) not in visited
                    ):
                        area += 1
                        visited.add((r, c))
                        queue.append((r, c))
            return area

        # For each island, calculate area and update maxArea
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = bfs(i, j)
                    maxArea = max(maxArea, area)

        return maxArea