# https://leetcode.com/problems/last-stone-weight/description/
# Time: O(nlogn) - n * each heap operation (log n)
# Space: O(n) - heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapify(heap)

        while len(heap) >= 2:
            y, x = heappop(heap), heappop(heap)
            if x == y:
                continue
            heappush(heap, -abs(y-x))
        if len(heap) == 1:
            return -heap[0]
        return 0
