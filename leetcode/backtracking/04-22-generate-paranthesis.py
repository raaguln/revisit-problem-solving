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