# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Time: O(nlogn) - sorting
# Space: O(n) - set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Logic - sort only the unique values (cauz we need strictly consecutive)
        use two pointer to update lcs_length

        Edge cases - 
        You forgot to get just the unique values, wrong answer for [1, 2, 2, 3]
        '''
        if len(nums) <= 1:
            return len(nums)

        nums = sorted(set(nums))
        print(nums)
        
        longest = 1
        left, right = 0, 1
        while right < len(nums) and left < len(nums)-1:
            # print(nums[left], nums[right])
            if nums[right-1] == nums[right] - 1:
                longest = max(longest, right-left+1)
                right += 1
            else:
                left = right
                right += 1
        return longest

'''
Logic - 
Create set. Sequence starts if num-1 is not in the set. Update length of sequence till num+1 is in the set.
Time: O(n)
Space: O(n)
'''  

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)
        longest = 0
        for n in lookup:
            if n-1 in lookup:
                continue
            sequenceLength = 1
            while n+1 in lookup:
                sequenceLength += 1
                n += 1
            longest = max(longest, sequenceLength)
        return longest