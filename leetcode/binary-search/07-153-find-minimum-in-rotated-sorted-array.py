# NOTE - Different from your usual template
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Time: O(logn)
# Space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r) // 2
            # this means - smallest value must be to the right of m
            if nums[m] > nums[r]:
                l = m + 1
            # Lowest in left half
            else:
                r = m
        # left pointer -> min
        return nums[l]

# Find max
        l, r = 0, len(nums) - 1

        # NOTE: Fails without this
        # If array not rotated (strictly ascending)
        if nums[l] < nums[r]:
            return nums[r]
        while l < r:
            m = (l + r + 1) // 2  # upper mid to prevent infinite loop
            if nums[m] > nums[r]:
                l = m          # max in right half, including m
            else:
                r = m - 1      # max in left half, excluding m
        return nums[l]


# NOTE - USING THE SAME as min AND FLIPPING - DOENST WORK
l, r = 0, len(nums) - 1
while l < r:
    m = (l + r) // 2
    # If middle element is greater than rightmost,
    # max is in left half including m
    if nums[m] > nums[r]:
        r = m
    else:
        l = m + 1
return nums[l]