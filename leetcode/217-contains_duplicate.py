# Attempt 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(set(nums)) == len(nums)):
            return False
        return True

# Attempt 2 -> very bad
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for n in nums:
            if(n in cache):
                return True
            cache[n] = 0
        return False

# Attempt 3 - TIME LIMIT EXCEEDED
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        while(len(nums)):
            n = nums.pop()
            if(n in nums):
                return True
        return False

# Attempt 4 -
# Time - better than #1
# Space - worse than #1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for n in nums:
            if n in cache:
                return True
            cache.add(n)
        return False