'''
DP - O(n)
Why We Track Both curr_max and curr_min?
Because a negative number can:
- Turn a large positive product into a negative, and
- Turn a small negative product into a big positive!

So we track:
- curr_max: max product ending at current index
- curr_min: min product ending at current index
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize current max, current min, and result to first element
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]
        
        # Loop through the rest of the array
        for i in range(1, len(nums)):
            num = nums[i]
            
            # If number is negative, swap max and min
            # Because multiplying by a negative flips max/min
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            
            # Update current max/min by either:
            # - starting fresh from current number, or
            # - multiplying with previous max/min
            curr_max = max(num, num * curr_max)
            curr_min = min(num, num * curr_min)
            
            # Update the global maximum product
            result = max(result, curr_max)
        
        return result
