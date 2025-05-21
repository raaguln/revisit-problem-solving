# Time: O(n log n + m log m)
# Space: O(1)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Greedy approach
        g.sort()
        s.sort()

        # 
        children = 0
        cookie = 0
        while children < len(g) and cookie < len(s):
            if g[children] <= s[cookie]:
                children += 1
            cookie += 1
        return children