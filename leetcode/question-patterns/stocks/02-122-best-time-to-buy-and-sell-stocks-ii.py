'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Algo -
For each day, check if the price is higher than the previous day:
If yes, then buy on the previous day and sell on this day (because you can make a profit).
Add that profit (prices[i] - prices[i-1]) to total_profit.


- When prices go up from one day to the next, buying 
the previous day and selling the next day gives profit.
Summing these small profits is the same as buying at 
the lowest point and selling at the highest point in each "rising" segment.
- This works because the problem allows multiple transactions without limits.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total_profit += prices[i] - prices[i-1]
        return total_profit
