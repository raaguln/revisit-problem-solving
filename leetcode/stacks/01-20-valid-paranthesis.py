# https://leetcode.com/problems/valid-parentheses/description/
# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. Starts with } -> False
        2. As we keep progressing, extra } -> False
        3. For every } -> pop out existing {
        4. at end, if stack is empty -> True
        '''
        stack = []
        mapping = {
            '}': '{',
            ')': '(',
            ']': '[',
        }
        openBrackets = mapping.values()
        for i in range(len(s)):
            if s[i] in openBrackets:
                stack.append(s[i])
            else:
                if stack and mapping[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True