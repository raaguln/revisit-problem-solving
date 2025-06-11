'''
https://leetcode.com/problems/longest-common-subsequence/description/

Subsequences - 
- maintains order
- can be contigious or non-contigious
Eg: {1,3,2}
{1,2}, {3,2} -> subsequence
{2,1} -> not subsequence

Substring / Subarray - 
- maintains order
- always contigious
Eg: "abcdef"
"cde" - substring
"ace" - not substring
'''

'''
Top down, unoptimized - TLE
Time - O(2^(m + n))
- At each step, two recursive calls are made: (i+1, j) and (i, j+1)
- Maximum depth of recursion is O(m + n)
- Number of unique subproblems is O(m * n), but results are not cached
- Total number of calls grows exponentially without memoization

Space - O(m + n)
- Recursive depth is at most `m + n` in the worst case
- Each recursive call adds a frame to the call stack
- No additional space (no memoization or DP table used)
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        def recursion(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + recursion(i+1, j+1)
            else:
                return max(
                    recursion(i+1, j),
                    recursion(i, j+1)
                )
        return recursion(0, 0)

'''
Top down, optimized
Time - O(m * n)
- Each unique subproblem (i, j) is solved only once due to caching
- There are at most m * n unique subproblems (i from 0 to m, j from 0 to n)
- Each subproblem does O(1) work besides recursive calls

Space - O(m * n)
- Cache stores results for up to m * n subproblems
- Maximum recursion depth is O(m + n)
- Call stack frames use space proportional to recursion depth
'''
from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = {}
        @lru_cache(None)
        def recursion(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + recursion(i+1, j+1)
            else:
                return max(
                    recursion(i+1, j),
                    recursion(i, j+1)
                )
        return recursion(0, 0)

        

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

"""
Time - O(m * n)
Space - O(m * n)

Explanation -  
i - index in text1  
j - index in text2  

DP logic -  
QUESTION -> What is the length of the longest common subsequence between text1[i:] and text2[j:]?

1. If text1[i] == text2[j]:  
    - Characters match → Include this character → dp[i][j] = 1 + dp[i+1][j+1]  
2. If text1[i] != text2[j]:  
    - We skip one character (either from text1 or text2)  
    - Try both options and take the max:
        - Skip text1[i] → dp[i+1][j]
        - Skip text2[j] → dp[i][j+1]  
    - dp[i][j] = max(dp[i+1][j], dp[i][j+1])

Base Case Initialization -  
- If either string is exhausted, LCS = 0  
- So we initialize dp[m][*] = 0 and dp[*][n] = 0  

Table - Step 0 after base case initialization (m = 3, n = 3 example) →  
  ""  d   o   g  
""[0][0][0][0]  
c [0][ ][ ][ ]  
a [0][ ][ ][ ]  
t [0][ ][ ][ ]  
↑  
text1 → "cat"
"""

'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

'''
Bottom up optimized
Time - O(m * n)
- Two nested loops iterate over m and n respectively
- Each iteration performs O(1) operations (comparison and max)

Space - O(n)
- Uses a single 1D array of size n+1 for DP
- Only constant extra space (`prev`, `temp`) used per iteration
- Optimizes space from O(m * n) to O(n)
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n+1)
        
        for i in range(m-1, -1, -1):
            prev = 0
            for j in range(n-1, -1, -1):
                # Save current dp[j] before overwriting (dp[i+1][j])
                temp = dp[j]

                if text1[i] == text2[j]:
                    dp[j] = 1 + prev  # prev holds dp[i+1][j+1]
                else:
                    dp[j] = max(dp[j], dp[j + 1])  # max(dp[i+1][j], dp[i][j+1])
                
                # Update prev for next j
                prev = temp
        return dp[0]

        
        