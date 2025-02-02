# Time: O(logn)
# Space: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(target):
            l, r = 0, len(nums)
            while l < r:
                m = (l+r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l
        start = binarySearch(target)
        end = binarySearch(target + 1) - 1
        
        if start < len(nums) and nums[start] == target:
            return [start, end]
        return [-1, -1]