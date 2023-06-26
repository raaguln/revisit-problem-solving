n = int(input())
arr = map(int, input().split())

# Solution 1 - works
no_dup = []
for num in arr:
    if num not in no_dup:
        no_dup.append(num)
no_dup.sort()
print(no_dup[-2])

# Solution 2 - doesn't work for [5,5,5,5,5,6]
max = -100
second_max = -101
for num in arr:
    if num > max:
        max = num
    elif num > second_max and num < max:
        second_max = num
print(second_max)


# Solution 3 - fixed solution 2
max = -100
second_max = -101
for num in arr:
    if num > max:
        second_max = max
        max = num
    elif num > second_max  and num < max:
        second_max = num
print(second_max)