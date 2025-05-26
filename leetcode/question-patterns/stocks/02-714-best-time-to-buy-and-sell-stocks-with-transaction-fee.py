from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # hold: max profit if we currently hold a stock
        # cash: max profit if we currently do NOT hold a stock
        hold = -prices[0]  # Initially, if we buy on day 0, profit = -price[0]
        cash = 0           # Initially, if we do nothing, profit = 0
        
        for price in prices[1:]:
            # If we hold a stock today, max profit is either:
            # - keep holding the stock from before, or
            # - buy today (which means we had cash yesterday and buy today)
            hold = max(hold, cash - price)
            
            # If we don't hold a stock today, max profit is either:
            # - keep the cash from yesterday, or
            # - sell the stock today (which means we had stock yesterday and sell today, minus fee)
            cash = max(cash, hold + price - fee)
        
        # At the end, max profit will be when we do NOT hold any stock
        return cash
