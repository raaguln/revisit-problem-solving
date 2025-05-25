'''
Top Down Unoptimized

Time - O(2^n)
- At each index `i`, there are two choices: include `nums[i]` (if valid) or exclude it
- Maximum recursion depth is O(n)
- Number of unique subproblems is O(n^2) (based on parameters i and j), but no memoization used
- Exponential calls due to recomputation of overlapping subproblems

Space - O(n)
- Maximum recursion depth is O(n)
- Each recursive call adds a frame to the call stack
- No additional space used (no memoization or DP table)
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, prev):
            if i == n:
                return 0
            
            # Option 1: skip current element
            skip = dfs(i + 1, prev)
            
            # Option 2: take current element if it's increasing
            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + dfs(i + 1, i)
            
            return max(skip, take)

        return dfs(0, -1)

'''
Bottom Up Optimized

Time - O(n^2)  
- We fill a DP table of size (n+1) x (n+1)  
- Each cell computed in constant time  
- Total operations = O(n^2)

Space - O(n^2)  
- DP table of size (n+1) x (n+1)  
- No extra space beyond this table

Explanation -  
i - current index in nums (considering nums[i:])  
prev - index of previous chosen element (or -1 if none chosen)  

DP logic -  
QUESTION -> What is the length of the Longest Increasing Subsequence starting from index i, given the previous chosen element is at index prev?

1. Skip nums[i]:  
   - Don't take current element → dp[i+1][prev+1]  
2. Take nums[i]:  
   - Only if prev == -1 (no previous element) OR nums[i] > nums[prev] (to maintain increasing order)  
   - Then length = 1 + dp[i+1][i+1] (i becomes new prev)  

Choose the maximum of skip and take to maximize LIS length.

Indexing note -  
- prev ranges from -1 to n-1, to handle -1, we shift index by 1 in dp table → prev + 1  

Table - Step 0 after initialization (example n=5) →  
Rows represent i (current index), columns represent prev+1 (previous chosen index + 1), values = length of LIS starting at i with prev  

       prev=-1  prev=0  prev=1  prev=2  prev=3  prev=4  prev=5  
i=5 |   0      0       0       0       0       0       0  
i=4 |          ...  
...  
↑  
nums = [some array], solve dp[0][-1+1] = dp[0][0] for final LIS length
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][j]: length of LIS starting from index i, with previous chosen index j (-1 means no previous)
        # Since prev can be -1, we offset by 1 for indexing: prev+1 ranges from 0 to n
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for prev in range(i - 1, -2, -1):  # prev from i-1 down to -1
                skip = dp[i + 1][prev + 1]
                take = 0
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + dp[i + 1][i + 1]
                dp[i][prev + 1] = max(skip, take)
        
        return dp[0][0]

'''
Initialize every dp[i] to 1 (each element alone forms an LIS).
For each i, look back at all j < i.
If nums[j] < nums[i], nums[i] can extend the subsequence ending at j.
Update dp[i] accordingly.
The answer is the longest among all dp[i].
'''
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        dp = [1] * n  # Each element is an LIS of length 1 by itself
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)