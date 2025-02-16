# Attempt 0
# Time: O(n^2)
# Space: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
# Time - O(n)
# Space - O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        for k, v in counter.items():
            if(v > 1):
                return True
        return False

# Time - O(n)
# Space - O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            if(counter[n] > 1):
                return True


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