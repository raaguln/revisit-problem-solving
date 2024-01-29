def mergesort(nums):
  if len(nums) == 1:
    return nums
  mid = int(len(nums) / 2)
  left, right = nums[:mid], nums[mid:]
  # Recursion to get L and R
  # which will be sorted cause we rewrite over OG arr
  mergesort(left)
  mergesort(right)
  
  #Two pointer Sort
  i = j = k = 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      nums[k] = left[i]
      k += 1
      i += 1
    else:
      nums[k] = right[j]
      k += 1
      j += 1
  # Remaining Elements
  while i < len(left):
    nums[k] = left[i]
    k += 1
    i += 1            
  while j < len(right):
    nums[k] = right[j]
    k += 1
    j += 1

nums = [8,-1,4,7,12,54,7,2,0,45,3]
mergesort(nums)
print(nums)