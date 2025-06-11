# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
# Time:  O(n)
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maximumProfit = max(maximumProfit, profit)
                right += 1
            else:
                left = right
                right += 1
        return maximumProfit
