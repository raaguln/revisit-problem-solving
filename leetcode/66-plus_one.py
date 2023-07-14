# Attempt n
'''
Lots of silly mistakes
1. Tried to do a simple if else, realized the edge cases with 9 and
the previous numbers
2. Tried to convert it all to int and do int addition and convert it 
back to list, syntax error and left it
'''

# Attempt 1
# 49ms (beats 56.64%)
# 16.3 MB (beats 30.79%)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        last = -1
        while last >= -len(digits):
            if digits[last] == 9:
                digits[last] = 0
                last -= 1
                continue
            elif digits[last] < 9:
                digits[last] += 1
                return digits
        return [1, *digits]

# Attempt 2 - DESTRUCTURING IS COSTLY!!
# 42ms (beats 88.75%)
# 16.3 MB (beats 30.79%)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        last = -1
        while last >= -len(digits):
            if digits[last] == 9:
                digits[last] = 0
                last -= 1
                continue
            elif digits[last] < 9:
                digits[last] += 1
                return digits
        return [1] + digits