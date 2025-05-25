'''
Top Down Unoptimized

Time - O(2^n)
- At each step, two recursive calls are made: (i+1, j) and (i, j-1)
- Maximum depth of recursion is O(n)
- Number of unique subproblems is O(n^2), but results are not cached
- Total number of recursive calls is exponential due to overlapping subproblems and no memoization

Space - O(n)
- Maximum recursive depth is O(n) in the worst case
- Each recursive call adds a frame to the call stack
- No additional space used (no memoization or DP table)
'''
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)

        def recursion(i, j):
            # already a palindrome or empty
            if i >= j:
                return 0  
            if s[i] == s[j]:
                return recursion(i + 1, j - 1)
            # insert at either end, take min
            return 1 + min(
                recursion(i + 1, j),
                recursion(i, j - 1)
            )

        return recursion(0, n-1)
