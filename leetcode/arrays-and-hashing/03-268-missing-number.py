# https://leetcode.com/problems/missing-number/description/
# Time: O(nlogn)
# Space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

# Time: O(n)
# Space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
    
