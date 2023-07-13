# Attempt 1 - O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        indices = []
        for i in range(0, length):
            for j in range(i+1, length):
                if(nums[i] + nums[j] == target):
                    indices = [i, j]
        return indices

# Attempt 2 - O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if(len(nums) == 2):
            return [0, 1]
        dictionary = {}
        for i, n1 in enumerate(nums):
            n2 = target - n1
            if(n2 in dictionary):
                return [i, dictionary[n2]]
            dictionary[n1] = i
