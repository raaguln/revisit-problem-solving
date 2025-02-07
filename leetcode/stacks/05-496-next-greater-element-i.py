# Faster, but .index() is slow
# Time: O(n)
# Space: O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Find next greater for all elements in nums2
        n2 = len(nums2)
        nextGreater = [-1] * n2
        stack = []
        for i in range(n2):
            while stack and nums2[i] > nums2[stack[-1]]:
                oldI = stack.pop()
                nextGreater[oldI] = nums2[i]
            stack.append(i)
        
        # Get the required output for nums1
        output = []
        for num in nums1:
            index = nums2.index(num)
            output.append(nextGreater[index])
        return output

# Using hashmap to speed up .index()
# Time: O(n)
# Space: O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Find next greater for all elements in nums2
        n2 = len(nums2)
        nextGreater = {}
        stack = []
        for i in range(n2):
            while stack and nums2[i] > nums2[stack[-1]]:
                oldI = stack.pop()
                nextGreater[nums2[oldI]] = nums2[i]
            stack.append(i)
        
        # Get the required output for nums1
        output = []
        for num in nums1:
            value = nextGreater.get(num, -1)
            output.append(value)
        return output