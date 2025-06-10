'''
https://leetcode.com/problems/single-element-in-a-sorted-array/description/

If mid is even:

If nums[mid] == nums[mid + 1], the single element is after mid.

Else, it's before or at mid.

If mid is odd:

If nums[mid] == nums[mid - 1], single element is after mid.

Else, it's before mid.
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        
        return nums[l]
