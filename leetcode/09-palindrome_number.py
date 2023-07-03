# Attempt 1
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

# Attempt 2
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]

# Attempt 3 - if condition rules out a lot of calculation and helps in faster compute
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string = str(x)
        return string == string[::-1]

# Attempt 4 (worse than #3)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_copy = x
        new_x = 0
        while x_copy > 0:
            new_x = (new_x * 10) + x_copy % 10
            x_copy = x_copy // 10
        return new_x == x