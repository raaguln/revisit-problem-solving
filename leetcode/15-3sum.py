# Attempt 1 - naive attempt
# Expected TLE error
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        result = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ind = sorted([nums[i], nums[j], nums[k]])
                        if ind not in result:
                            result.append(ind)
        return result

# Attempt 2 - same TLE
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        result = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                target = 0 - (nums[i] + nums[j])
                if target in nums[j+1:]:
                    k = nums[j+1:].index(target) + (j+1)
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    if triplet not in result:
                            result.append(triplet)
        return result