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
            # Ensure mid is even, so that
            # the duplicate is always at the right
            if mid % 2:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid
        
        return nums[l]

# Alternatively - 
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] == nums[mid - 1]:
                # Pair is mid-1 and mid, so unique must be on right side if mid is odd
                if (mid - 1) % 2 == 0:
                    l = mid + 1
                else:
                    r = mid - 2
            elif nums[mid] == nums[mid + 1]:
                # Pair is mid and mid+1, unique must be on right side if mid is even
                if mid % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1
            else:
                # mid is unique
                return nums[mid]
        
        return nums[l]