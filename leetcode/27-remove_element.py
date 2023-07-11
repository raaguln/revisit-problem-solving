# Attempt 1 - logic untested as leetcode didn't run this
# This works in local, but `global` doesn't work in leetcode
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        def sort_helper(x):
            if x == val:
                global count
                count += 1
                return 1
            return 0
        nums.sort(key=sort_helper)
        return count

# Attempt 2 - meh runtime
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                count += 1
        nums.sort(key=lambda x: 1 if x == val else 0)
        return count

# Attempt 3 - best
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count, i = 0, 0
        while i < len(nums):
            if nums[i] != val:
                count += 1
            else:
                nums.pop(i)
                continue
            i += 1
        return count