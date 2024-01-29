def sum_rec(nums):
	if len(nums) == 0:
		return 0
	return nums[0] + sum_rec(nums[1:])

nums = [1,2,3,4,5]
print(sum_rec(nums))