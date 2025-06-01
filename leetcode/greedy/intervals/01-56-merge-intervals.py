# https://leetcode.com/problems/merge-intervals/description/
'''
Time: O(nlogn)
Space: O(n)

Interval rules -
1. start and end are inclusive, merge them if they are equal
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort to have the start times in order
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            oldStart, oldEnd = output[-1]
            if oldEnd >= start:
                output[-1][1] = max(end, oldEnd)
            else:
                output.append(intervals[i])
        return output