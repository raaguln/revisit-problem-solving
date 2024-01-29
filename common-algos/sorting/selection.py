nums = [8,-1,4,7,12,54,7,2,0,45,3]
for i in range(len(nums)):
  min_val = i
  for j in range(i+1, len(nums)):
    if nums[min_val] > nums[j]:
      min_val = j
  if min != i:
    nums[i], nums[min_val] = nums[min_val], nums[i]
print(nums)