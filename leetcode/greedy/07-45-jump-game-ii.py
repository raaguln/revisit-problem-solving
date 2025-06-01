# https://leetcode.com/problems/jump-game-ii/description/
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        max_reach = 0      # Furthest reachable index
        jumps = 0          # Number of jumps taken
        current_end = 0    # End of the range for the current jump
        n = len(nums)

        for i, reach in enumerate(nums):
            # Update the furthest reachable index from current position
            max_reach = max(max_reach, i + reach)
            
            # If we reached the end of the current jump's range,
            # we need to jump and update the range to max_reach
            if i == current_end:
                jumps += 1
                current_end = max_reach
                
                # If we can reach or go beyond the last index, return jumps
                if current_end >= n - 1:
                    break
        
        return jumps