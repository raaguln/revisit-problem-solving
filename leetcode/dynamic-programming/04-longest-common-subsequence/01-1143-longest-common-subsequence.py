'''
Subsequences / subarray - 
- maintains order
- can be contigious or non-contigious

Subarray - 
- maintains order
- always contigious
Eg: {1,3,2}
{1,2}, {3,2} -> subsequence
{2,1} -> not subsequence

'''

'''
Brainstorm:
edge cases - 
1. if string is same, return length

Logic - 
1. if the first char are same, length of lcs is 1 + lcs of rest of the string


'''