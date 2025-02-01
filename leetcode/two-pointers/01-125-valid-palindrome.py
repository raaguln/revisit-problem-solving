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
