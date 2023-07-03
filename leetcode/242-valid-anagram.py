# Attempt 1
# Good runtime, bad memory
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        if s_list == t_list:
            return True
        return False

# Attempt 2
# Bad runtime, Better memory
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Attempt 3
# Mediocre runtime, Good memory
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