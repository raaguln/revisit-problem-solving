'''
Time - O(k^amount)
- For each call with `remaining`, the function tries all k coins
- Without memoization, calls overlap and grow exponentially
- The height of recursion can be up to `amount`
- Total calls are exponential in `amount`

Space - O(amount)
- Maximum recursion depth is `amount` in the worst case
- Each recursive call adds a frame to the call stack
- No additional data structures used
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(remaining):
            if remaining == 0:
                return 0  # no coins needed for amount 0
            if remaining < 0:
                return float('inf')  # invalid path

            # Try every coin and choose the best
            min_coins = float('inf')
            for coin in coins:
                res = dfs(remaining - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, 1 + res)

            return min_coins

        result = dfs(amount)
        return result if result != float('inf') else -1

'''
Bottom Up Optimized

Time - O(amount * len(coins))  
- For each amount from 1 to amount, iterate over all coin denominations  
- Each iteration performs constant time operations  
- Total operations = amount * number_of_coins

Space - O(amount)  
- A 1D DP array of size amount + 1 is maintained  
- dp[i] stores the fewest number of coins needed to make amount i  
- No recursion stack space used

Explanation -  
a - current amount we are trying to make  
dp[a] - minimum coins needed to make amount a  

DP logic -  
QUESTION -> What is the minimum number of coins required to make amount a?  

1. Base case:  
   - dp[0] = 0 (0 coins needed to make amount 0)  
2. For each amount a from 1 to amount:  
   - For each coin in coins:  
     - If coin <= a, update dp[a] = min(dp[a], dp[a - coin] + 1)  
     - This checks if using the current coin reduces the number of coins needed  
3. If dp[amount] remains amount + 1, it means amount cannot be made with given coins, return -1

Table - Step 0 after initialization (amount=5, coins=[1,2,5]):

Index:   0  1  2  3  4  5  
dp:      0  6  6  6  6  6   (6 is sentinel, amount+1)

After filling dp:

dp[1] = min(dp[1], dp[0]+1) = 1  
dp[2] = min(dp[2], dp[1]+1, dp[0]+1) = 1  
dp[3] = min(dp[3], dp[2]+1, dp[1]+1) = 2  
dp[4] = min(dp[4], dp[3]+1, dp[2]+1) = 2  
dp[5] = min(dp[5], dp[4]+1, dp[3]+1, dp[0]+1) = 1  

Final dp:

Index:   0  1  2  3  4  5  
dp:      0  1  1  2  2  1  

Answer = dp[amount] = 1
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array where dp[i] = fewest coins to make amount i
        # Use amount+1 as a sentinel value (more than any possible number of coins)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # base case: 0 coins needed for amount 0

        for a in range(1, amount + 1):
            for coin in coins:
                if coin <= a:
                    dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
