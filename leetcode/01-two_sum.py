# Attempt 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        indices = []
        for i in range(0, length):
            for j in range(i+1, length):
                if(nums[i] + nums[j] == target):
                    indices = [i, j]
        return indices

# Attempt 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]

# Attempt 3 - if condition rules out a lot of calculation and helps in faster compute
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string = str(x)
        return string == string[::-1]

# Attempt 4 (worse than #3)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_copy = x
        new_x = 0
        while x_copy > 0:
            new_x = (new_x * 10) + x_copy % 10
            x_copy = x_copy // 10
        return new_x == x