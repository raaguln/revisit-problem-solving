# Time: O(nlogn) - n * each heap operation (log n)
# Space: O(n) - heap
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones]
        
        # Max Heap
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, -abs(y-x))
        if stones:
            return -heapq.heappop(stones)
        else:
            return 0
