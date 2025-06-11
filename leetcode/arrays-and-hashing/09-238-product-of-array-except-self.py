# https://leetcode.com/problems/product-of-array-except-self/
# Time:  O(n^2)
# Space: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        for i in range(0, n):
            for j in range(0, n):
                if i != j:
                    result[i] *= nums[j]
        return result

        

# Time:  O(n)
# Space: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums = [2,  3,  4,  5]
        pre =  [1,  2,  6, 24]

        nums = [2,  3,  4,  5]
        post = [60, 20, 5,  1]

        prod = [60, 40, 30, 24]
        '''
        n = len(nums)

        pre = [1] * n
        post = [1] * n

        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]

        # n = 5 -> index range = 0 to 4 -> 3,2,1,0
        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        return [pre[i] * post[i] for i in range(n)]