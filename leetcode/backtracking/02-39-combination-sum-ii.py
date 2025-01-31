'''
Constraints:
1. Can have duplicates
2. One element - used only once
3. All +ve integers
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def recursion(i, sub, summation):
            if i >= len(candidates) or summation > target:
                return
            if summation == target:
                output.append(sub)
                return
            recursion(i+1, sub + [candidates[i]], summation + candidates[i])
            recursion(i+1, sub, summation)
        
        recursion(0, [], 0)
        return output
    