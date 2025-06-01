'''
https://leetcode.com/problems/path-with-minimum-effort/description/

Dijkstra's, but instead of accumulating cost with +, 
we take max() of the path so far and the current move’s difference.

Time Complexity Discussion:  
- Each cell is pushed into the heap at most once: O(m * n) heap operations.  
- Each heap operation (push/pop) takes O(log(m * n)).  
- So total time complexity is O((m * n) * log(m * n)).

Space Complexity Discussion:  
- Effort matrix takes O(m * n) space.  
- Heap can grow up to O(m * n) elements.  

Final Complexity:  
Time Complexity: O((m * n) * log(m * n))  
Space Complexity: O(m * n)
'''
from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        # Min heap: (effort_so_far, row, col)
        heap = [(0, 0, 0)]
        effort = [[float('inf')] * n for _ in range(m)]
        effort[0][0] = 0

        while heap:
            cur_effort, i, j = heappop(heap)

            # Reached destination
            if i == (m-1) and j == (n-1):
                return cur_effort

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if (
                    0 <= nr < m and 
                    0 <= nc < n
                ):
                    # Cost
                    diff = abs(heights[nr][nc] - heights[i][j])
                    next_effort = max(cur_effort, diff)

                    if next_effort < effort[nr][nc]:
                        effort[nr][nc] = next_effort
                        heappush(heap, (next_effort, nr, nc))
        
        # Unreachable
        return -1
