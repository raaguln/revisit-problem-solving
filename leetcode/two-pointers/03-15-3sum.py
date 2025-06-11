# https://leetcode.com/problems/3sum/description/
# Time: O(n^2)
# Space: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique = sorted(nums)
        solutions = set()
        for i in range(len(unique)):
            a = unique[i]
            target = 0 - a
            left, right = i+1, len(unique)-1
            while left < right:
                if unique[left] + unique[right] == target:
                    triplet = tuple([a, unique[left], unique[right]])
                    if triplet not in solutions:
                        solutions.add(triplet)
                    left += 1
                    right -= 1
                elif unique[left] + unique[right] > target:
                    right -= 1
                else:
                    left += 1
        return [list(triplet) for triplet in solutions]

# Time: O(n^2) - but faster than the previous solution
# Space: O(1) - no extra storage
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # No extra storage
        nums.sort()
        # No need for set because we are skipping duplicates
        solutions = []
        # No need to check last two elements
        for i in range(len(nums)-2):
            # Skip duplicates for 'a'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            # No need for 0-a
            target = -a
            left, right = i+1, len(nums)-1
            while left < right:
                # Calculate once
                twoSum = nums[left] + nums[right]
                if twoSum == target:
                    solutions.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for b & c
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif twoSum > target:
                    right -= 1
                else:
                    left += 1
        return solutions

