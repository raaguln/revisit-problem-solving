# https://leetcode.com/problems/kth-largest-element-in-an-array/
from heapq import heapify, heappop

'''
- Time Complexity: O(n + (n-k) log n)
  - heapify: O(n)
  - heappop repeated (n-k) times: O((n-k) log n)
- Space Complexity: O(1) (in-place heap)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        return nums[0]

# Also, kth smallest element
class Solution:
    def findKthSmallest(self, nums: List[int], k: int) -> int:
        # max heap
        heap = []
        for n in nums:
            heappush(heap, -n)
            if len(heap) > k:
                heappop(heap)
        return -heap[0]

# QUICK SELECT - for kth largest
# Time: O(n) - average case, O(n^2) - worst case
# Space: O(logn) - average case, O(n) - worst case
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(arr, k):
            if len(arr) == 1:
                return arr[0]

            pivot = arr[len(arr) // 2]

            # Create left, middle, and right (ascending order)
            # Note - if you do descending order here, modify accordingly below
            left, middle, right = [], [], []
            for num in arr:
                if num > pivot:
                    right.append(num)
                elif num == pivot:
                    middle.append(num)
                else:
                    left.append(num)
            
            # kth largest (start searching from right)
            leftLen, midLen, rightLen = len(left), len(middle), len(right)
            if k < rightLen:
                return quickSelect(right, k)
            elif k < rightLen + midLen:
                return middle[0]
            else:
                return quickSelect(left, k - rightLen - midLen)
        
        # 0 based index
        return quickSelect(nums, k-1)


# QUICK SELECT - for kth smallest
class Solution:
    def findKthSmallest(self, nums: List[int], k: int) -> int:
        def quickSelect(arr, k):
            if len(arr) == 1:
                return arr[0]

            pivot = arr[len(arr) // 2]

            left, middle, right = [], [], []
            for num in arr:
                if num < pivot:       # Changed: '<' for left (smaller than pivot)
                    left.append(num)
                elif num == pivot:
                    middle.append(num)
                else:
                    right.append(num)  # Changed: '>' for right (greater than pivot)

            leftLen, midLen, rightLen = len(left), len(middle), len(right)

            if k < leftLen:                # Search left (smaller side)
                return quickSelect(left, k)
            elif k < leftLen + midLen:     # Pivot is the kth smallest
                return middle[0]
            else:                          # Search right side (larger numbers)
                return quickSelect(right, k - leftLen - midLen)

        # k is 1-based index, convert to 0-based for quickSelect
        return quickSelect(nums, k - 1)
