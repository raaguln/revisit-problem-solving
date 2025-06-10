# https://leetcode.com/problems/generate-parentheses/
# Time Complexity: O(4^n/sqrt(n)) -> complex approximation due to the if conditions
# Time Compexity: O(2^(2n)) -> 2n because we have 2n characters in the string
# - 2 choices for each character
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def generate(string, openBrackets, closeBrackets):
            if openBrackets == closeBrackets == n:
                output.append(string)
                return
            # If we can still add an open parenthesis
            if openBrackets < n:
                generate(string + '(', openBrackets+1, closeBrackets)
            # If we can add a closing parenthesis (only if it won't exceed open)
            if openBrackets > closeBrackets:
                generate(string + ')', openBrackets, closeBrackets+1)

        generate('', 0, 0)
        return output

# Equally optimal
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        
        def backtrack(path, open_count, close_count):
            # Base case: we've used all n pairs
            if len(path) == 2 * n:
                output.append(''.join(path))
                return
            
            # Add opening parenthesis if we haven't used all n
            if open_count < n:
                path.append('(')
                backtrack(path, open_count + 1, close_count)
                path.pop()
            
            # Add closing parenthesis if it won't make string invalid
            if open_count > close_count:
                path.append(')')
                backtrack(path, open_count, close_count + 1)
                path.pop()
        
        backtrack([], 0, 0)
        return output