# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        results = []
        target_length = len(digits)
        
        def recursion(i, path):
            if len(path) == target_length:
                results.append(path)
                return
            
            number = str(digits[i])
            for char in mapping[number]:
                recursion(i+1, path+char)

        recursion(0, '')
        return results
