
'''
Top Down Unoptimized

Time - O(2^n)
- At each step, two recursive calls are made: (i+1, j) and (i, j-1)
- Maximum depth of recursion is O(n)
- Number of unique subproblems is O(n^2), but results are not cached
- Total number of recursive calls grows exponentially due to recomputation

Space - O(n)
- Maximum recursive depth is O(n) in the worst case
- Each recursive call adds a frame to the call stack
- No additional space used (no memoization or DP table)
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        def recursion(i, j):
            # Base case: single character
            if i == j:
                return 1
            # Base case: invalid range
            if i > j:
                return 0
            # Characters match, add 2 and recurse inward
            if s[i] == s[j]:
                return 2 + recursion(i+1, j-1)
            # Characters don't match, take max of skipping either end
            return max(
                recursion(i+1, j),
                recursion(i, j-1)
            )

        return recursion(0, n-1)
        
'''
Bottom Up Unoptimized

Time - O(n^2)
- Two nested loops each run up to n times (i from n-1 to 0, j from i+1 to n-1)
- Each cell dp[i][j] is computed once with O(1) work per iteration

Space - O(n^2)
- A 2D DP table of size n x n is used to store results of subproblems
- No recursion, so no call stack space used
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
  