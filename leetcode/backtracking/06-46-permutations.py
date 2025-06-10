'''
# https://leetcode.com/problems/permutations/description/

# Time: O(n! × n²) where n is the length of the input list
# Space: O(n! × n²) where n is the length of the input list

Each recursive call creates 2 new lists
For n=8, this creates ~80,000 temporary lists!
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        n = len(nums)
        def backtrack(permutation, arr):
            if len(permutation) == n:
                output.append(permutation)
                return
            for i in range(len(arr)):
                backtrack(
                    permutation + [arr[i]],
                    arr[0:i] + arr[i+1:]
                )

        backtrack([], nums)
        return output