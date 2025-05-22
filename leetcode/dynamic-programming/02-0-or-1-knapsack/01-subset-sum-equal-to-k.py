'''
Given an array arr of n integers and an integer target, 
determine if there is a subset of the given array 
with a sum equal to the given target.

Examples:
Input: arr = [1, 2, 7, 3], target = 6
Output: True
Explanation: There is a subset (1, 2, 3) with sum 6.

Input: arr = [2, 3, 5], target = 6
Output: False
Explanation: There is no subset with sum 6.
'''

"""
Solutions - 
1. Generate all subsequences and check
    - power set
    - recursion

This is wasteful because we just need one answer and return
"""
# Top down, unoptimized
# Time - O(2^n)
# Space - O(n)
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        def recursion(index, target):
            if target == 0:
                return True
            if index == n or target < 0:
                return False
        
            include = recursion(index+1, target - arr[index])
            exclude = recursion(index+1, target)
            
            return include or exclude

        return recursion(0, target)


# Top down, optimized
# Time - O(n * target)
#   - n indices and target + 1 possible remaining sums
#   - Each unique pair (index, curr_target) is computed only once
# Space - O(n * target)
#   - recursion stack is O(n)
#   - memoization - O(n * target)
class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        memo = {}
        def recursion(index, target):
            if target == 0:
                return True
            if index == n or target < 0:
                return False
            if (index, target) in memo:
                return memo[(index, target)]
        
            include = recursion(index+1, target - arr[index])
            exclude = recursion(index + 1, target)

            result = include or exclude
            memo[(index, target)] = result
            return result
            
        return recursion(0, target)

# Bottom up, unoptimized
"""

i - no. of elements in array used (from left)
j - target value we are trying to reach

DP logic - 
QUESTION -> can we make target j with i elements?

1. If current number <= target?
    - DON'T SELECT number, can we make target j with i-1 elements?
    - OR
    - SELECT number, can we make target j-number with i-1 elements?
2. if current number > target
    - CAN'T SELECT number, can we make target j with i-1 elements?

Step 0 -> 
     0     1     2     3     4     5     6
   ----------------------------------------
0 | T   | F   | F   | F   | F   | F   | F   |  ← No numbers used
1 | T   |     |     |     |     |     |     |
2 | T   |     |     |     |     |     |     |
3 | T   |     |     |     |     |     |     |
4 | T   |     |     |     |     |     |     |

Step 1 ->
     0     1     2     3     4     5     6
   ----------------------------------------
0 | T   | F   | F   | F   | F   | F   | F   |
1 | T   | T   | F   | F   | F   | F   | F   |  ← Used [1]
2 | T   |     |     |     |     |     |     |
3 | T   |     |     |     |     |     |     |
4 | T   |     |     |     |     |     |     |

Step 2 ->
     0     1     2     3     4     5     6
   ----------------------------------------
0 | T   | F   | F   | F   | F   | F   | F   |
1 | T   | T   | F   | F   | F   | F   | F   |
2 | T   | T   | T   | T   | F   | F   | F   |  ← Used [1, 2]
3 | T   |     |     |     |     |     |     |
4 | T   |     |     |     |     |     |     |
"""

class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)

        # i - no. of elements from left used
        # j - target value we are trying to reach
        dp = [False for _ in range(target+1) for _ in range(n+1)]

        # Target of 0 -> possible with empty subsets
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                number = arr[i-1]
                
                # If current number is less than target
                if number <= j:
                    """
                    dp[i][j] -> can we make target j with i elements?
                    =
                    dp[i-1][j] -> DON'T SELECT NUMBER, can we make target j with i-1 elements?
                    OR
                    dp[i-1][j-number] -> SELECT NUMBER, can we make target j-number with i-1 elements?
                    """
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - number]
                
                else:
                    # dp[i-1][j] -> Don't select number, can we make target j with i-1 elements?
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]