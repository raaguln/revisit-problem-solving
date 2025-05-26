# Top down, unoptimized
# TLE
# Time: O(2*n)
# Space: O(n) - stack
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = int(total / 2)

        def canPartition(i, curr_sum):
            if curr_sum == target:
                return True
            if i >= n or curr_sum > target:
                return False
            
            include = canPartition(i+1, curr_sum + nums[i])
            exclude = canPartition(i+1, curr_sum)

            return include or exclude

        return canPartition(0, 0)

# Top down, optimized
# MLE
# Time: O(2*n)
# Space: O(n) - stack
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = int(total / 2)

        memo = {}
        def canPartition(i, curr_sum):
            if curr_sum == target:
                return True
            if i >= n or curr_sum > target:
                return False
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            include = canPartition(i+1, curr_sum + nums[i])
            exclude = canPartition(i+1, curr_sum)
            
            result = include or exclude
            memo[(i, curr_sum)] = result

            return result

        return canPartition(0, 0)

# Bottom up, unoptimized
# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = int(total / 2)

        # i = no. of elements in array used (from left)
        # j = target we are trying to achieve
        # dp[i][j] = whether we can achieve target or not
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]

        # we can achieve target 0 with empty set
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                number = nums[i-1]

                # If number is <= target
                if number <= j:
                    # don't select number, target = j
                    # Select number, target = j-number
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-number]
                else:
                    # can't select number, target = j
                    dp[i][j] = dp[i-1][j]
        return dp[n][target]


# Bottom up, optimized - WRONG SOLUTION
# Time: O(m*n)
# Space: O(n)
from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Issue - forward loop for j -> dp[j-number] tries to access values
        from current loop (values leak forward)
        - In step 2, while processing num = 2, if dp[1] is changed early, dp[3] = dp[3] or dp[1] might read the updated dp[1], not the original value (which breaks the logic).
        Fix - use backward loop
        """
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = int(total / 2)

        # i = no. of elements in array used (from left)
        # j = target we are trying to achieve
        # dp[i][j] = whether we can achieve target or not
        dp = [False for _ in range(target+1)]

        # we can achieve target 0 with empty set
        dp[0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                number = nums[i-1]

                # If number is <= target
                if number <= j:
                    # don't select number, target = j
                    # Select number, target = j-number
                    dp[j] = dp[j] or dp[j-number]
                else:
                    # can't select number, target = j
                    dp[j] = dp[j]
        return dp[target]



# Bottom up, optimized
# Time: O(m*n)
# Space: O(n)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Issue - forward loop for j -> dp[j-number] tries to access values
        from current loop (values leak forward)
        - In step 2, while processing num = 2, if dp[1] is changed early, dp[3] = dp[3] or dp[1] might read the updated dp[1], not the original value (which breaks the logic).
        Fix - use backward loop
        """
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = int(total / 2)

        # i = no. of elements in array used (from left)
        # j = target we are trying to achieve
        # dp[i][j] = whether we can achieve target or not
        dp = [False] * (target+1)

        # we can achieve target 0 with empty set
        dp[0] = True

        for number in nums:
            for j in range(target, -1, -1):
                # If number is <= target
                if number <= j:
                    # don't select number, target = j
                    # Select number, target = j-number
                    dp[j] = dp[j] or dp[j-number]
                else:
                    # can't select number, target = j
                    dp[j] = dp[j]
        return dp[target]