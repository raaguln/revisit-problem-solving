# https://leetcode.com/problems/delete-operation-for-two-strings/
'''
Top Down Unoptimized

Time - O(2^(m + n))
- At each step, two recursive calls are made: (i+1, j) and (i, j+1)
- Maximum recursion depth is O(m + n)
- Number of unique subproblems is O(m * n), but they are recomputed due to lack of memoization
- Total number of calls grows exponentially with input size

Space - O(m + n)
- Maximum recursive depth is O(m + n)
- Each recursive call adds a frame to the call stack
- No additional space used (no memoization or DP table)
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i, j):
            # If either string is empty, delete all characters from the other
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            # Characters match, no deletion needed
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            # Try deleting from either word1 or word2
            return 1 + min(dfs(i + 1, j), dfs(i, j + 1))
        
        return dfs(0, 0)


'''
Bottom Up Optimized

Time - O(m * n)  
- We fill a 2D DP table of size (m+1) x (n+1)  
- Each cell takes constant time to compute  
- Total operations = O(m * n)

Space - O(m * n)  
- DP table is of size (m+1) x (n+1)  
- No additional space used apart from the table  

Explanation -  
i - index in word1  
j - index in word2  

DP logic -  
QUESTION -> What is the minimum number of deletions needed to make word1[i:] and word2[j:] equal?

1. If word1[i] == word2[j]:  
    - Characters match → No deletion needed → dp[i][j] = dp[i+1][j+1]  
2. If word1[i] != word2[j]:  
    - We must delete one character  
    - Either delete word1[i] → dp[i+1][j]  
    - Or delete word2[j] → dp[i][j+1]  
    - Take minimum of the two options + 1 deletion cost  

Base Case Initialization -  
- If i == m (word1 is exhausted): delete remaining chars in word2 → dp[m][j] = n - j  
- If j == n (word2 is exhausted): delete remaining chars in word1 → dp[i][n] = m - i  

Table - Step 0 after initialization of base cases (m = 3, n = 3 example) →  
  ""  d   o   g  
""[3][2][1][0]  
c [2][ ][ ][ ]  
a [1][ ][ ][ ]  
t [0][ ][ ][ ]  
↑  
word1 → "cat"
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # Base case: if one string is empty, delete all characters from the other
        for i in range(m + 1):
            dp[i][n] = m - i  # delete remaining from word1
        for j in range(n + 1):
            dp[m][j] = n - j  # delete remaining from word2

        # Fill the table from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])

        return dp[0][0]
