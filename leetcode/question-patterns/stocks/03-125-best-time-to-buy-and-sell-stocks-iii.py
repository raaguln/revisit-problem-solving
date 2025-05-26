# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
first_buy:
Either keep the current first_buy (previous best buy),
Or buy at the current price (which is -price, since it's an expense).
So first_buy = max(previous first_buy, -price).

first_sell:
Either keep the current first_sell (previous best profit after selling),
Or sell now, which is current price + profit from the first buy (first_buy + price).
So first_sell = max(previous first_sell, first_buy + price).

second_buy:
Either keep the current second_buy,
Or buy again after the first sell, so subtract the current price from the profit after first sell (first_sell - price).
So second_buy = max(previous second_buy, first_sell - price).

second_sell:
Either keep the current second_sell,
Or sell the second stock now, which is second_buy + price.
So second_sell = max(previous second_sell, second_buy + price).
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy = float('-inf')
        first_sell = 0
        second_buy = float('-inf')
        second_sell = 0
        
        for price in prices:
            first_buy = max(first_buy, -price)                # Max profit after first buy
            first_sell = max(first_sell, first_buy + price)  # Max profit after first sell
            second_buy = max(second_buy, first_sell - price) # Max profit after second buy
            second_sell = max(second_sell, second_buy + price) # Max profit after second sell
        
        return second_sell
