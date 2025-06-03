# https://leetcode.com/problems/subsets/description/
'''
1. Backtracking
Time complexity:

The recursion explores two possibilities for each element: include it or exclude it.
For n elements, total subsets are 2^n.
Each recursive call eventually creates a subset, so total calls and subsets generated are about 2^n.
Constructing each subset (when adding an element) takes O(k) where k is the current subset length, but since all subsets combined have total elements summed up to n * 2^(n-1), the complexity remains O(n * 2^n).

Space complexity:

The recursion stack depth is O(n) because it goes down one level per element.
The output list stores 2^n subsets, each of average size O(n), so total space for storing results is O(n * 2^n).
Temporary space used by subsets during recursion is proportional to recursion depth, O(n).
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        def recursion(i, sub):
            if i >= len(nums):                 # At the end, append that subset
                subsets.append(sub)
                return
            recursion(i+1, sub + [nums[i]])    # Take the current element
            recursion(i+1, sub)                # Not taking the current element

        recursion(0, [])
        return subsets

'''
2. Backtracking
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        def recursion(start: int, current_subset: List[int]):
            subsets.append(current_subset[:])        # Append a copy of the current subset
            
            for i in range(start, len(nums)):
                current_subset.append(nums[i])      # Include nums[i]
                recursion(i + 1, current_subset)    # Move forward with next elements
                current_subset.pop()                # Backtrack: remove last added element
        
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

        