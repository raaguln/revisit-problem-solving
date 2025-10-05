'''
https://leetcode.com/problems/combination-sum/description/

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

            # index OOB or sum exceeds target
            if i >= len(candidates) or summation > target:
                return
            # 
            if sum(sub) == target:
                if sub not in output:
                    output.append(sub)
                return
            
            # 1. include current again
            recursion(i, sub + [candidates[i]])
            # 2. don't include current, move to next
            recursion(i+1, sub)
            # 3. include current, move to next
            recursion(i+1, sub + [candidates[i]])
            
        recursion(0, [])
        return output
    
'''
Avoid duplicate by using set (did not optimize much)
Also, the 3rd call is unnecessary because it is already covered by 1st call
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
            recursion(i, sub + [candidates[i]], summation + candidates[i])
            
        recursion(0, [], 0)
        return output


'''
Constraints:
1. All elements are unique (IMPORTANT)
2. Same element can be used multiple times
3. All +ve integers

backtrack(0, [], 0)
├── backtrack(0, [2], 2)
│   ├── backtrack(0, [2, 2], 4)
│   │   └── backtrack(0, [2, 2, 2], 6) ← pruned
│   │   └── backtrack(1, [2, 2, 3], 7) ← pruned
│   └── backtrack(1, [2, 3], 5) ← valid
├── backtrack(1, [3], 3)
│   └── backtrack(1, [3, 3], 6) ← pruned
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to help pruning and avoid duplicates
        output = []
        
        def backtrack(start: int, current: List[int], current_sum: int):
            if current_sum == target:
                output.append(current[:])
                return
            
            if current_sum > target:
                return
            
            # Explore candidates starting from 'start' index
            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # Since we can reuse same element, 'i' remains the same
                backtrack(i, current, current_sum + candidates[i])
                
                # Backtrack
                current.pop()
        
        backtrack(0, [], 0)
        return output