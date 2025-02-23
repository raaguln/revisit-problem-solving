'''
Brainstorm:
Options for stes we can take - 1 or 2
1. If n <= 0 => ways = 0
2. If n == 1 => ways = 1 (1 step from ground)
3. If n == 2 => ways = 2 (1 or 2 step from ground)
4. If n == 3 => ways = 3
    - 1, 1, 1
    - 1, 2
    - 2, 1
    Also note - Since steps = [1, 2] only, we need to reach the previous
    two levels (n=2 or n=1) to be able to climb to the current level (n=3).
    So, the number of ways to climb to the current level is the sum of n=2 and n=1.
5. If n == 4 => ways = 5
    - 1, 1, 1, 1
    - 1, 1, 2
    - 1, 2, 1
    - 2, 1, 1
    - 2, 2
    So, the number of ways to climb to the current level is the sum of n=3 and n=2.
'''
'''
Iterative, bottom-up, space optimized
Time complexity: O(n)
Space complexity: O(1)

Notes:
1. n+2 because n=1 in climbing stairs == n=2 in fibonacci
'''
# Top-down
# Time: O(2^n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        def recursion(step):
            if step <= 0:
                # 1 way to climb
                return 1
            if step == 1:
                return 1
            oneStep = recursion(step-1)
            twoStep = recursion(step-2)
            return oneStep + twoStep

        ways = recursion(n)
        return ways
    
# Top down with memoization
# Time: O(n)
# Space: O(n)
class Solution:
    def __init__(self):
        self.cache = {}
    
    def climbStairs(self, n: int) -> int:
        def recursion(step):
            if step in self.cache:
                return self.cache[step]
            if step <= 0:
                # 1 way to climb
                return 1
            if step == 1:
                return 1
            oneStep = recursion(step-1)
            twoStep = recursion(step-2)

            ways = oneStep + twoStep
            self.cache[step] = ways

            return ways

        ways = recursion(n)
        return ways
    
# Bottom-up
# Time: O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {
            0: 1,
            1: 1
        }
        for step in range(2, n+1):
            cache[step] = cache[step-1] + cache[step-2]
        return cache[n]
    

# Bottom-up, space optimized
# Time: O(n)
# Space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        first, second = 1, 1
        for step in range(2, n+1):
            temp = first + second
            first, second = second, temp
        return second