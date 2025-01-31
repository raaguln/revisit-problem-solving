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
        n = len(nums)
        pre = [1] * n
        val = 1
        for i in range(n):
            pre[i] = val
            val *= nums[i]

        post = [1] * n
        val = 1
        for i in range(n-1, -1, -1):
            post[i] = val
            val *= nums[i]
        
        return [pre[i] * post[i] for i in range(n)]