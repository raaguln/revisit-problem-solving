'''
https://leetcode.com/problems/find-median-from-data-stream/description/


Solution - 2 heaps (small and large)
- small -> max heap
- large -> min heap
          small          large
Step 1    [10]           []
Step 2    [2]            [10]
Step 3    [10, 2]        [14]
Step 4    [7, 2]         [10, 14]
Step 5    [7, 5, 2]      [10, 14]
Step 6    [5, 3, 2]      [7, 10, 14]
Step 7    [7, 5, 3, 2]   [8, 10, 14]
Step 8    [8, 7, 3, 2]   [10, 12, 14]
Step 9    [7, 6, 3, 2, 5] [8, 10, 12, 14]
Step 10   [8, 7, 6, 2, 5, 3]  [9, 10, 12, 14]
'''
class MedianFinder:

    def __init__(self):
        # max-heap
        self.left = []
        # min-heap
        self.right = []
        
        self.n = 0

    def addNum(self, num: int) -> None:
        # Add to small
        heappush(self.left, -num)

        # get largest value from left
        left_max = -heappop(self.left)
        heappush(self.right, left_max)

        # Balance sizes: small can be 1 element larger than large
        # get smallest value from right
        if len(self.left) < len(self.right):
            right_min = heappop(self.right)
            heappush(self.left, -right_min)
        
        # Update counter
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (-self.left[0] + self.right[0]) / 2
        return -self.left[0]