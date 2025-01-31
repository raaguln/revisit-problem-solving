# Time Complexity: O(n * k * log(k)) where n is the number of strings, k is the length of the longest string
# Space Complexity: O(n * k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        return list(hashmap.values())
    
# Time Complexity: O(n * k) where n is the number of strings, k is the length of the longest string
# Space Complexity: O(n * k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        return list(hashmap.values())