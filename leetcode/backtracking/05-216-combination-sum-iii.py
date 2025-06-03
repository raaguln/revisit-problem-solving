# https://leetcode.com/problems/combination-sum-iii/
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        
        def recursion(number, sub, total):
            sub_length = len(sub)
            if total == n and sub_length == k:
                results.append(sub)
                return
            if number > 9 or sub_length > k or total > n:
                return
            
            # include, and go to next
            recursion(number+1, sub+[number], total+number)

            # exclude, and go to next
            recursion(number+1, sub, total)

        recursion(1, [], 0)
        return results