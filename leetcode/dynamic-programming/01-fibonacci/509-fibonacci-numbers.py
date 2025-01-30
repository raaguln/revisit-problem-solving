'''
1. Recursive
Time complexity: O(2^n)
Space complexity: O(n)
'''
class Solution:
    def fib(self, n: int) -> int:
        # Recursive
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)