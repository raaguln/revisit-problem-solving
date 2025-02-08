'''
Problem - 
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
'''

'''
Time: O(nlogn)
Space: O(n)

Interval rules - 
1. start and end are not inclusive
'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort()
        mergedIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            oldStart, oldEnd = mergedIntervals[-1]
            if oldEnd > start:
                mergedIntervals[-1][1] = max(oldEnd, end)
            else:
                mergedIntervals.append(intervals[i])
        return len(intervals) == len(mergedIntervals)