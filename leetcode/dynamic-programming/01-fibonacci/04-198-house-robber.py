'''
https://leetcode.com/problems/house-robber/description/

Brainstorm:
1. house = [], max = 0
2. house = [4], max = first element (4)
3. house = [4, 6]
    - 4 + skip 6
    - 6
   answer = 6
4. house = [4,6,3]
    - 4 + skip 6 + 3
    - 6 + skip 3
    - 3
5. house = [4,6,3,2]
    - 4 + skip 6 + 3 + skip 2
    - 6 + skip 3 + 2
    - 3 + skip 2
    - 2
We see a pattern - 
    - 4 + skip 6 + subproblem([3, 2])
    - 6 + subproblem([2])
    - 3 + subproblem([])
    - 2
'''
'''
Recursion:
Time: O(2^n)
Space: O(n)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursion(i):
            if i >= len(nums):
                return 0
            selectFirst = nums[i] + recursion(i+2)
            selectSecond = recursion(i+1)
            maxProfit = max(selectFirst, selectSecond)
            return maxProfit
        return recursion(0)
        
    
'''
Recursion, top down, memoization:
Time: O(n)
Space: O(n)
'''
class Solution:
    def __init__(self):
        self.cache = {}
    def rob(self, nums: List[int]) -> int:
        def recursion(i):
            if i >= len(nums):
                return 0
            
            # Get values from cache if there
            recursioni2 = None
            if i+2 in self.cache:
                recursioni2 = self.cache[i+2]
            else:
                recursioni2 = recursion(i+2)

            recursioni1 = None
            if i+1 in self.cache:
                recursioni1 = self.cache[i+1]
            else:
                recursioni1 = recursion(i+1)

            robFirst = nums[i] + recursioni2
            robSecond = recursioni1
            maxVal = max(robFirst, robSecond)
            self.cache[i] = maxVal
            return maxVal
        return recursion(0)

# lru cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def recursion(i):
            if i >= len(nums):
                return 0
            selectFirst = nums[i] + recursion(i+2)
            selectSecond = recursion(i+1)
            maxProfit = max(selectFirst, selectSecond)
            return maxProfit
        return recursion(0)
        

'''
Bottom up brainstorm:
house = [5, 3, 10, 10, 15]
Options - at each step - rob or not rob
1. At 1st house
    - rob 5, maxValue = 5
    - skip 5, maxValue = 0
    => maxValue = max(5, 0) = 5
    => table = [5, 0, 0, 0, 0]
2. At 2nd house
    - rob 3, maxValue = 3 (can't take previous value as it is adjacent)
    - skip 3, maxValue = 5 (from previous house)
    => maxValue = max(3, 5) = 5
    => table = [5, 5, 0, 0, 0]
3. At 3rd house
    - rob 10, maxValue = 10 + 5 = 15 (ith house + max from (i-2)th house)
    - skip 10, maxValue = 5
    => maxValue = max(15, 5) = 15
    => table = [5, 5, 15, 0, 0]
4. At 4th house
    - rob 10, maxValue = 10 + 5 = 15 (ith house + max from (i-2)th house)
    - skip 10, maxValue = 15
    => maxValue = max(15, 15) = 15
    !! both values are 15, but here we do rob the to get the immediate 10
        (won't affect our max cost, but if we need a list of items that we are robbing)
    => table = [5, 5, 15, 15, 0]
'''


'''
Iterative, bottom-up, tabulation:
Time: O(n)
Space: O(n)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        
        result = [0] * n
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])

        for i in range(2, n):
            robCurrent = nums[i] + result[i-2]
            notRobCurrent = result[i-1]
            result[i] = max(robCurrent, notRobCurrent)
        return result[-1]


'''
Iterative, bottom-up, tabulation, space optimized:
Time: O(n)
Space: O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        
        lastBeforeHouse = nums[0]
        lastHouse = max(nums[0], nums[1])

        for i in range(2, n):
            robCurrent = nums[i] + lastBeforeHouse
            notRobCurrent = lastHouse
            temp = max(robCurrent, notRobCurrent)
            lastBeforeHouse, lastHouse = lastHouse, temp 
        return lastHouse

        