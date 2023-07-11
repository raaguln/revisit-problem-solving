# WIP
# Attempt 1
# Forgot to check length before -
#   1. popping
#   2. at the end before returning true
# And forgot to return true, forgot to 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '{': '}',
            '[': ']',
            '(': ')',
        }
        for b in list(s):
            if b not in mapping.keys() and b not in mapping.values():
                return False
            if b in mapping.keys():
                stack.append(b)
            elif b in mapping.values():
                if len(stack) == 0:
                    return False
                prev_b = stack.pop()
                if mapping[prev_b] != b:
                    return False
        if len(stack) != 0:
            return False
        return True