'''
Top Down Unoptimized

Time - O(2^(m + n))
- At each step, two recursive calls are made: (i+1, j) and (i, j+1)
- Maximum recursion depth is O(m + n)
- Number of unique subproblems is O(m * n), but no caching/memoization used
- Each recursive call creates new strings via concatenation, adding extra overhead
- Overall exponential due to recomputation and string concatenations

Space - O(m + n)
- Maximum recursion depth is O(m + n)
- Each call holds a substring concatenation, potentially increasing memory usage
- No memoization cache used, so no extra DP table space
'''
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def dfs(i, j):
            # If str1 is exhausted, return the rest of str2
            if i == len(str1):
                return str2[j:]
            # If str2 is exhausted, return the rest of str1
            if j == len(str2):
                return str1[i:]
            # Characters match, include it once
            if str1[i] == str2[j]:
                return str1[i] + dfs(i + 1, j + 1)
            # Characters don't match, try both insertions
            option1 = str1[i] + dfs(i + 1, j)
            option2 = str2[j] + dfs(i, j + 1)
            if len(option1) <= len(option2):
                return option1 
            else:
                return option2
        
        return dfs(0, 0)


'''
Bottom Up Optimized - MLE!!

Time - O(m * n * max(m, n))  
- We fill a DP table of size (m+1) x (n+1)  
- Each cell concatenates strings which can take up to O(max(m, n)) time  
- Total complexity is O(m * n * max(m, n))

Space - O(m * n * max(m, n))  
- DP table stores strings that can be as long as m + n in worst case  
- Hence, total space depends on size of strings stored in each cell

Explanation -  
i - index in str1  
j - index in str2  

DP logic -  
QUESTION -> What is the shortest common supersequence (SCS) of str1[i:] and str2[j:]?

1. If str1[i] == str2[j]:  
   - Characters match → include the character once and proceed →  
     dp[i][j] = str1[i] + dp[i+1][j+1]  
2. If str1[i] != str2[j]:  
   - Two options:  
     - Include str1[i], then solve for dp[i+1][j] → option1  
     - Include str2[j], then solve for dp[i][j+1] → option2  
   - Take the option with the shorter resulting supersequence  
   - dp[i][j] = shorter of option1 and option2  

Base Case Initialization -  
- If j == n (str2 exhausted): remaining substring is str1[i:] → dp[i][n] = str1[i:]  
- If i == m (str1 exhausted): remaining substring is str2[j:] → dp[m][j] = str2[j:]  

Table - Step 0 after initialization of base cases (example m=3, n=3) →  
Rows represent str1 indices, columns represent str2 indices, each cell holds shortest supersequence from i, j onward  

Example (str1 = "abc", str2 = "acd"):  
 dp[m][j]: "", "d", "cd", "acd"  
 dp[i][n]: "abc", "bc", "c", ""  
'''
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

        # Initialize base cases
        for i in range(m - 1, -1, -1):
            dp[i][n] = str1[i:]  # If str2 is exhausted, append remaining str1
        for j in range(n - 1, -1, -1):
            dp[m][j] = str2[j:]  # If str1 is exhausted, append remaining str2

        # Fill dp bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = str1[i] + dp[i + 1][j + 1]
                else:
                    option1 = str1[i] + dp[i + 1][j]
                    option2 = str2[j] + dp[i][j + 1]
                    dp[i][j] = option1 if len(option1) <= len(option2) else option2

        return dp[0][0]

'''
Bottom up optimized - WORKS
Don't store the entire string into the DP table
'''
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        # dp[i][j] stores length of shortest supersequence of str1[i:] and str2[j:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][n] = m - i
        for j in range(n + 1):
            dp[m][j] = n - j

        # Fill dp with lengths only
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])

        # Reconstruct the shortest supersequence string from dp table
        i, j = 0, 0
        result = []
        while i < m and j < n:
            if str1[i] == str2[j]:
                result.append(str1[i])
                i += 1
                j += 1
            else:
                if dp[i + 1][j] < dp[i][j + 1]:
                    result.append(str1[i])
                    i += 1
                else:
                    result.append(str2[j])
                    j += 1

        # Append remaining characters
        result.append(str1[i:])
        result.append(str2[j:])

        return "".join(result)
