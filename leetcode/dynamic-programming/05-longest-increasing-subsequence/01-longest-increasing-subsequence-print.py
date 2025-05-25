class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)

        def dfs(i, prev_index):
            if i == n:
                return []

            # Option 1: skip current element
            option1 = dfs(i + 1, prev_index)

            # Option 2: take current element if it is increasing
            option2 = []
            if prev_index == -1 or nums[i] > nums[prev_index]:
                option2 = [nums[i]] + dfs(i + 1, i)

            # Return the longer subsequence
            if len(option1) > len(option2):
                return option1
            else:
                return option2

        return dfs(0, -1)

class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        # dp[i] will hold the longest increasing subsequence starting at index i
        dp = [[] for _ in range(n)]

        for i in range(n-1, -1, -1):
            max_subseq = []
            for j in range(i+1, n):
                if nums[j] > nums[i] and len(dp[j]) > len(max_subseq):
                    max_subseq = dp[j]
            dp[i] = [nums[i]] + max_subseq

        # The result is the longest subsequence starting from any index
        longest = []
        for seq in dp:
            if len(seq) > len(longest):
                longest = seq

        return longest
