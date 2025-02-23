# https://leetcode.com/problems/group-anagrams/description/

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
    

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:

            count = {}
            for char in word:
                if char not in count:
                    count[char] = 0
                count[char] += 1
            

            key = "".join(sorted(word))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        return list(hashmap.values())


# Time Complexity: O(n * k) where n is the number of strings, k is the length of the longest string
# Space Complexity: O(n * k)

# (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
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