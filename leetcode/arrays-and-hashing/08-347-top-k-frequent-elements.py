# https://leetcode.com/problems/top-k-frequent-elements/
# Time:  O(nlogn)
# Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        values = count.items()
        values = sorted(values, key=lambda x: x[1], reverse=True)[:k]
        return [num for num, _ in values]
    

'''
Time Complexity: O(N)
    Counting frequencies: O(N)
    Filling countTable: O(N)
    Collecting k elements: At most O(N), but practically O(K)
Space Complexity: O(N) (For countTable and count dictionary)
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        '''
        Each index is the count, and it stores a list of 
        numbers with the particular count
        Eg: 
        nums = [1,1,1,2,2,3]
        countTable = [[], [3], [2], [1], [], [], []]
                       0.  1.   2.   3.   4.  5.  6
        ''' 
        countTable = [[] for i in range(len(nums) + 1)]
        for key, value in count.items():
            countTable[value].append(key)
        
        output = []
        for i in range(len(countTable)-1, -1, -1):
            output.extend(countTable[i])
            if len(output) >= k:
                break

        return output[:k]