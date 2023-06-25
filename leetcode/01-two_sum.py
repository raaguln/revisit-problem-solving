class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        indices = []
        for i in range(0, length):
            for j in range(i+1, length):
                if(nums[i] + nums[j] == target):
                    indices = [i, j]
        return indices