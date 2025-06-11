# Time: O(logn)
# Space: O(1)
# CODE 1 - lower bounds binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m+1
            else:
                r = m
        if l < len(nums) and nums[l] == target:
            return l
        return -1

# CODE 2 - early stop binary search
# Time: O(logn)
# Space: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m
        if l < len(nums) and nums[l] == target:
            return l
        return -1

'''
That said, Code 2 can be marginally faster on 
large inputs in practice due to early exit — 
but only when the target appears and is hit early. 
From an algorithmic complexity perspective, they are both O(log n).
'''

'''
This loop terminates when l == r, but never actually checks 
index l directly inside the loop unless the condition 
nums[m] == target is satisfied.

So if the loop exits without returning, and your binary 
search logic narrows the window down to a single element 
l == r, the element at nums[l] could still be the target.

But you wouldn’t have returned from inside the loop 
because m != target at any previous step (or you 
never checked it in Code 1).
'''