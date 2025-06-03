'''
https://takeuforward.org/data-structure/subset-sum-sum-of-all-subsets/

Given an array print all the sum of the subset generated from it, in the increasing order.
'''
def subset_sums(arr):
    def helper(index, current_sum):
        if index == len(arr):
            result.append(current_sum)
            return
        # include
        helper(index + 1, current_sum + arr[index])
        # exclude
        helper(index + 1, current_sum)
    
    result = []
    helper(0, 0)
    result.sort()
    for val in result:
        print(val)
