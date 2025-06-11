# https://leetcode.com/problems/maximum-subarray/description/
# Brute force
# Time: O(n^2)
# Space: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxPossibleSum = float("-inf")
        for i in range(n):
            for j in range(i, n):
                value = sum(nums[i:j+1])
                maxPossibleSum = max(maxPossibleSum, value)
        return maxPossibleSum

# Kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = float("-inf")
        maxSum = float("-inf")
        for n in nums:
            currentSum = max(n, currentSum + n)
            maxSum = max(maxSum, currentSum)
        return maxSum
        