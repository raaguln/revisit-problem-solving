'''

'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        def dfs(day, transactions_left, holding):
            # Base cases
            if day == n or transactions_left == 0:
                return 0
            
            # If currently holding a stock, can either sell or skip
            if holding:
                # Sell stock today or hold
                sell = prices[day] + dfs(day + 1, transactions_left - 1, False)
                skip = dfs(day + 1, transactions_left, True)
                return max(sell, skip)
            else:
                # If not holding, can either buy or skip
                buy = -prices[day] + dfs(day + 1, transactions_left, True)
                skip = dfs(day + 1, transactions_left, False)
                return max(buy, skip)
        
        return dfs(0, k, False)
