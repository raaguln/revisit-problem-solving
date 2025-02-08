'''
Does not work cauz
firstList   = [[0,2],[5,10],[13,23],[24,25]]
secondList  = [[1,5],[8,12],[15,24],[25,26]]
Output   - [[1,2],[5,5],[13,12],[15,23],[24,24]]
Expected - [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
'''
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        output = []
        i, j = 0, 0
        n1, n2 = len(firstList), len(secondList)
        while i < n1 and j < n2:
            print(firstList[i], secondList[j])
            i1start, i1end = firstList[i]
            i2start, i2end = secondList[j]

            start = max(i1start, i2start)
            end = min(i1end, i2end)
            output.append([start, end])

            if i1start < i2start < i1end:
                i += 1
            elif i1start == i2start or i1end == i2start or i1start == i2end:
                i += 1
                j += 1
            else:
                j += 1
        return output



'''
Works
Time: O(n + m)
Space: O(1)
'''
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        output = []
        i, j = 0, 0
        n1, n2 = len(firstList), len(secondList)
        while i < n1 and j < n2:
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            if start1 > end2:
                j += 1
            elif start2 > end1:
                i += 1
            else:
                output.append([
                    max(start1, start2),
                    min(end1, end2)
                ])
                if end1 > end2:
                    j += 1
                else:
                    i += 1

        return output