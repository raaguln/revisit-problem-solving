# Right
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        last, penult = 2, 3
        for i in range(4, n+1):
            temp = last + penult
            last = penult
            penult = temp
        return penult