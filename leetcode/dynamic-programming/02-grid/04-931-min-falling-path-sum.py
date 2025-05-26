'''
Top Down Unoptimized (Recursive without memoization)

Time - Exponential: O(3^n)
- At each cell, up to three recursive calls are made (down-left, down, down-right)
- Maximum depth of recursion is `n` (number of rows)
- No memoization leads to repeated subproblems, causing exponential growth

Space - O(n)
- Recursion stack depth is at most `n` (number of rows)
- No additional space used apart from recursion stack
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        def dfs(row, col):
            if col < 0 or col >= n:
                return float('inf')  # Out of bounds
            if row == n - 1:
                return matrix[row][col]  # Base case: last row

            # Recur for the three possible next steps
            return matrix[row][col] + min(
                dfs(row + 1, col - 1),
                dfs(row + 1, col),
                dfs(row + 1, col + 1)
            )

        # Try all starting points in the first row
        return min(dfs(0, col) for col in range(n))

'''
Bottom Up Optimized

Time - O(n^2)  
- Each cell in the n x n matrix is processed once  
- For each cell, checking up to 3 adjacent cells below takes constant time  
- Total operations = n * n * 3 = O(n^2)

Space - O(n^2)  
- A 2D DP table of size n x n is maintained  
- dp[i][j] stores the minimum falling path sum starting at cell (i, j)  
- No recursion, so no extra call stack space

Explanation -  
i - row index in the matrix (from bottom to top)  
j - column index in the matrix  

DP logic -  
QUESTION -> What is the minimum falling path sum starting at cell (i, j)?  

1. Base case:  
   - For the last row i = n-1, dp[i][j] = matrix[i][j] (only one choice, itself)  
2. For other rows from bottom to top:  
   - dp[i][j] = matrix[i][j] + min of the three possible moves in the next row:  
     - down-left: dp[i+1][j-1] (if valid)  
     - down: dp[i+1][j]  
     - down-right: dp[i+1][j+1] (if valid)  

Answer -  
- The minimum value in the top row dp[0][j] for j in [0, n-1] is the minimum falling path sum

Table - Step 0 after initialization of base case (last row):

matrix:
   2   1   3  
   6   5   4  
   7   8   9  

dp after last row initialized:  
   0   0   0  
   0   0   0  
   7   8   9  

After filling second row up:

   0   0   0  
  11  10  13  
   7   8   9  

After filling first row up:

  12  11  14  
  11  10  13  
   7   8   9  

Answer = min(dp[0]) = 11
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # Create dp array with same size as matrix
        dp = [[0] * n for _ in range(n)]

        # Initialize last row of dp with the last row of matrix (base case)
        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]

        # Build dp table from bottom to top
        for i in range(n-2, -1, -1):
            for j in range(n):
                # Consider all possible moves down-left, down, down-right
                down_left = dp[i+1][j-1] if j-1 >= 0 else float('inf')
                down = dp[i+1][j]
                down_right = dp[i+1][j+1] if j+1 < n else float('inf')

                dp[i][j] = matrix[i][j] + min(down_left, down, down_right)

        # The answer is the minimum value in the first row of dp
        return min(dp[0])
