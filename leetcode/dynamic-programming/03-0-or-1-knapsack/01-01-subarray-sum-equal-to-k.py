'''
https://leetcode.com/problems/subarray-sum-equals-k/

'''
# Alternative O(n²) brute force for understanding:
class Solution_BruteForce:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        
        return count

'''
Time: O(n)

Array: [1, 2, 3, 1], k = 3

Position 0: sum=1, looking for 1-3=-2 (nope)
Position 1: sum=3, looking for 3-3=0 (yes! empty start)
            Found subarray [1,2] = 3 ✓
Position 2: sum=6, looking for 6-3=3 (yes! from position 1)  
            Found subarray [3] = 3 ✓
Position 3: sum=7, looking for 7-3=4 (nope)

Answer: 2 subarrays
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        # HashMap: prefix_sum -> how many times we've seen it
        sum_count = {0: 1}  # Empty subarray has sum 0
        
        for num in nums:
            prefix_sum += num
            
            # If (prefix_sum - k) exists, we found subarray(s) with sum k
            if (prefix_sum - k) in sum_count:
                count += sum_count[prefix_sum - k]
            
            # Add current prefix_sum to our map
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        return count