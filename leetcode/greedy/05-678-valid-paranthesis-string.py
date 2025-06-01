'''
https://leetcode.com/problems/valid-parenthesis-string/

Does not work!!
Logic -
- left -> consider * as (
- right -> consider * as )
- empty -> consider * as ""

This assumes that the * will always be only '(' or only ')'
but it can be flexible
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = 0
        right = 0
        empty = 0

        for char in s:
            if char == '(':
                left += 1
                right += 1
                empty += 1
            elif char == ')':
                left -= 1
                right -= 1
                empty -= 1
            
            # char is '*'
            else:
                left += 1
                right -= 1
                # do nothing for empty
        if left or right or empty:
            return True
        return False

'''
Goal - always have count ( = 0

low - minimum possible number of unmatched '('
high - maximum possible number of unmatched ')'
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0   # min possible '(' count
        high = 0  # max possible '(' count
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low = max(low - 1, 0)
                high -= 1
            else:  # char == '*'
                low = max(low - 1, 0)  # treat '*' as ')'
                high += 1              # treat '*' as '('
                                       # treat '*' as ''
            
            # Even in best case, we have more ')'
            # than '(', so invalid
            if high < 0:
                return False
        
        # there is a way to balance the brackets
        # either by doing (, ) or empty
        return low == 0
