# https://leetcode.com/problems/valid-palindrome/
# Time: O(n)
# Space: O(n) - filtered list and its reversed version
class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [x.lower() for x in s if x.isalnum()]
        return arr[::-1] == arr
    
# Time: O(n)
# Space: O(n) - filtered list and some constants
class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [x.lower() for x in s if x.isalnum()]
        left, right = 0, len(arr)-1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left += 1
            right -= 1
        return True

# Time: O(n)
# Space: O(1) - no extra space used 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # arr = [x.lower() for x in s if x.isalnum()]
        left, right = 0, len(s)-1
        while left < right:
            c1 = s[left].lower()
            c2 = s[right].lower()
            if not c1.isalnum():
                left += 1
                continue
            if not c2.isalnum():
                right -= 1
                continue
            if c1 != c2:
                return False
            left += 1
            right -= 1
        return True
