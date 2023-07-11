# Attempt 1 - runtime error
# pop from empty list - len should be <1 instead of 2
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.isdigit() or len(t) > 2:
                stack.append(int(t))
                continue
            # No need to check as the notation is always right
            n2 = stack.pop()
            n1 = stack.pop()
            if t == '+':
                stack.append(n1 + n2)
            elif t == '-':
                stack.append(n1 - n2)
            elif t == '*':
                stack.append(n1 * n2)
            elif t == '/':
                result = n1 // n2
                stack.append(result if result > 0 else 0)
            else:
                stack.append(int(t))
        return stack.pop()

# Attempt 2 - Wrong answer
# ["4","-2","/","2","-3","-","-"]
# Output -5
# Expected -7
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # len(t) > 1 -> for negative numbers
            if t.isdigit() or len(t) > 1:
                stack.append(int(t))
                continue
            # No need to check as the notation is always right
            n2 = stack.pop()
            n1 = stack.pop()
            if t == '+':
                stack.append(n1 + n2)
            elif t == '-':
                stack.append(n1 - n2)
            elif t == '*':
                stack.append(n1 * n2)
            elif t == '/':
                result = n1 // n2
                stack.append(result if result > 0 else 0)
            else:
                stack.append(int(t))
        return stack.pop()

# Attempt 3 - best
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # len(t) > 1 -> for negative numbers
            if t.isdigit() or len(t) > 1:
                stack.append(int(t))
                continue
            # No need to check as the notation is always right
            n2 = stack.pop()
            n1 = stack.pop()
            if t == '+':
                stack.append(n1 + n2)
            elif t == '-':
                stack.append(n1 - n2)
            elif t == '*':
                stack.append(n1 * n2)
            elif t == '/':
                stack.append(int(n1 / n2))
        return stack.pop()