'''
https://leetcode.com/problems/number-of-enclaves/description/

Time - O(m * n)
- Each cell is visited at most once by BFS when marking reachable land cells from the border
- BFS from all border land cells collectively cover at most all cells
- The final nested loops scan all cells to count enclaves
- Total complexity linear in the number of cells

Space - O(m * n)
- The visited matrix uses O(m * n) space
- The BFS queue can hold up to O(m * n) cells in the worst case (if all cells are land and connected)
- No recursion stack used since BFS is iterative
'''

from collections import deque
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

        # 1. Run BFS from all land cells on the border
        for i in range(m):
            for j in [0, n-1]:  # first and last column
                if grid[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)
        for j in range(n):
            for i in [0, m-1]:  # first and last row
                if grid[i][j] == 1 and not visited[i][j]:
                    bfs(i, j)

        # 2. Count land cells not visited (enclaves)
        enclave_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    enclave_count += 1

        return enclave_count

'''
Multi source BFS and using same storage
Time - O(m * n)
- Each cell is processed at most once during BFS marking connected land cells from the border
- Enqueuing all border land cells takes O(m + n)
- BFS explores all reachable land cells from borders, collectively covering at most all cells
- Final loop counts remaining land cells by scanning the entire grid

Space - O(min(m, n))
- The queue holds cells during BFS; in worst case, it can grow up to O(min(m, n)) (longest border-connected land strip)
- No extra visited matrix needed since grid is modified in place to mark visited cells
- No recursion stack used since BFS is iterative
'''
from collections import deque
from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()

        # Enqueue all border land cells and mark them visited by setting to 0
        for i in range(m):
            for j in [0, n-1]:
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0
        for j in range(n):
            for i in [0, m-1]:
                if grid[i][j] == 1:
                    queue.append((i, j))
                    grid[i][j] = 0

        # BFS to mark all reachable land from border as sea (0)
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))

        # Count remaining land cells (enclaves)
        enclave_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    enclave_count += 1

        return enclave_count
