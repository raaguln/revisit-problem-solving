class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        In arrays, if we have maximum sub, then remaining array will
        give minimum sum.
        But we wouldn't have considered circular max subs, so
        - find max sub using kadane + max() -> max1
        - find minimum sub using kadane + min() -> remaining circular is max2
        - max of max1 and max2 = maximum circular sub
        
        Special edge case - 
        1. if there are no +ve numbers, then total and globalMin would become same.
        So in that case, we don't have a max circular sub, we just need to return
        the max normal sub (which is our globalMax)
        '''
        # Max 1 - using normal kadane
        currentMax = float("-inf")
        globalMax = float("-inf")
        
        # Max 2 - using kadane and min()
        currentMin = float("inf")
        globalMin = float("inf")
        total = 0

        for num in nums:
            currentMax = max(num, currentMax + num)
            globalMax = max(globalMax, currentMax)
            currentMin = min(num, currentMin + num)
            globalMin = min(globalMin, currentMin)
            total += num
            
        circularGlobalMax = total - globalMin

        if globalMax > 0:
            return max(globalMax, circularGlobalMax)
        return globalMax