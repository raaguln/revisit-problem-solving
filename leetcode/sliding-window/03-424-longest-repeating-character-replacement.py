# Incorrect solution
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        longestSubLength = 0

        left, right = 0, 1
        otherCount = 0
        while right < len(s):
            rightStart = right
            while right < len(s) and s[left] != s[right]:
                otherCount += 1
                right += 1
                if otherCount > k:
                    otherCount = 0
                    left = rightStart
                    right = left + 1
                    break
            if right < len(s) and s[left] == s[right]:
                right += 1
                longestSubLength = max(longestSubLength, right-left+1)
        return longestSubLength

# Also didn't work
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        longestSubLength = 0
        left, right = 0, 0
        mods = k
        while right < len(s):
            if s[left] == s[right]:
                longestSubLength = max(longestSubLength, right - left + 1)
                right += 1
            elif mods > 0:
                mods -= 1
                longestSubLength = max(longestSubLength, right - left + 1)
                right += 1
            else:
                while left + 1 < right and s[left] == s[left+1]:
                    left += 1
                left += 1
                mods += 1
        return longestSubLength


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  
        left = 0

        # Stores max frequency of any character in the window
        max_freq = 0
        max_length = 0
        
        for right in range(len(s)):
            # Get count of current character
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # Check if the remaining characters can be replaced
            # (window size) - max_freq > k
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
   

# # Works
# # Time: O(n)
# # Space: O(n)
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         l1, l2 = len(s1), len(s2)
#         if l1 > l2:
#             return False

#         count1, count2 = [0] * 26, [0] * 26
#         for i in range(l1):
#             c1, c2 = s1[i], s2[i]
#             count1[ord(c1) - ord('a')] += 1
#             count2[ord(c2) - ord('a')] += 1
        
#         if count1 == count2:
#             return True

#         # Maintain the fixed window size
#         for right in range(l1, l2):
#             count2[ord(s2[right]) - ord('a')] += 1
#             count2[ord(s2[right-l1]) - ord('a')] -= 1
#             if count1 == count2:
#                 return True
#         return False
