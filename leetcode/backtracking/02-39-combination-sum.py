'''
Constraints:
1. All elements are unique (IMPORTANT)
2. Same element can be used multiple times
3. All +ve integers
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def recursion(i, sub):
            summation = sum(sub)
            if i >= len(candidates) or summation > target:
                return
            if sum(sub) == target:
                if sub not in output:
                    output.append(sub)
                return
            recursion(i, sub + [candidates[i]])
            recursion(i+1, sub)
            recursion(i+1, sub + [candidates[i]])
            
        recursion(0, [])
        return output
    
'''
Avoid duplicate by using set (did not optimize much)
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        visited = {}
        def recursion(i, sub):
            summation = sum(sub)
            if i >= len(candidates) or summation > target:
                return
            if summation == target:
                key = tuple(sub)
                if key not in visited:
                    output.append(sub)
                    visited[key] = None
                return
            recursion(i, sub + [candidates[i]])
            recursion(i+1, sub)
            recursion(i+1, sub + [candidates[i]])
            
        recursion(0, [])
        return output

'''
Maintain running sum to avoid complex computation
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Optimize 1 - running sum
        output = []
        def recursion(i, sub, summation):
            # Maintain running sum to avoid complex computation
            # summation = sum(sub)
            if i >= len(candidates) or summation > target:
                return
            if summation == target:
                if sub not in output:
                    output.append(sub)
                return
            # Old summation
            recursion(i+1, sub, summation)
            # New summation
            summation += candidates[i]
            recursion(i, sub + [candidates[i]], summation)
            recursion(i+1, sub + [candidates[i]], summation)
            
        recursion(0, [], 0)
        return output