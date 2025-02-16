# https://leetcode.com/problems/container-with-most-water/description/
# This works because we start from the widest container, 
# and move the pointer at the shorter end inwards.

# Time:  O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maximum = max(area, maximum)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maximum
