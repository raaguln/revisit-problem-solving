# https://leetcode.com/problems/n-th-tribonacci-number/description/
# Top down (TLE)
# Time complexity: O(3^n) - 3 calls for each number
# Space complexity: O(n) - max depth of recursion stack
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return (
            self.tribonacci(n-1) + 
            self.tribonacci(n-2) + 
            self.tribonacci(n-3)
        )
    
# Top down, memoization
# Time complexity: O(n) - each number is calculated only once and stored in cache
# Space complexity: O(n)
class Solution:
    def __init__(self):
        self.cache = {}
    
    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        value = (
            self.tribonacci(n-1) + 
            self.tribonacci(n-2) + 
            self.tribonacci(n-3)
        )
        self.cache[n] = value
        return value

# Bottom up, iterative
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {
            0: 0,
            1: 1,
            2: 1,
        }
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
        return cache[n]

# Bottom up, iterative, space optimized
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        first, second, third = 0, 1, 1
        for i in range(3, n+1):
            temp = first + second + third
            first, second, third = second, third, temp
        return third