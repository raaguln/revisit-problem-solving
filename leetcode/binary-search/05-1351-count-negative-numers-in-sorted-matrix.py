# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Not binary search per se, but try using that approach
# Pattern recog
# Time: O(rows + cols)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #  4  3  2 -1
        #  3  2  1 -1
        #  1  1 -1 -2
        # -1 -1 -2 -3
        # It forms a staircase, so start from bottom left, and find edges
        # Start from last row, first column
        count = 0
        noColumns = len(grid[0])
        i, j = len(grid)-1, 0
        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                count += noColumns - j
                i -= 1
            else:
                j += 1
        return count
            