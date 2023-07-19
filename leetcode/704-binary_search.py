# I MESSED UP BINARY SEARCH :facepalm

# Attempt 1
'''
RangeError
[-1,0,3,5,9,12]
13
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + right // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right -= 1
            elif nums[mid] < target:
                left += 1
        return -1

# Attempt 2
'''
[5]
5
My output - -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right -= 1
            elif nums[mid] < target:
                left += 1
        return -1

# Attempt 3
'''
[2. 5]
5
My output - -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right -= 1
            elif nums[mid] < target:
                left += 1
        return -1

# Attempt 4 - barely binary search :facepalm
'''
266 ms (beats 5.16)
17.9MB (beats 34.84)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        # if len(nums) == 1 and nums[0] == target:
        #     return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right -= 1
            elif nums[mid] < target:
                left += 1
        return -1

# Attempt 5 - tried python's inbuilt
'''
254ms (25)
17.9MB (39)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if target in nums:
            return nums.index(target)
        else:
            return -1

# Finally
'''
249 ms (47)
17.8MB (94)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1