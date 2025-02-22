# https://leetcode.com/problems/search-insert-position/description/
# Time: O(logn)
# Space: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l