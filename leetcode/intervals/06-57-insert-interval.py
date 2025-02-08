'''
Time: O(nlogn)
Space: O(n)
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        allIntervals = intervals + [newInterval]
        allIntervals.sort(key=lambda x: x[0])

        merged = [allIntervals[0]]
        for start, end in allIntervals:
            oldStart, oldEnd = merged[-1]
            if start > oldEnd:
                merged.append([start, end])
            else:
                merged[-1] = [min(start, oldStart), max(end, oldEnd)]
        return merged

        