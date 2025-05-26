'''
Time - O(2^(m + amount))
- At each call, two recursive branches: take or skip coin[i]
- Maximum recursion depth is roughly m + amount (m = number of coins)
- Without memoization, the number of calls grows exponentially

Space - O(m + amount)
- Maximum recursion depth is at most m + amount
- Each recursive call adds a frame to the call stack
- No additional data structures used
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(i, remaining):
            # If remaining amount is 0, found a valid combination
            if remaining == 0:
                return 1
            # If no coins left or remaining < 0, no valid combination
            if i == len(coins) or remaining < 0:
                return 0
            
            # Choose to take coin[i] or skip it
            take = dfs(i, remaining - coins[i])   # use coin[i]
            skip = dfs(i + 1, remaining)           # skip coin[i]
            return take + skip
        
        return dfs(0, amount)

'''
Bottom Up Optimized

Time - O(n * amount)  
- There are n coins and amount+1 subproblems for amounts from 0 to amount  
- Each subproblem dp[i][j] is computed once, with constant time operations  
- Total complexity = n * amount

Space - O(n * amount)  
- A 2D DP table of size (n+1) x (amount+1) is maintained  
- dp[i][j] stores the number of ways to make amount j using coins from index i to the end  
- No recursion stack used

Explanation -  
n - number of coin denominations  
i - current coin index (from bottom up)  
j - current amount  

DP logic -  
QUESTION -> How many ways to make amount j using coins from index i to n-1?  

1. Base case:  
   - For any i, dp[i][0] = 1 (there is exactly one way to make amount 0: use no coins)  
2. For each coin index i from n-1 down to 0:  
   - dp[i][j] = ways to make amount j without using coin i (dp[i+1][j])  
   - Plus ways to make amount j by including coin i if possible (dp[i][j - coins[i]])  
3. dp[0][amount] gives total number of ways to make amount using all coins

Table - Step 0 after initialization (coins=[1,2], amount=3):

     0  1  2  3  
i=2 [1, 0, 0, 0]  # dp[n][...] base case beyond last coin  
i=1 [1, 0, 0, 0]  
i=0 [1, 0, 0, 0]  

After filling dp:

i=1 (coin=2):  
dp[1][0]=1  
dp[1][1]=dp[2][1]=0  
dp[1][2]=dp[2][2] + dp[1][0] = 0 + 1 =1  
dp[1][3]=dp[2][3] + dp[1][1] = 0 + 0 =0  

i=0 (coin=1):  
dp[0][0]=1  
dp[0][1]=dp[1][1] + dp[0][0] = 0 +1 =1  
dp[0][2]=dp[1][2] + dp[0][1] = 1 +1 =2  
dp[0][3]=dp[1][3] + dp[0][2] = 0 +2 =2  

Answer = dp[0][3] = 2 ways
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        # dp[i][j] = number of ways to make amount j using coins from i to end
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        # Base case: when remaining amount is 0, there is exactly 1 way (use no coins)
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Fill the table bottom up
        for i in range(n - 1, -1, -1):
            for j in range(amount + 1):
                # skip coin i
                dp[i][j] = dp[i + 1][j]
                
                # take coin i if possible
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j - coins[i]]
        
        return dp[0][amount]
