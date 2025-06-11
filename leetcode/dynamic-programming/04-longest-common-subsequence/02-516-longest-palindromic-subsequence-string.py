# https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> str:
        n = len(s)

        def recursion(i, j):
            # Base case: invalid range
            if i > j:
                return ""
            # Base case: single character
            if i == j:
                return s[i]
            # Characters match, add them and recurse inward
            if s[i] == s[j]:
                return s[i] + recursion(i + 1, j - 1) + s[j]
            # Characters don't match, pick the longer subsequence by skipping either end
            left = recursion(i + 1, j)
            right = recursion(i, j - 1)
            return left if len(left) >= len(right) else right

        return recursion(0, n - 1)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        # For reconstructing the subsequence
        seq = [[""] * n for _ in range(n)]

        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
            seq[i][i] = s[i]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + (dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
                    seq[i][j] = s[i] + (seq[i + 1][j - 1] if i + 1 <= j - 1 else "") + s[j]
                else:
                    if dp[i + 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i + 1][j]
                        seq[i][j] = seq[i + 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]
                        seq[i][j] = seq[i][j - 1]

        return seq[0][n - 1]
