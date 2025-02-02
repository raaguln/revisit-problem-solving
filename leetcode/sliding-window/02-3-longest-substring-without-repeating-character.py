# Did not work cauz of wrong updates to pointers
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        longestSub = set(s[0])
        maxLen = 1
        left, right = 0, 1
        while right < len(s):
            if s[right] in longestSub:
                while s[right] in longestSub:
                    longestSub.remove(s[left])
                    left += 1
                longestSub.add(s[right])
                left = right
                right += 1
            else:
                longestSub.add(s[right])
                maxLen = max(maxLen, right - left + 1)
                right += 1
        return maxLen

# Time: O(n)
# Space: O(min(m, n)), where m is the size of the charset and n is the size of the string
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        chars = set(s[0])
        maxLen = 1
        left, right = 0, 1
        while right < len(s):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right])
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen


