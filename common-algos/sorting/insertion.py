nums = [8, -1,4,7,12,54,7,2,0,45,3]
for i in range(1, len(nums)):
  current = nums[i]
  j = i - 1
  while j >= 0 and nums[j] > current:
    nums[j+1] = nums[j]
    j -= 1
  nums[j+1] = current
print(nums)