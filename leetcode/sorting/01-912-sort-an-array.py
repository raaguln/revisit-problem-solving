# Bubble sort
# Time: O(n^2)
# Space: O(1)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Bubble sort
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

# Selection sort
# Time: O(n^2)
# Space: O(1)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Selection sort
        n = len(nums)
        for i in range(n):
            minVal = nums[i]
            minIndex = i
            for j in range(i+1, n):
                if nums[j] < minVal:
                    minVal = nums[j]
                    minIndex = j
            if minIndex != i:
                nums[i], nums[minIndex] = nums[minIndex], nums[i]
        return nums
    
# Insertion sort
# Time: O(n^2)
# Space: O(1)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Insertion sort
        for i in range(1, len(nums)):
            current = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > current:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = current
        return nums

# Merge sort
# Time: O(nlogn)
# Space: O(n) - O(nlogn) for recursive calls, O(n) for the lists
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            mid = len(nums) // 2
            left, right = nums[:mid], nums[mid:]
            left, right = mergeSort(left), mergeSort(right)

            output = []
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    output.append(left[l])
                    l += 1
                else:
                    output.append(right[r])
                    r += 1
            
            # Remaining in left
            while l < len(left):
                output.append(left[l])
                l += 1
            
            # Remaining in right
            while r < len(right):
                output.append(right[r])
                r += 1
            
            return output
        
        return mergeSort(nums)
            
# Quick sort / Pivot sort
# Time: O(nlogn)
# Space: O(n) - O(nlogn) for recursive calls, O(n) for the lists
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def pivotSort(nums):
            if len(nums) <= 1:
                return nums
            pivot = nums[len(nums) // 2]

            left, middle, right = [], [], []
            for num in nums:
                if num > pivot:
                    right.append(num)
                elif num == pivot:
                    middle.append(num)
                else:
                    left.append(num)
            return pivotSort(left) + middle + pivotSort(right)
        
        return pivotSort(nums)
            
# Bucket sort
# Time: O(n)
# Space: O(k) - k is the range of the input
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maxVal = 5*(10**4)
        '''
        This only works if it can have only integer values!!

        To include both +ve and -ve maxVal, use 2 * maxVal
        Note - 
            -5*(10**4) => index=0
            0          => index=maxVal
            5*(10**4)  => index=2*maxVal
        '''
        buckets = [0] * (2 * maxVal + 1)
        for n in nums:
            buckets[n + maxVal] += 1

        output = []
        for i in range(2 * maxVal + 1):
            if buckets[i]:
                output.extend([i - maxVal] * buckets[i])
        return output

            