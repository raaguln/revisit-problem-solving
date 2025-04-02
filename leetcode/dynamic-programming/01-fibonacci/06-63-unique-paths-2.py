'''
Top down
Time - O(2^(m+n)) - 2^(m+n) calls
Space - O(m+n) recursion stack for m*n calls
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # If start or end is obstacle
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        def countPaths(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            if obstacleGrid[i][j] == 1:
                return 0
            return countPaths(i-1, j) + countPaths(i, j-1)
        return countPaths(m-1, n-1)

'''
Top down with memoization
Time - O(2^(m+n)) - 2^(m+n) calls
Space - O(m+n) recursion stack for m*n calls
'''
class Solution:
    def __init__(self):
        self.cache = {}
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # If start or end is obstacle
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        def countPaths(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            if obstacleGrid[i][j] == 1:
                return 0
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            ways = countPaths(i-1, j) + countPaths(i, j-1)
            self.cache[(i, j)] = ways
            return ways
        return countPaths(m-1, n-1)

'''
Bottom up
Time - O(m*n)
Space - O(m*n)
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        ways = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # One way to reach the first step - already be there
        ways[1][1] = 1
        # matrix is 1 to end (row and col). 0th col and 0th row is to avoid
        # index errors while doing i-1 and j-1 in loop
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    ways[i][j] = 0
                    continue    
                ways[i][j] = ways[i-1][j] + ways[i][j-1]
        return ways[m][n]

'''
Bottom up, space optimized
Time - O(m*n)
Space - O(n)
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # Reuse the same array again and again
        ways = [0 for _ in range(n+1)]
        # One way to reach the first step - already be there
        ways[1] = 1
        # matrix is 1 to end (row and col). 0th col and 0th row is to avoid
        # index errors while doing i-1 and j-1 in loop
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                if obstacleGrid[i-1][j-1] == 1:
                    ways[j] = 0
                    continue
                # ways[j] -> top value (stored in same box)
                # ways[j-1] -> left value
                ways[j] = ways[j] + ways[j-1]
        return ways[n]