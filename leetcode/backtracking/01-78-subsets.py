# https://leetcode.com/problems/subsets/description/
'''
Recursion
Time: O(2^n)
Space: O(n) recursive stack + O(2^n) for output storage
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Method 1 - recursion
        subsets = []
        def recursion(i, sub):
            # At the end, append that subset
            if i >= len(nums):
                subsets.append(sub)
                return
            # Take the current element
            recursion(i+1, sub + [nums[i]])
            # Not taking the current element
            recursion(i+1, sub)
        recursion(0, [])
        return subsets

'''
Using bit manipulation
Time: O(n * 2^n) - generates 2^n subsets and each subset takes O(n) time to generate
Space: O(2^n)
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Method 2 - bits
        # 2**n, based on bits you select the numbers in list
        '''
            000
            001
            010
            011
            100
            101
            110
            111
        '''
        subsets = []
        n = len(nums)
        for i in range(2**n):
            binary = bin(i)[2:].zfill(n)
            sub = []
            for j in range(n):
                if binary[j] == "1":
                    sub.append(nums[j])
            subsets.append(sub)
        return subsets

'''
Start small and build
Time: O(n * 2^n) - iterates through n elements and for each element, creates new subset (doubling the list size)
Space: O(2^n)
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Method 3 - start with small, and build
        subsets = [[]]
        for num in nums:
            newSubs = []
            for sub in subsets:
                newSubs.append(sub + [num])
            subsets.extend(newSubs)
        return subsets

'''
collections combination
Time: O(2^n)
Space: O(2^n)
'''

from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Method 4 - combinations
        subsets = []
        for i in range(len(nums)+1):
            # Generate combinations
            possibilities = combinations(nums, i)
            # Flatten the possibilities, type conversion
            possibilities = map(lambda x: list(x), possibilities)
            subsets.extend(possibilities)
        return subsets

        