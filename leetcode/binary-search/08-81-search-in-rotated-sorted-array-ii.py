'''
- https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
- can contain duplicates
- Because duplicates can "mask" whether the left or right half is sorted, 
  the classic binary search logic from problem 33 sometimes fails.
- When nums[l] == nums[m] == nums[r], we cannot tell which half is sorted.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return True
            
            # If duplicates at ends prevent us from deciding sorted half
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            # Left half is sorted
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Right half is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return False

