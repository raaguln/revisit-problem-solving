nums = [-1,4,7,12,54,7,2,0,45,3]
for i in range(len(nums)):
  for j in range(i+1, len(nums)):
    if nums[i] > nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
print(nums)