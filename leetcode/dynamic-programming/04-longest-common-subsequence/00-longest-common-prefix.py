# https://leetcode.com/problems/longest-common-prefix/
# Solution 1
# Time - O(m*n) - m = len of shortest string, n = length of array
# Space - O(m)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        ref = strs[0]
        for i in range(len(ref)):
            for word in strs:
                if i >= len(word) or ref[i] != word[i]:
                    return ref[:i]
        return ref
            