# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
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