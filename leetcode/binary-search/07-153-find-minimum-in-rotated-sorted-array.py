# NOTE - Different from your usual template
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Time: O(logn)
# Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r) // 2
            # Lowest in right half
            if nums[m] > nums[r]:
                l = m + 1
            # Lowest in left half
            else:
                r = m
        # left pointer -> min
        return nums[l]