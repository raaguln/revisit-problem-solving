'''
Top Down Unoptimized

Time - O(2^(m + n))
- In the worst case, each `'*'` leads to two recursive calls: match zero (`dfs(i, j+1)`) or one+ (`dfs(i+1, j)`)
- The maximum recursion depth is O(m + n)
- No memoization, so many overlapping subproblems are recomputed
- Exponential number of recursive calls due to branching at each `'*'`

Space - O(m + n)
- Maximum recursive depth is O(m + n) in the worst case
- Each recursive call adds a frame to the call stack
- No additional space used (no memoization or DP table)
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            # If both strings are fully matched
            if i == len(s) and j == len(p):
                return True
            # If pattern is exhausted but s is not
            if j == len(p):
                return False
            # If string is exhausted but pattern has remaining characters
            if i == len(s):
                # Remaining pattern characters must all be '*'
                for k in range(j, len(p)):
                    if p[k] != '*':
                        return False
                return True

            if p[j] == s[i] or p[j] == '?':
                return dfs(i + 1, j + 1)
            elif p[j] == '*':
                # '*' matches zero characters or one character and continues
                return dfs(i, j + 1) or dfs(i + 1, j)
            else:
                return False

        return dfs(0, 0)

'''
Bottom Up Optimized

Time - O(m * n)  
- We fill a DP table of size (m+1) x (n+1)  
- Each cell is computed in constant time  
- Total operations = O(m * n)

Space - O(m * n)  
- DP table of size (m+1) x (n+1)  
- No extra space beyond this table

Explanation -  
i - index in s  
j - index in p  

DP logic -  
QUESTION -> Does the substring s[i:] match the pattern p[j:]?

1. If p[j] == s[i] or p[j] == '?':  
   - Current characters match → check if rest matches → dp[i][j] = dp[i+1][j+1]  
2. If p[j] == '*':  
   - '*' can match empty → dp[i][j+1]  
   - '*' can match one or more characters → dp[i+1][j]  
   - Combine both: dp[i][j] = dp[i+1][j] or dp[i][j+1]  
3. If characters don't match and no wildcard → dp[i][j] = False  

Base Case Initialization -  
- dp[m][n] = True (empty string matches empty pattern)  
- When s is exhausted (i = m), remaining pattern must be all '*' to be valid  
  → dp[m][j] = True if p[j:] is all '*'  
  → Otherwise False  

Table - Step 0 after initialization of base cases (example m=3, n=3) →  
Rows represent suffixes of s, columns represent suffixes of p, values = match status (True/False)  

     ""   *    ?    a  
"" | T | T | F | F  
c  |   |   |   |  
b  |   |   |   |  
a  |   |   |   |  
↑  
s = "abc", p = "a?*"
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: empty string matches empty pattern
        dp[m][n] = True

        # Fill the last row: s is exhausted, check if remaining p are all '*'
        for j in range(n - 1, -1, -1):
            if p[j] == '*':
                dp[m][j] = dp[m][j + 1]
            else:
                dp[m][j] = False

        # Fill the dp table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if p[j] == s[i] or p[j] == '?':
                    dp[i][j] = dp[i + 1][j + 1]
                elif p[j] == '*':
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]
                else:
                    dp[i][j] = False

        return dp[0][0]
