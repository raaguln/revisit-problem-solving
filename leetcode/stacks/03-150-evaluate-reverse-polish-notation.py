# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Time: O(n)
# Space: O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # Mistake 1: Here, t.isdigit() / t.isnumeric() was failing for negative numbers
            if t not in '+-/*':
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    stack.append(int(a / b))
        return stack[0]