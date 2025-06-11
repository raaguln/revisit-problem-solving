# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
'''
Sort the index and store first occurrence of number with index.
Index will be the number of elements smaller than current no.
Return that on original array

Time Complexity: O(nlogn)
Space Complexity: O(n)
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        firstIndexMapping = {}
        for i in range(len(temp)):
            if temp[i] not in firstIndexMapping:
                firstIndexMapping[temp[i]] = i
        count = []
        for i in range(len(nums)):
            count.append(
                firstIndexMapping[nums[i]]
            )
        return count

'''
Create a frequency count of numbers using list. This helps prevent sorting.
Note - count[nums[i]+1] += 1 => you do nums[i]+1 so that you can directly use count[nums[i]] in output
Time Complexity: O(n)
Space Complexity: O(n)
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * 102

        # Count frequency of each number
        for num in nums:
            count[num] += 1

        # Build prefix sums: count[i] will store how many numbers are <= i
        for i in range(1, 102):
            count[i] += count[i - 1]

        # For each number, how many are smaller = count[num - 1] if num > 0 else 0
        output = []
        for num in nums:
            output.append(count[num - 1] if num > 0 else 0)

        return output