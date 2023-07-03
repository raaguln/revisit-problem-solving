# Attempt 1
'''
Initially did this - 
  cache[key] = cacheVal.append(word)

...instead of this - 
  cacheVal.append(word)
  cache[key] = cacheVal

.append() did not return any value and was throwing an error.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for word in strs:
            key = ''.join(sorted(word))
            cacheVal = cache.get(key, [])
            cacheVal.append(word)
            cache[key] = cacheVal
        return cache.values()