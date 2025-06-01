# https://leetcode.com/problems/candy/description/
'''
Goal - At the end, every kid has a fair number of stickers: 
more than their neighbor if they did better, and the total 
number of stickers is as small as possible.
'''
'''
1. DOES NOT WORK
One left pass does not work because - 

It NEEDS TO GO THROUGH the kids array twice, in two directions:

Left to right:
If a kid has a higher rating than the kid on their left, give them one more candy than the left kid.
(This handles increasing slopes like: 1 → 2 → 3)

Right to left:
Now go the other way. If a kid has a higher rating than the kid on their right, and they don’t already have more candies, increase their candies.
(This handles decreasing slopes like: 5 → 4 → 3)

Both passes are needed because you need to respect both neighbors: the one on the left and the one on the right.
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Step 1: Everyone gets at least one candy

        for i in range(0, n):
            if i-1 >= 0 and ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
            if i+1 < n and ratings[i] > ratings[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)

'''
2. Works. Separate left and right passes
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # Step 1: Everyone gets at least one candy

        # Step 2: Left to Right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Step 3: Right to Left
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Step 4: Sum total candies
        return sum(candies)
