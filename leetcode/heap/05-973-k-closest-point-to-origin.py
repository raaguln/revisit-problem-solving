# https://leetcode.com/problems/k-closest-points-to-origin/description/
# Time: O(nlogk) + O(klogn) = O(nlogn)
# Space: O(n)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)

        for x,y in points:
            distance = (x*x + y*y)**(1/2)
            heappush(heap, (distance, [x, y]))

        closestPoints = []
        while len(closestPoints) < k:
            min_val = heappop(heap)[1]
            closestPoints.append(min_val)

        return closestPoints

# Optimized
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            # We don't need square root
            dist = (x*x + y*y)
            
            heappush(heap, (-dist, [x, y]))

            # Maintain the size of heap
            if len(heap) > k:
                heappop(heap)
        
        return [point for _, point in heap]


# More optimized
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            # We don't need square root
            dist = (x*x + y*y)

            # Maintain the size of heap
            if len(heap) < k:
                heappush(heap, (-dist, [x, y]))
            else:
                if dist < -heap[0][0]:
                    heapreplace(heap, (-dist, [x, y]))
            
        return [point for _, point in heap]