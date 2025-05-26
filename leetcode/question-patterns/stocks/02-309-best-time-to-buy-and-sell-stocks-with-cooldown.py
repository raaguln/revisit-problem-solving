# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # Three states:
        # hold[i] - max profit holding a stock on day i
        # sold[i] - max profit just sold stock on day i
        # rest[i] - max profit doing nothing (rest) on day i
        
        hold = [0] * n
        sold = [0] * n
        rest = [0] * n
        
        hold[0] = -prices[0]  # Buy on day 0
        sold[0] = 0           # Cannot sell on day 0
        rest[0] = 0           # No action on day 0
        
        for i in range(1, n):
            # Either keep holding or buy today after rest yesterday
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            
            # Sell stock today which was held yesterday
            sold[i] = hold[i-1] + prices[i]
            
            # Either rest after selling yesterday or rest yesterday too
            rest[i] = max(rest[i-1], sold[i-1])
        
        # Maximum profit is max of sold or rest on last day (can't be holding stock)
        return max(sold[-1], rest[-1])
