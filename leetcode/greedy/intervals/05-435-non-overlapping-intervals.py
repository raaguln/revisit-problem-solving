'''
Did not work. This is cauz some intervals are large and they end up removing lot of smaller intervals
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return None
        # intervals.sort()
        mergedIntervals = [intervals[0]]
        for start, end in intervals:
            oldStart, oldEnd = mergedIntervals[-1]
            if oldEnd <= start:
                mergedIntervals.append([start, end])
            else:
                mergedIntervals[-1][1] = max(oldEnd, end)
        print(intervals)
        print(mergedIntervals)
        return len(intervals) - len(mergedIntervals)


'''
Greedy Algorithm
1. Sort the intervals based on the end time
2. If the current interval overlaps with the previous interval, remove the interval with the larger end time
3. Return the number of removed intervals

Time: O(nlogn)
Space: O(1)
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return None
        # intervals.sort()
        mergedIntervals = [intervals[0]]
        for start, end in intervals:
            oldStart, oldEnd = mergedIntervals[-1]
            if oldEnd <= start:
                mergedIntervals.append([start, end])
            else:
                mergedIntervals[-1][1] = max(oldEnd, end)
        print(intervals)
        print(mergedIntervals)
        return len(intervals) - len(mergedIntervals)
                