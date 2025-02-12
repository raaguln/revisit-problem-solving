'''
If addition and subtraction are there, they can be processed later.
Only multiplication and division need to be processed immediately cauz of priority.

'''
class Solution:
    def calculate(self, s: str) -> int:
        # We start with 0 and +, so that we can take in our first number
        current = 0
        prevOperation = '+'
        stack = []
        
        def calculator():
            if prevOperation == '+':
                stack.append(current)
            elif prevOperation == '-':
                stack.append(-current)
            elif prevOperation == '*':
                prev = stack.pop()
                stack.append(prev * current)
            elif prevOperation == '/':
                prev = stack.pop()
                stack.append(int(prev / current))

        for char in s:
            if char.isdigit():
                # Parse number
                current = current * 10 + int(char)
            elif char in '+-/*':
                calculator()
                # Assign the new operation
                prevOperation = char
                # Reset current
                current = 0
        
        # Run it for the last digit
        calculator()

        # Final value = sum of all elements in stack
        return sum(stack)
