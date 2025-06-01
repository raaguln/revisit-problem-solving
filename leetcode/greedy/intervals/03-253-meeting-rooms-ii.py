# https://leetcode.com/problems/meeting-rooms-ii/description/
'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the 
minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
'''
'''
Method 1 - Logic DOES NOT WORK because start and end are not inclusive - 
you can have a meeting in a single room (with end1=10 and start2=10)
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Works only if end1 and start2 are considered overlap
        '''
        flattened = []
        for start, end in intervals:
            flattened.extend([f"s{start}", f"e{end}"])
        flattened.sort(key=lambda x: int(x[1:]))
        
        currentMeetings, maxMeetings = 0, 0
        for val in flattened:
            time = int(val[1:])
            if val[0] == "s":
                currentMeetings += 1
            else:
                currentMeetings -= 1
            maxMeetings = max(currentMeetings, maxMeetings)
        
        return maxMeetings

'''
Time complexity: O(nlogn) - sorting
Space complexity: O(n) - storing all start and end times
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Works only if end1 and start2 are considered overlap
        '''
        start, end = [], []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()
        
        n = len(start)
        i, j = 0, 0
        currMeetings, maxMeetings = 0, 0
        while i < n and j < n:
            # A meeting starts
            if start[i] < end[j]:
                currMeetings += 1
                i += 1
            # one meeting starts and another one ends
            elif start[i] == end[j]:
                i += 1
                j += 1
            # A meeting ends
            else:
                currMeetings -= 1
                j += 1
            maxMeetings = max(currMeetings, maxMeetings)
        return maxMeetings
    
'''
Min heap approach
Time complexity: O(nlogn) - sorting
Space complexity: O(n) - storing all start and end times

Note - this won't work without you sorting the input initially
'''

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Min-heap solution
        Create new meeting if - 
        1. if no meetings
        2. if m1 is ending after start of m2
        Else - 
        assign m2 to the room where the meeting ended earliest
        '''
        intervals.sort(key=lambda x:x[0])
        heap = []            # Store end times
        for start, end in intervals:
            if not heap or heap[0] > start:
                heapq.heappush(heap, end)
            else:
                heapq.heapreplace(heap, end)
        return len(heap)