'''
https://leetcode.com/problems/hand-of-straights/

Time: O(N log N) due to heap operations and looping through hand.
Space: O(N) for counter and heap.
'''
import heapq
from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]  # smallest available card
            for i in range(start, start + groupSize):
                if count[i] == 0:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    # remove from heap if it was the smallest and now exhausted
                    if i != min_heap[0]:
                        return False  # not in correct order
                    heapq.heappop(min_heap)
        return True
