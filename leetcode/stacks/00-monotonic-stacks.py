'''
1. Next greater element
Monotonic decreasing stack (strictly decreasing)
Time: O(n)
Space: O(n)

Note - change the > to >= for non-strictly decreasing stack
'''

def printStack(stack, originalArray):
    print("Stack: ", end="")
    for i in stack:
        print(originalArray[i], end=" ")
    print()


nums = [5,7,2,8,0,3,3,6,7]
n = len(nums)
output = [-1] * n

# Stores indices only
stack = []
for i in range(len(nums)):
    while stack and nums[i] > nums[stack[-1]]:
        index = stack.pop()
        output[index] = nums[i]
    stack.append(i)
    printStack(stack, nums)
print(nums)
print(output)

'''
2. Next smaller element
Monotonic increasing stack (strictly increasing)
Time: O(n)
Space: O(n)
'''
nums = [5,7,2,8,0,3,3,6,7]
n = len(nums)
output = [-1] * n

# Stores indices only
stack = []
for i in range(len(nums)):
    while stack and nums[i] < nums[stack[-1]]:
        index = stack.pop()
        output[index] = nums[i]
    stack.append(i)
    printStack(stack, nums)
print(nums)
print(output)

'''
3. Previous greater element
'''
nums = [5,7,2,8,0,3,3,6,7]
n = len(nums)
output = [-1] * n

# Stores indices only
stack = []
for i in range(len(nums)-1, -1, -1):
    while stack and nums[i] > nums[stack[-1]]:
        index = stack.pop()
        output[index] = nums[i]
    stack.append(i)
    printStack(stack, nums)
print(nums)
print(output)

'''
4. Previous smaller element
'''
nums = [5,7,2,8,0,3,3,6,7]
n = len(nums)
output = [-1] * n

# Stores indices only
stack = []
for i in range(len(nums)-1, -1, -1):
    while stack and nums[i] < nums[stack[-1]]:
        index = stack.pop()
        output[index] = nums[i]
    stack.append(i)
    printStack(stack, nums)
print(nums)
print(output)