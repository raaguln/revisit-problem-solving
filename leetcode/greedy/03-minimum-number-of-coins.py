'''
- Only for canonical coin systems (like Indian currency)
- greedy algorithm always produces the minimum number of 
  coins to make change for any amount
    - Each larger coin value is a multiple or combination of 
      smaller coins in such a way that greedy selection leads to an optimal solution.
    - For example, to make 40 Rs:
        - Greedy picks 20 + 20 = 2 coins (optimal)
        - DP would confirm no better solution exists.
'''
class Solution:
    def minCoins(self, amount: int) -> int:
        denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
        coin_count = 0
        remaining_amount = amount
        
        for coin in denominations:
            if remaining_amount == 0:
                break
            coins_used = remaining_amount // coin
            coin_count += coins_used
            remaining_amount -= coins_used * coin
        
        return coin_count

'''
Non-canonical - 
- denominations = [1, 3, 4]
- To make change for 6:
    - Greedy picks:
        4 (remaining 2)
        1 + 1 (total 3 coins)

    - But optimal is:
        3 + 3 (total 2 coins)

So greedy fails here.
'''
class Solution:
    def minCoinsDP(self, amount: int, denominations: List[int]) -> int:
        # Initialize DP array where dp[i] = min coins for amount i
        # Use amount+1 as "infinity" since max coins needed can't exceed amount (all 1 Rs coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # 0 coins needed for amount 0
        
        for amt in range(1, amount + 1):
            for coin in denominations:
                if coin <= amt:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1  # -1 means not possible
