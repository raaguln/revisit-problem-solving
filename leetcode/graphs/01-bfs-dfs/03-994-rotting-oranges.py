# https://leetcode.com/problems/rotting-oranges/description/
'''
Time: O(m*n) -> getting rotten oranges is O(m*n) and BFS is O(m*n) (each fresh orange is visited once)
Space: O(m*n) -> queue can have all the oranges in the worst case

Mistakes you did:
1. Forgot for _ in range(len(rotten)): -> process at current level cauz only these oranges
got rotten in this minute
2. Forgot to check if fresh == 0 at the end of the loop -> if fresh == 0, return minutesDone
'''
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return None
        m, n = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        minutesDone = 0
        while rotten and fresh > 0:
            minutesDone += 1
            # For rotten oranges in current level
            for _ in range(len(rotten)):
                row, col = rotten.popleft()
                for di, dj in directions:
                    r, c = row+di, col+dj
                    if r < 0 or r >= m or c < 0 or c >= n:
                        continue
                    # Already rotten or empty
                    elif grid[r][c] == 2 or grid[r][c] == 0:
                        continue
                    else:
                        grid[r][c] = 2
                        fresh -= 1
                        rotten.append((r, c))
        
        if fresh == 0:
            return minutesDone
        return -1


