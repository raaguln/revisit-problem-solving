# Attempt 1 - TLE
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            left = nums[0:i]
            right = nums[i+1:]
            if 0 in left or 0 in right:
                result.append(0)
                continue
            left_prod, right_prod = 1, 1
            for n in left:
                left_prod *= n
            for n in right:
                right_prod *= n
            result.append(left_prod * right_prod)
        return result