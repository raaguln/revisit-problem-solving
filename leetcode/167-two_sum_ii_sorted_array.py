# Attempt 1 -
# 7577 ms (beats 5.5%)
# 17.2 MB (beats 95%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            to_find = target - numbers[i]
            if to_find not in numbers[i+1:]:
                continue
            return [i + 1, numbers[i+1:].index(to_find) + (i+1) + 1]

# Attempt 2 - Used binary search since sorted array
# 238 ms (beats 5.5%) -> ???
# 17.3 MB (beats 61.54%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            to_find = target - numbers[i]
            # binary search
            low, high = 0, len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2
                if to_find == numbers[mid]:
                    if i == mid:
                        if mid-1 >= 0 and numbers[mid-1] == numbers[mid]:
                            return [i + 1, mid]
                        elif mid+1 < len(numbers) and numbers[mid+1] == numbers[mid]:
                            return [i + 1, mid+2]
                    return [i + 1, mid + 1]
                elif to_find < numbers[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

# Attempt 3 - had to look it up online
# This solution only works cauz there's always one exact solution available
# 127ms (97.27%)
# 17.2MB (95.14%)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1