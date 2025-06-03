'''
https://leetcode.com/problems/top-k-frequent-elements/
- Time Complexity: O(n log k)
  - Counting frequencies: O(n)
  - Heap operations for n elements with size k: O(n log k)
- Space Complexity: O(n)
  - Counter dictionary: O(n)
  - Heap: O(k)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)

        heap = []
        for num in num_count:
            count = num_count[num]
            heappush(heap, (count, num))
            if len(heap) > k:
                heappop(heap)
        return [num for _, num in heap]