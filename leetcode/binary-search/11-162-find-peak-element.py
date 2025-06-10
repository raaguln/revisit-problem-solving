'''
https://leetcode.com/problems/find-peak-element/description/
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Goal is to bring l == r when there is a peak
        '''
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[mid + 1]:
                # Down slope - Peak is at mid or to the left
                r = mid
            else:
                # Up slope - Peak is to the right
                l = mid + 1
        
        return l