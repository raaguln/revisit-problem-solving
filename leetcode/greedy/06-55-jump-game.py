# https://leetcode.com/problems/jump-game/description/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for i, reach in enumerate(nums):
            # Can't reach the index
            if i > max_reach:
                return False

            # index + powerup
            max_reach = max(max_reach, i + reach)
            if max_reach >= n-1:
                return True

        return False

            