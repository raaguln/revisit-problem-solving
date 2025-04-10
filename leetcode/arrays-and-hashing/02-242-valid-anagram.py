# https://leetcode.com/problems/valid-anagram/description/
# Time - O(nlogn)
# Space - O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Attempt 3
# Time - O(n)
# Space - O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        cacheS = {}
        cacheT = {}
        for i in range(len(s)):
            cacheS[s[i]] = cacheS.get(s[i], 0) + 1
            cacheT[t[i]] = cacheT.get(t[i], 0) + 1
        return cacheS == cacheT
    
# Attempt 4
# Time - O(n)
# Space - O(n)    
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)