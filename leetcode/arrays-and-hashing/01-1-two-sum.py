# Time Complexity: O(n^2)
# Space Complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Time Complexity: O(n)
# Space Complexity: O(n)            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in cache:
                return [cache[diff], i]
            cache[nums[i]] = i
        