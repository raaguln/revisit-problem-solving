"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Time Complexity Discussion:  
- BFS explores each cell at most once, so it visits O(n²) cells in an n x n grid.  
- Each cell checks up to 8 neighbors, so total operations are O(8 * n²) = O(n²).

Space Complexity Discussion:  
- The visited matrix takes O(n²) space.  
- The queue can hold up to O(n²) elements in the worst case.  
- Directions list is constant size O(1).

Final Complexity:  
Time Complexity: O(n²)  
Space Complexity: O(n²)
"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        visited = [[False for _ in range(n)] for _ in range(n)]
        visited[0][0] = True

        while queue:
            r, c, length = queue.popleft()

            if r == n-1 and c == n-1:
                return length

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < n and 
                    0 <= nc < n and 
                    not visited[nr][nc] and 
                    grid[nr][nc] == 0
                ):
                    visited[nr][nc] = True
                    queue.append((nr, nc, length + 1))

        return -1
