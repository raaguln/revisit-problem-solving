# BUCKET SORT

# 1. Normal Sort
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        decreasing = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return "".join([char*count for char, count in decreasing])

# 2. Bucket Sort
# Time: O(n)
# Space: O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        maxCount = max(counter.values())
        buckets = [[] for _ in range(maxCount+1)]
        for char, count in counter.items():
            buckets[count].append(char*count)
        
        output = []
        for i in range(len(buckets)-1, -1, -1):
            if len(buckets[i]):
                output.extend(buckets[i])
        return "".join(output)