# https://leetcode.com/problems/minimum-path-sum/
'''
Top Down Unoptimized (Recursive without memoization)

Time - Exponential (O(2^(m+n)))
- At each cell, two recursive calls are made: up and left
- This leads to a large number of repeated subproblems

Space - O(m + n)
- Due to recursion stack in worst case
- Maximum depth is `m + n` (from bottom-right to top-left)
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def computePathCost(i, j):
            if i < 0 or j < 0:
                return float("inf")
            if i == 0 and j == 0:
                return grid[i][j]
            return grid[i][j] + min(
                computePathCost(i-1, j),
                computePathCost(i, j-1)
            )
        
        return computePathCost(m-1, n-1)

'''
Top down optimized
Time - O(m * n)
- Each unique cell (i, j) is computed only once due to memoization
- There are m * n unique subproblems in total
- Each subproblem takes constant time to compute (excluding recursive calls already cached)

Space - O(m * n)
- Memoization cache stores results for m * n cells
- Recursive depth is at most m + n in the worst case
- Call stack can grow to O(m + n) due to recursion
- Overall space is dominated by the cache: O(m * n)
'''
class Solution:
    def __init__(self):
        self.cache = {}
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def computePathCost(i, j):
            if i < 0 or j < 0:
                return float("inf")
            if i == 0 and j == 0:
                return grid[i][j]
            if (i, j) in self.cache:
                return self.cache[(i, j)]
            cost = grid[i][j] + min(
                computePathCost(i-1, j),
                computePathCost(i, j-1)
            )
            self.cache[(i, j)] = cost
            return cost
        
        return computePathCost(m-1, n-1)


'''
Bottom Up Optimized

Time - O(m * n)  
- Each cell in the grid is visited exactly once  
- For every cell (i, j), we compute the minimum path sum in constant time  
- Total operations = m * n

Space - O(m * n)  
- A 2D DP table of size m x n is used  
- Each dp[i][j] stores the minimum sum to reach cell (i, j)  
- No recursion, so no extra call stack space used

Explanation -  
i - row index in the grid  
j - column index in the grid  

DP logic -  
QUESTION -> What is the minimum path sum to reach cell (i, j) from (0, 0)?  

1. If i == 0 and j == 0 →  
    - Base case: only one cell, dp[0][0] = grid[0][0]  
2. Else →  
    - Take the minimum path sum from either the top or left neighbor  
    - up = dp[i-1][j] if i > 0 else inf  
    - left = dp[i][j-1] if j > 0 else inf  
    - dp[i][j] = grid[i][j] + min(up, left)

Table - Step 0 after initialization of base case →  
(Example 3x3 grid)

    1   3   1  
    1   5   1  
    4   2   1  

    DP Table after Step 0:

     1    0    0  
     0    0    0  
     0    0    0  

After first row fill:

     1    4    5  
     0    0    0  
     0    0    0  

Final DP table:

     1    4    5  
     2    7    6  
     6    8    7  

Answer = dp[2][2] = 7
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]  # Initialize a 2D array for DP

        # Initialize first cell
        dp[0][0] = grid[0][0]
        
        # Initialize first row (can only come from left)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Initialize first column (can only come from above)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Fill the rest of the dp table
        for i in range(1, m):
            for j in range(1, n):
                up = dp[i-1][j]
                left = dp[i][j-1]
                dp[i][j] = grid[i][j] + min(up, left)
        
        return dp[m-1][n-1]
