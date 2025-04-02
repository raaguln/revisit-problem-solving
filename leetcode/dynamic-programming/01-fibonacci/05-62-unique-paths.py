'''
Top down recursion
Time - O(2^(m+n)) - 2^(m+n) calls
Space - O(m+n) recursion stack for m*n calls
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def pathCount(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return pathCount(i-1, j) + pathCount(i, j-1)
        return pathCount(m-1, n-1)

'''
Top down with memoization
Time - O(2^(m+n)) - 2^(m+n) calls
Space - O(m+n) recursion stack for m*n calls
'''
class Solution:
    def __init__(self):
        self.cache = {}
    def uniquePaths(self, m: int, n: int) -> int:
        def pathCount(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            if (i,j) in self.cache:
                return self.cache[(i,j)]
            count = pathCount(i-1, j) + pathCount(i, j-1) 
            self.cache[(i,j)] = count
            return count
        return pathCount(m-1, n-1)

'''
Bottom up
Time - O(m*n)
Space - O(m*n)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # One way to reach the first step - already be there
        ways[1][1] = 1
        # matrix is 1 to end (row and col). 0th col and 0th row is to avoid
        # index errors while doing i-1 and j-1 in loop
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    continue
                ways[i][j] = ways[i-1][j] + ways[i][j-1]
        return ways[m][n]

'''
Bottom up, space optimized
Time - O(m*n)
Space - O(n)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
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
                # ways[j] -> top value (stored in same box)
                # ways[j-1] -> left value
                ways[j] = ways[j] + ways[j-1]
        return ways[n]