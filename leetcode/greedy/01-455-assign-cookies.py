# https://leetcode.com/problems/assign-cookies/description/
# Time: O(n log n + m log m)
# Space: O(1)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # use smallest cookie to satisfy the least greedy child
        # handle the least greedy children first
        g.sort()
        # hand out the smallest cookie first, so that
        # more greedy children will have bigger cookies
        s.sort()

        children = 0
        cookie = 0
        while children < len(g) and cookie < len(s):
            # if cookie is big enough, greed satisfied
            if g[children] <= s[cookie]:
                children += 1
            # Whether or not the current cookie satisfies 
            # the current child, it is either assigned or too small
            cookie += 1

        return children