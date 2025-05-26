'''
Time - O(2^n)
- Each element has 2 choices: add or subtract
- Total recursive calls double at each step
- Number of calls grows exponentially with n

Space - O(n)
- Maximum recursion depth is n (length of nums)
- Each call adds a frame to the call stack
- No additional data structures used
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        def dfs(i, current_sum):
            # Base case: all numbers processed
            if i == n:
                return 1 if current_sum == target else 0
            
            # Choose '+' sign for nums[i]
            add = dfs(i + 1, current_sum + nums[i])
            # Choose '-' sign for nums[i]
            subtract = dfs(i + 1, current_sum - nums[i])
            
            return add + subtract
        
        return dfs(0, 0)

'''
Bottom Up Unptimized

Time - O(n * total * 2) = O(n * total)  
- n is the number of elements in nums  
- total = sum of all elements in nums  
- For each element i and each possible sum s in range [-total, total], we update dp  
- Each dp state updated twice (add and subtract)  
- Total operations approximately O(n * total)

Space - O(n * total * 2) = O(n * total)  
- A 2D DP table of size (n+1) x (2*total + 1) stores counts of ways to reach each sum  
- dp[i][s] represents number of ways to get sum s - offset using first i numbers  
- No recursion stack used

Explanation -  
n - number of elements  
total - sum of all elements (used for offset to handle negative sums)  
offset = total (to shift sums from range [-total, total] to [0, 2*total])  
dp[i][s] - number of ways to reach sum s - offset using first i elements  

DP logic -  
QUESTION -> How many ways to reach sum (s - offset) using first i numbers?  

1. Base case:  
   - dp[0][offset] = 1 (0 numbers to reach sum 0)  
2. For each number i in 1 to n:  
   - For each sum s in 0 to 2*total:  
     - If dp[i-1][s] > 0 (there are ways to reach sum s - offset with i-1 numbers):  
       - Add nums[i-1]: dp[i][s + nums[i-1]] += dp[i-1][s] (if in range)  
       - Subtract nums[i-1]: dp[i][s - nums[i-1]] += dp[i-1][s] (if in range)  
3. Return dp[n][target + offset] if target in [-total, total], else 0  

Table - Step 0 after initialization (nums=[1,1], target=0):  

offset = 2 (total=2)  
dp[0][2] = 1 (sum = 0)  
All other dp[0][s] = 0  

After processing first number (1):  
dp[1][3] = dp[0][2] = 1 (sum = +1)  
dp[1][1] = dp[0][2] = 1 (sum = -1)  

After processing second number (1):  
dp[2][4] = dp[1][3] = 1 (sum = +2)  
dp[2][2] = dp[1][3] + dp[1][1] = 1 + 1 = 2 (sum = 0)  
dp[2][0] = dp[1][1] = 1 (sum = -2)  

Answer = dp[n][target + offset] = dp[2][2] = 2 ways
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        
        # dp[i][s] = number of ways to reach sum s using first i numbers
        # We shift sums by total to handle negative indices (offset)
        offset = total
        dp = [[0] * (2 * total + 1) for _ in range(n + 1)]
        
        # Base case: 0 numbers used, sum = 0 => 1 way
        dp[0][offset] = 1
        
        for i in range(1, n + 1):
            for s in range(2 * total + 1):
                if dp[i-1][s] != 0:
                    # Add nums[i-1]
                    if s + nums[i-1] <= 2 * total:
                        dp[i][s + nums[i-1]] += dp[i-1][s]
                    # Subtract nums[i-1]
                    if s - nums[i-1] >= 0:
                        dp[i][s - nums[i-1]] += dp[i-1][s]
        
        # If target sum is out of range, return 0
        if target > total or target < -total:
            return 0
        
        return dp[n][target + offset]
