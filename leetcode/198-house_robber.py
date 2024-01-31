# Wrong logic
class Solution:
    def rob(self, nums: List[int]) -> int:
        loot1, loot2 = 0, 0
        for i in range(0, len(nums), 2):
            loot1 += nums[i]
        for i in range(1, len(nums), 2):
            loot2 += nums[i]
        return max(loot1, loot2)

# Destructured the array before checking for edge condition
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = nums[0], nums[1]
        if n < 2:
            return max(nums[0], nums[1])
        for i in range(2, n):
            temp = max(nums[i] + a, b)

# set a,b to 0 as it is more versatile
class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(nums)):
            temp = max(nums[i] + a, b)
            a = b
            b = temp
        return b