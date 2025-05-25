'''
Top Down Unoptimized

Time - O(2^n)
- At each element, two choices: include or exclude
- Inclusion depends on divisibility with the previously included element, but in worst case can still branch twice at each step
- Maximum recursion depth is O(n)
- No memoization leads to exponential recomputation

Space - O(n)
- Recursion depth up to O(n)
- Each recursive call adds a frame to the call stack
- No additional data structures for memoization or DP
'''
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()  # Sort to make divisibility checks easier
        n = len(nums)

        def dfs(i, prev_index):
            # If reached the end of the list
            if i == n:
                return []

            # Option 1: skip current element
            option1 = dfs(i + 1, prev_index)

            # Option 2: take current element if divisible with previous
            option2 = []
            if prev_index == -1 or nums[i] % nums[prev_index] == 0:
                option2 = [nums[i]] + dfs(i + 1, i)

            # Return the longer subset
            if len(option1) > len(option2):
                return option1
            else:
                return option2

        return dfs(0, -1)

'''
Bottom Up Optimized

Time - O(n^2)  
- Outer loop runs n times, inner loop runs up to n times  
- Each step does constant work to check divisibility and length comparison  
- Total operations = O(n^2)

Space - O(n^2) (worst case)  
- DP array of lists storing subsets  
- Each dp[i] can hold up to n elements in the worst case  

Explanation -  
i - current index in nums (considering nums[i:] suffix)  

DP logic -  
QUESTION -> What is the largest divisible subset starting at index i?

1. For each j > i:  
   - If nums[j] is divisible by nums[i], nums[i] can be prepended to dp[j]  
   - We choose dp[j] with the longest length to extend from  
2. dp[i] = [nums[i]] + longest dp[j] where nums[j] % nums[i] == 0  

Final Answer -  
- The longest subset among all dp[i] is the largest divisible subset in nums

Table - Step 0 after initialization (example nums = [1, 2, 4, 8]) →  
dp array holds subsets starting at each index:

i | dp[i]  
---|-------  
3 | [8]  
2 | [4, 8]  
1 | [2, 4, 8]  
0 | [1, 2, 4, 8]  

Answer: dp[0] = [1, 2, 4, 8]
'''
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)

        # dp[i] will hold the largest divisible subset starting at index i
        dp = [[] for _ in range(n + 1)]
        # We add an extra element for convenience with prev_index = -1 handled as dp[n]

        for i in range(n - 1, -1, -1):
            max_subset = []
            for j in range(i + 1, n):
                # If nums[j] is divisible by nums[i], we can extend the subset starting at j
                if nums[j] % nums[i] == 0 and len(dp[j]) > len(max_subset):
                    max_subset = dp[j]
            dp[i] = [nums[i]] + max_subset

        # The answer is the longest subset among all dp[i]
        return max(dp[:-1], key=len)

