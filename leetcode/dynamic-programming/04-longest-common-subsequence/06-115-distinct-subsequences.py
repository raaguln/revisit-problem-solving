'''
Top Down Unoptimized

Time - O(2^m)
- At each step, two recursive calls may be made: (i+1, j+1) and (i+1, j)
- Maximum recursion depth is O(m)
- Number of unique subproblems is O(m * n), but no memoization is used
- Exponential recomputation of overlapping subproblems

Space - O(m)
- Maximum recursion depth is O(m) in the worst case
- Each recursive call adds a frame to the call stack
- No additional space used (no memoization or DP table)
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        dfs(i, j) returns number of distinct subsequences in s[i:] that match t[j:].
        If j == len(t), full match → return 1.
        If i == len(s) but not matched fully → return 0.
        If characters match, recurse both by including and excluding current char.
        If characters don't match, only skip char in s.
        '''
        m, n = len(s), len(t)

        def dfs(i, j):
            # If we've matched all characters in t
            if j == n:
                return 1
            # If s is exhausted but t is not
            if i == m:
                return 0
            
            count = 0
            if s[i] == t[j]:
                # Option 1: match current characters and move both pointers
                count += dfs(i + 1, j + 1)
            # Option 2: skip current char in s
            count += dfs(i + 1, j)
            
            return count
        
        return dfs(0, 0)

'''
Bottom Up Optimized

Time - O(m * n)  
- We fill a DP table of size (m+1) x (n+1)  
- Each cell is computed in constant time  
- Total operations = O(m * n)

Space - O(m * n)  
- DP table of dimensions (m+1) x (n+1)  
- No extra space used beyond this table

Explanation -  
i - index in s  
j - index in t  

DP logic -  
QUESTION -> How many distinct subsequences of s[i:] match t[j:]?

1. If s[i] == t[j]:  
   - Two options:  
     - Use s[i] to match t[j] → dp[i+1][j+1]  
     - Skip s[i] and try to match t[j] → dp[i+1][j]  
   - Total ways = dp[i+1][j+1] + dp[i+1][j]  
2. If s[i] != t[j]:  
   - Can't use s[i], so skip it → dp[i+1][j]  

Base Case Initialization -  
- If t[j:] is empty (j == n), there is exactly 1 way to match it (delete all characters in s[i:]) → dp[i][n] = 1  
- If s[i:] is empty and t[j:] is not → no way to match → default dp[i][j] = 0  

Table - Step 0 after initialization of base cases (example m=3, n=2) →  
Rows represent s[i:], columns represent t[j:], values are number of distinct subsequences  

     ""   b    c  
"" | 1 | 0 | 0  
 a | 1 |   |    
 b | 1 |   |    
 b | 1 |   |    
↑  
s = "abb", t = "bc"
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[i][j] will store the number of distinct subsequences in s[i:] that match t[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: an empty t can be matched by any suffix of s in exactly 1 way (by deleting all characters)
        for i in range(m + 1):
            dp[i][n] = 1

        # Fill the table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    # If characters match: include it + skip it
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    # If characters don't match: skip character in s
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]