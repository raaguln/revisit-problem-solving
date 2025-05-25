'''
Top Down Unoptimized

Time - O(3^(m + n))
- At each step (when characters don't match), three recursive calls are made: insert, delete, replace
- Maximum recursion depth is O(m + n)
- Number of unique subproblems is O(m * n), but they are recomputed due to lack of memoization
- Total number of calls grows exponentially with branching factor of 3

Space - O(m + n)
- Maximum recursive depth is O(m + n) in the worst case
- Each recursive call adds a frame to the call stack
- No additional space used (no memoization or DP table)
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dfs(i, j):
            # If one word is exhausted, the rest of the other must be inserted or deleted
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                # Characters match, move both pointers
                return dfs(i + 1, j + 1)
            else:
                # Option 1: Insert word2[j] into word1 (advance j)
                insert_op = 1 + dfs(i, j + 1)
                # Option 2: Delete word1[i] (advance i)
                delete_op = 1 + dfs(i + 1, j)
                # Option 3: Replace word1[i] with word2[j] (advance both)
                replace_op = 1 + dfs(i + 1, j + 1)
                return min(insert_op, delete_op, replace_op)

        return dfs(0, 0)

'''
Bottom Up Optimized

Time - O(m * n)  
- We fill a 2D DP table of size (m+1) x (n+1)  
- Each cell takes constant time to compute  
- Total operations = O(m * n)

Space - O(m * n)  
- DP table of size (m+1) x (n+1)  
- No extra space used beyond this table

Explanation -  
i - index in word1  
j - index in word2  

DP logic -  
QUESTION -> What is the minimum number of edit operations (insert, delete, replace) to convert word1[i:] to word2[j:]?

1. If word1[i] == word2[j]:  
   - Characters match → no edit needed → dp[i][j] = dp[i+1][j+1]  
2. If word1[i] != word2[j]:  
   - Three possible operations:  
     - Insert word2[j] → dp[i][j+1] + 1  
     - Delete word1[i] → dp[i+1][j] + 1  
     - Replace word1[i] with word2[j] → dp[i+1][j+1] + 1  
   - Take the operation with the minimum cost  

Base Case Initialization -  
- If i == m (word1 exhausted): need to insert all remaining characters of word2 → dp[m][j] = n - j  
- If j == n (word2 exhausted): need to delete all remaining characters of word1 → dp[i][n] = m - i  

Table - Step 0 after initialization of base cases (example m=3, n=3) →  
Rows represent suffixes of word1, columns represent suffixes of word2, values = min edit distance  

     ""   a    c    t  
"" | 3 | 2 | 1 | 0  
c  | 2 |   |   |  
a  | 1 |   |   |  
t  | 0 |   |   |  
↑  
word1 = "tac", word2 = "tac"
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # dp[i][j] will represent the min edit distance between word1[i:] and word2[j:]
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # Fill base cases:
        # If word1 is exhausted, all remaining characters in word2 need to be inserted
        for j in range(n + 1):
            dp[m][j] = n - j
        # If word2 is exhausted, all remaining characters in word1 need to be deleted
        for i in range(m + 1):
            dp[i][n] = m - i

        # Fill the table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    insert_op = 1 + dp[i][j + 1]
                    delete_op = 1 + dp[i + 1][j]
                    replace_op = 1 + dp[i + 1][j + 1]
                    dp[i][j] = min(insert_op, delete_op, replace_op)

        return dp[0][0]