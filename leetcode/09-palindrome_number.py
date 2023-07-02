class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        length = len(x_list)
        palindrome = True
        for i in range(length // 2):
            if(x_list[i] != x_list[-(i+1)]):
                palindrome = False
                break
        return palindrome