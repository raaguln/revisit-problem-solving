# Attempt 1 - forgot upper case
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        string = ''.join(filter(lambda char: char.isalnum(), s))
        if string != string[::-1]:
            return False
        return True

# Attempt 2 - meh performance, bad memory
# 70ms (beats 33.72%)
# 22.2MB (beats 6.51%)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        string = ''.join(map(str.lower, filter(str.isalnum, s)))
        if string != string[::-1]:
            return False
        return True

# Attempt 3 - two pointers.
# 67ms (beats 45.3%)
# 17.1MB (beats 52.25%)
# Used - new_s = ''.join([char.lower() if char.isalnum() else '' for char in s]), 76ms!!
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        a = 0
        b = len(s) - 1
        while b > a:
            if not s[a].isalnum():
                a += 1
                continue
            if not s[b].isalnum():
                b -= 1
                continue
            if s[a].lower() != s[b].lower():
                return False
            a += 1
            b -= 1
        return True

# Attempt 3 - worse than #2
# 70ms (beats 33.72%)
# 17.9MB (beats 19.24%)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        new_s = ''.join(filter(str.isalnum, s))
        a = 0
        b = len(new_s) - 1
        while b > a:
            if new_s[a].lower() != new_s[b].lower():
                return False
            a += 1
            b -= 1
        return True