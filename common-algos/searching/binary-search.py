def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right -= 1
        else:
            left += 1
    return "Element not in the list!"

nums = [1,2,3,4,5,6,7,8,9]
print(binary_search(nums, 6))