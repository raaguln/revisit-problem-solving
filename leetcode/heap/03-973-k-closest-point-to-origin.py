# Time: O(nlogk) + O(klogn) = O(nlogn)
# Space: O(n)
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for x,y in points:
            distance = (x*x + y*y)**(1/2)
            heapq.heappush(heap, (distance, [x, y]))
        closestPoints = []
        while len(closestPoints) < k:
            closestPoints.append(
                heapq.heappop(heap)[1]
            )
        return closestPoints