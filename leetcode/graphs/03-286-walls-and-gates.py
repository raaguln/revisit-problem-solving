# Good problem to understand BFS.
'''
Question - 
You are given an m x n grid rooms initialized with these three possible values.

1. -1  => A wall or an obstacle.
2. 0   => A gate.
3. INF => Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF 
   as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, 
it should be filled with INF.


Example 1:
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]


Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
'''


'''
Method 1 - For each cell, do BFS and find gate, update cell
Time: O(k * mn) -> k is the number of empty rooms
    1. The bfs function is called for every non-wall, non-gate cell (value > 0), so potentially O(mn) calls.
    2. Each bfs performs a level-order traversal and visits multiple cells. In the worst case, 
    the entire grid is traversed once for each call.
    3. Worst-case scenario: O((mn)²) when all cells are empty rooms, leading to redundant BFS calls.
Space: O(m*n) -> queue is O(m*n)
'''
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        if m == 1 and n == 1:
            return
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def bfs(i, j):
            visited = set()
            queue = deque()
            queue.append((i, j, 0))
            visited.add((i, j, 0))
            gateFound = False
            while queue:
                row, col, level = queue.popleft()
                level += 1
                for di, dj in directions:
                    r, c = row+di, col+dj
                    if (r < 0 or r >= m) or (c < 0 or c >= n):
                        continue
                    if rooms[r][c] == 0:
                        rooms[i][j] = level
                        return
                    elif (
                        rooms[r][c] > 0 and
                        (r,c) not in visited
                    ):
                        queue.append((r, c, level))
                        visited.add((r, c, level))

        for i in range(m):
            for j in range(n):
                if rooms[i][j] > 0:
                    bfs(i, j)
        

'''
Method 2 - For each gate, do BFS and update all cells (Multi-source BFS)
Time: O(m*n) -> each cell is visited once
    Step 1: Scanning the entire grid to enqueue gates → O(mn)
    Step 2: BFS visits each empty room (2147483647) exactly once → O(mn)
    Each cell is processed once, making the total complexity O(mn)
Space: O(m*n) -> queue is O(m*n)
'''
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        
        m, n = len(rooms), len(rooms[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        queue = deque()
        
        # Step 1: Add all gates (0s) to the queue
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        # Step 2: BFS from all gates simultaneously
        while queue:
            row, col = queue.popleft()
            for di, dj in directions:
                r, c = row + di, col + dj
                if 0 <= r < m and 0 <= c < n and rooms[r][c] == 2147483647:
                    rooms[r][c] = rooms[row][col] + 1
                    queue.append((r, c))
        
