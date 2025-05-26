'''
Time - O(2^(m + n))
- Each call may branch into up to two recursive calls (especially with '*')
- m = length of pattern p, n = length of string s
- Without memoization, many overlapping subproblems are recomputed
- Total calls can grow exponentially in the sum of lengths of s and p

Space - O(m + n)
- Maximum recursion depth is at most m + n (combined length of s and p)
- Each call adds a frame to the call stack
- No additional data structures used
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            # Base case: if pattern is exhausted
            if j == len(p):
                return i == len(s)

            # Check if current characters match (considering '.')
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # Handle '*' case
            if j + 1 < len(p) and p[j + 1] == '*':
                # Two possibilities:
                # 1) '*' means zero occurrence: skip current pattern + '*'
                # 2) '*' means one or more occurrence: if first matches, advance string index
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # No '*', just move both pointers if first matches
                return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)


'''
Bottom Up

Time - O(m * n)  
- m = length of string s, n = length of pattern p  
- Each dp state dp[i][j] computed once  
- Each state depends on constant time operations  
- Total complexity is O(m * n)

Space - O(m * n)  
- A 2D DP table of size (m+1) x (n+1) stores boolean values indicating if s[i:] matches p[j:]  
- No recursion stack used

Explanation -  
m - length of string s  
n - length of pattern p  
dp[i][j] - boolean indicating if substring s[i:] matches pattern p[j:]  

DP logic -  
QUESTION -> Does s from i to end match p from j to end?  

1. Base case:  
   - dp[m][n] = True (empty string matches empty pattern)  
2. For each position i in s and j in p from the end backwards:  
   - first_match = True if s[i] matches p[j] (either same char or '.') and i < m  
   - If next char in p (p[j+1]) is '*':  
       - Two cases:  
         a) '*' means zero occurrence of p[j]: dp[i][j] = dp[i][j+2]  
         b) '*' means one or more occurrences if first_match: dp[i][j] = dp[i+1][j]  
       - dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])  
   - Else (no '*'):  
       - dp[i][j] = first_match and dp[i+1][j+1]  
3. dp[0][0] gives final answer: whether entire s matches entire p

Table - After initialization (m=2, n=3 example):  

Indices i and j go from m to 0 and n to 0 respectively, filling dp bottom-up.

Example dp[m][n] = True (empty matches empty)  
Subproblems solved by checking matches and handling '*' cases.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j] means s[i:] matches p[j:]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty pattern matches empty string
        dp[m][n] = True
        
        # Fill the dp table bottom-up
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first_match = i < m and (s[i] == p[j] or p[j] == '.')
                
                if j + 1 < n and p[j + 1] == '*':
                    # '*' can represent zero occurrence or more if first matches
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        
        return dp[0][0]
