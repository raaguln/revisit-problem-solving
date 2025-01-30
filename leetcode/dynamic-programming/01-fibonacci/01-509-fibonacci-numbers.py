'''
1. Recursive, top down
Time complexity: O(2^n) - each call branches into 2 calls, binary tree of depth n, and 2n nodes
Space complexity: O(n) - maximum depth of the recursion stack (reaches upto depth n)
'''
class Solution:
    def fib(self, n: int) -> int:
        # Recursive
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)
    
'''
2. Recursive, top down, memoization
Time complexity: O(n) - number of non-memoized calls is n
Space complexity: O(n)
'''
class Solution:
    def __init__(self):
        self.cache = {}
    def fib(self, n: int) -> int:
        # Recursive, memoized
        if n in self.cache:
            return self.cache[n]
        if n == 0:
            return 0
        if n <= 2:
            return 1
        value = self.fib(n-1) + self.fib(n-2)
        self.cache[n] = value
        return value

'''
3. Iterative, bottom-up
Time complexity: O(n) - loop runs n times
Space complexity: O(n)

Notes - 
1. range(2, n+1) - range needs to be n+1 because we need to calculate the nth fibonacci number
'''
class Solution:
    def fib(self, n: int) -> int:
        # bottom up DP
        cache = {
            0: 0,
            1: 1
        }
        for i in range(2, n+1):
            value = cache[i-1] + cache[i-2]
            cache[i] = value
        return cache[n]
    
'''
4. Iterative, bottom-up, space optimized
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def fib(self, n: int) -> int:
        # bottom up DP with 2 variables
        if n == 0:
            return 0
        first, second = 0, 1
        for i in range(2, n+1):
            temp = first + second
            first, second = second, temp
        return second