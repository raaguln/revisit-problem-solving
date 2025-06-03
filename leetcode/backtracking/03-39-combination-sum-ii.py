'''
https://leetcode.com/problems/combination-sum-ii/description/

Constraints:
1. Can have duplicates
2. One element - used only once
3. All +ve integers
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort to find and skip duplicates later
        candidates.sort()
        output = []
        n = len(candidates)

        def recursion(start, sub, summation):
            if summation == target:
                output.append(sub)
                return
            if summation > target or start == len(candidates):
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Include candidates[i] and move to the next index
                recursion(i + 1, sub + [candidates[i]], summation + candidates[i])

        recursion(0, [], 0)
        return output
    