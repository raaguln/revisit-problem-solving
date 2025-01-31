# Attempt 1
# Time - O(n)
# Space - O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(len(set(nums)) == len(nums)):
            return False
        return True

# Attempt 2 -> very bad
# Time - O(n)
# Space - O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        for n in nums:
            if(n in cache):
                return True
            cache[n] = 0
        return False

# Attempt 4 -
# Time - O(n)
# Space - O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for n in nums:
            if n in cache:
                return True
            cache.add(n)
        return False