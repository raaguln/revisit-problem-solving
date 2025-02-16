# Wrong - doesn't work for [4,4,4,1,4]
# Time: O(n * 2^n)
# Space: O(n * 2^n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        def recursion(i, subset):
            if i == len(nums):
                if subset not in output:
                    output.append(subset)
                return
            recursion(i+1, subset + [nums[i]])
            recursion(i+1, subset)
            pass

        recursion(0, [])
        return output
    

# Time: O(n * 2^n)
# Space: O(n * 2^n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        def recursion(i, subset):
            if i == len(nums):
                if subset not in output:
                    output.append(subset)
                return
            recursion(i+1, subset + [nums[i]])
            recursion(i+1, subset)
            pass

        recursion(0, [])
        return output

# Time: O(n * 2^n)
# Space: O(n * 2^n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        # arrange in ascending order
        sortCount = [0 for _ in range(21)]
        for num in nums:
            sortCount[num+10] += 1
        final = []
        for i in range(len(sortCount)):
            final.extend(
                [i-10] * sortCount[i]
            )

        def recursion(i, subset):
            if i == len(final):
                if subset not in output:
                    output.append(subset)
                return
            recursion(i+1, subset + [final[i]])
            recursion(i+1, subset)
            pass

        recursion(0, [])
        return output


