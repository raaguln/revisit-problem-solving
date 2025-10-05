'''
K sorted array
- Every element in the array is at most k positions 
away from its position in the fully sorted array.
- element at index i -> can be in between (i - k and i + k) index
in sorted array
- 
'''

# Time: O(n log k) [full sorting is O(n log n)]
from heapq import heapify, heappop, heappush

def sort_k_sorted_array(arr, k):
    # maintain window of upto k elements
    heap = arr[:k+1]
    heapify(heap)

    result = []
    for i in range(k+1, len(arr)):
        # add min_val to result in window
        min_val = heappop(heap)
        result.append(min_val)

        # add new element in heap
        heappush(heap, arr[i])
    
    # handle the remaining elements in heap
    while heap:
        min_val = heappop(heap)
        result.append(min_val)

    return result