'''
https://leetcode.com/problems/triangle/description/

Time - O(2^n)
- At each level, two recursive calls are made (except the last row)
- Maximum recursion depth is n (number of rows)
- Without memoization, the number of calls doubles roughly at each level
- Total calls grow exponentially: O(2^n)

Space - O(n)
- Maximum recursion depth is n (height of the triangle)
- Each recursive call adds one frame to the call stack
- No additional data structures used
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        def dfs(row, col):
            # Base case: if we reach the last row, just return the value at that position
            if row == n - 1:
                return triangle[row][col]

            # Recur for the two possible next positions in the row below
            return triangle[row][col] + min(
                dfs(row + 1, col),     # Move down to same index
                dfs(row + 1, col + 1)  # Move down to next index
            )

        # Start from the top of the triangle (0, 0)
        return dfs(0, 0)

'''
Bottom Up Optimized (Space Optimized)

Time - O(n^2)  
- Each element in the triangle is processed exactly once  
- For each element, a constant time calculation is done to find the minimum of two adjacent elements below  
- Total operations proportional to total elements, which is about n(n+1)/2 ≈ O(n^2)

Space - O(n)  
- A 1D DP array is used, initially copied from the last row of the triangle  
- The DP array is updated in-place from bottom to top, reducing space from O(n^2) to O(n)  
- No recursion stack space used

Explanation -  
n - number of rows in the triangle  
row - current row being processed, from bottom up  
col - index of the element in the current row  

DP logic -  
QUESTION -> What is the minimum path sum starting at triangle[row][col] going downwards?  

1. Base case:  
   - dp initially stores the last row of the triangle  
2. For each element in row above:  
   - dp[col] = triangle[row][col] + min(dp[col], dp[col+1])  
   - This chooses the minimum path sum by picking the smaller of two adjacent numbers in the row below  
3. After processing up to the first row, dp[0] contains the minimum path sum from top to bottom

Table - Step 0 after initialization of base case (last row):

triangle:
      2  
     3 4  
    6 5 7  
   4 1 8 3  

dp after initialization:  
[4, 1, 8, 3]

After processing row 2 (6,5,7):  
dp = [6+min(4,1), 5+min(1,8), 7+min(8,3)]  
dp = [6+1=7, 5+1=6, 7+3=10, 3] (last value useless)

After processing row 1 (3,4):  
dp = [3+min(7,6), 4+min(6,10)]  
dp = [3+6=9, 4+6=10, 10, 3] (last 2 values useless)

After processing row 0 (2):  
dp = [2+min(9,10)]  
dp = [11, 10, 10, 3] (last 3 values useless)

Answer = dp[0] = 11
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # Create a dp array copying the last row of the triangle (base case)
        dp = triangle[-1][:]

        # Iterate from the second last row up to the first row
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                # For each element, add its value to the minimum of the two adjacent numbers in the row below
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        # dp[0] will hold the minimum path sum from top to bottom
        return dp[0]
