# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
# Time: O(logn)
# Space: O(1)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        To find smallest letter greater than target, we just need to find
        the insertion point for the the next letter that comes after target.
        If it exists, it will give index. If not, it will give the index
        where the next letter should have been (which would be our smallest 
        letter in array greater than target).
        1. target = a, next = b, arr = [a,c] => l = 1, so return arr[l]
        2. target = a, next = b, arr = [a,b] => l = 1, so return arr[l]
        Edge case also works - 
        3. target = z, next = {, arr = [a,c] => l = 2, so return you return 
        arr[0]
        '''
        nextLetter = chr(ord(target)+1)
        l, r = 0, len(letters)
        while l < r:
            m = (l+r) // 2
            if letters[m] < nextLetter:
                l = m + 1
            else:
                r = m
        if l >= len(letters):
            return letters[0]
        return letters[l]