
# Did not fully implement 2d binary search, but still passed all test cases and top solution
# Time (as of now): O(nlogn) - logn for binary search on rows, n for checking if target is in the row
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        midI, midJ = rows//2, cols//2
        leftI, rightI = 0, rows
        leftJ, rightJ = 0, cols
        while leftI < rightI:
            midI = (leftI + rightI) // 2
            if target < matrix[midI][0]:
                rightI = midI
            elif target > matrix[midI][-1]:
                leftI = midI + 1
            else:
                return target in matrix[midI]
                # while leftJ < rightJ:
                #     midJ = (leftJ + rightJ) // 2
                #     if target < matrix[midI][midJ]:
                #         rightJ = midJ
                #     elif target > matrix[midI][midJ]:
                #         leftJ = midJ + 1
                #     else:
                #         return True  
        return False
                
