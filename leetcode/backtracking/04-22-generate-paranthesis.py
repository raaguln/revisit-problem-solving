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
            if openBrackets < n:
                generate(string + '(', openBrackets+1, closeBrackets)
            if openBrackets > closeBrackets:
                generate(string + ')', openBrackets, closeBrackets+1)
            

        openBrackets = closeBrackets = 0
        generate('', openBrackets, closeBrackets)
        return output