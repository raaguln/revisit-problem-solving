# Same, but return the string
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        def recursion(i, j):
            if i == m or j == n:
                return ""
            if text1[i] == text2[j]:
                return text1[i] + recursion(i + 1, j + 1)
            else:
                res1 = recursion(i + 1, j)
                res2 = recursion(i, j + 1)
                if len(res1) >= len(res2):
                    return res1
                else:
                    return res2
        return recursion(0, 0)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> str:
        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # Fill dp table with LCS lengths
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        # Reconstruct the LCS string from the dp table
        i, j = 0, 0
        lcs = []
        while i < m and j < n:
            if text1[i] == text2[j]:
                lcs.append(text1[i])
                i += 1
                j += 1
            elif dp[i+1][j] >= dp[i][j+1]:
                i += 1
            else:
                j += 1

        return ''.join(lcs)
