# Attempt 1 - XXX
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [1]
        cache = {}
        max_1, max_2 = [0, 0], [0, 0]
        for n in nums:
            cache[n] = cache.get(n, 0) + 1
        for n in cache.keys():
            count = cache[n]
            if count > max_1[1]:
                max_1 = [n, count]
            elif count > max_2[1] and count < max_1[1]:
                max_2 = [n, count]
        return [max_1[0], max_2[0]]

# Attempt 2 - XXX
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [1]
        cache = {}
        for n in nums:
            cache[n] = cache.get(n, 0) + 1
        unique_nums = list(cache.keys())
        counts = list(cache.values())
        sorted_counts = sorted(counts, reverse=True)
        final = []
        for i in range(k):
            final.append(
                unique_nums[
                    counts.index(sorted_counts[i])
                ]
            )
        return final

# Attempt 3
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [1]
        cache = {}
        for n in nums:
            cache[n] = cache.get(n, 0) + 1
        nums_by_count = sorted(cache.items(), key=lambda x: x[1], reverse=True)
        return map(lambda x: x[0], nums_by_count[0:k])