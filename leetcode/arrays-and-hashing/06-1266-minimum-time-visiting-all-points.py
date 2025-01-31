# Time: O(n)
# Space: O(1)
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if len(points) ==  1:
            return 0
        # We can start from the first point, we don't have to start from 0,0
        time = 0
        x1, y1 = points.pop()
        while points:
            x2, y2 = points.pop()
            time += max(abs(x1-x2), abs(y1-y2))
            x1, y1 = x2, y2
        return time