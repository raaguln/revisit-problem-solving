# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note - set is implemented in the same way as hashmap, so lookup is O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        existing = set(nums)
        output = []
        for i in range(1, len(nums)+1):
            if i not in existing:
                output.append(i)
        return output
        