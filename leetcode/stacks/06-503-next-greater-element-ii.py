# https://leetcode.com/problems/next-greater-element-ii/description/
# Did not work
# Time: o(n)
# Space: o(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        output = [-1] * n
        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                oldI = stack.pop()
                output[oldI] = nums[i]
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            if output[i] == -1:
                while stack and nums[i] > nums[stack[-1]]:
                    oldI = stack.pop()
                    output[oldI] = nums[i]
            stack.append(i)
        return output
    
# 2 x Array, and clip the output array
# Time: o(n)
# Space: o(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        extendedNums = nums + nums
        n = len(extendedNums)
        stack = []
        output = [-1] * n
        for i in range(n):
            while stack and extendedNums[i] > extendedNums[stack[-1]]:
                oldI = stack.pop()
                output[oldI] = extendedNums[i]
            stack.append(i)
        return output[:int(n/2)]
