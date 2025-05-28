'''
https://leetcode.com/problems/surrounded-regions/description/

First code: Calls bfs() separately for each border 'O'. 
This can lead to multiple BFS traversals that might 
overlap or revisit parts of the board unnecessarily.

Second code: Adds all border 'O's to the queue first, 
then performs a single BFS traversal that processes 
all connected regions from all border 'O's simultaneously.
'''


'''
Simple BFS - works
Time - O(m * n)
- Each cell is visited at most once by the BFS (marked 'S' when visited)
- BFS from border 'O's explores connected 'O' regions, overall covering at most all cells
- The final two nested loops each iterate over all m*n cells
- Total work is proportional to the number of cells in the board

Space - O(min(m, n))
- The BFS queue can hold at most O(min(m, n)) cells in the worst case (longest border-connected region)
- No additional data structures besides the queue and a few variables are used
- The call stack is not used since BFS is iterative
'''
from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            board[i][j] = 'S'  # Mark safe

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        board[nx][ny] = 'S'
                        queue.append((nx, ny))

        # 1. BFS from all border 'O's
        for i in range(m):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][n-1] == 'O':
                bfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[m-1][j] == 'O':
                bfs(m-1, j)

        # 2. Flip all remaining 'O' to 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        # 3. Flip back all safe 'S' to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'


'''
Multi-source BFS
Time - O(m * n)
- Each cell is visited at most once during the BFS marking process
- Enqueuing all border 'O's takes O(m + n) time
- BFS explores all connected 'O's from border cells, covering at most all cells once
- The final nested loop scans all cells to flip 'O' to 'X' and 'S' back to 'O'
- Overall complexity is linear in the number of cells

Space - O(min(m, n))
- The queue can hold at most O(min(m, n)) cells at a time in the worst case
- No recursion used, only iterative BFS with the queue
- In-place modifications of the board require no extra storage beyond the queue
'''
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()

        # 1. Enqueue all border 'O's
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
                board[i][0] = 'S'
            if board[i][n-1] == 'O':
                queue.append((i, n-1))
                board[i][n-1] = 'S'
        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0, j))
                board[0][j] = 'S'
            if board[m-1][j] == 'O':
                queue.append((m-1, j))
                board[m-1][j] = 'S'

        # 2. BFS to mark all connected 'O' as safe 'S'
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    board[nx][ny] = 'S'
                    queue.append((nx, ny))

        # 3. Flip all remaining 'O' to 'X', and 'S' back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

'''
Multi-source DFS
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            board[i][j] = 'S'
            for dx, dy in directions:
                dfs(i + dx, j + dy)

        # DFS from border 'O's
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n-1] == 'O':
                dfs(i, n-1)
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[m-1][j] == 'O':
                dfs(m-1, j)

        # Flip
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
