# given m lists, which are sorted,
# return sorted array

# 1. Add everything to heap and pop
# Time: O(n log n) - where n is the total number of elements
#   - (log n = heap push) x n times


# 2. Only keep the minimum value from each list at each pop
# Time: O(n log m) - where m is the number of lists
#   - (log m = heap push) x n times

def merge_sorted_lists(arrays):
    arrays = [[1,4,5], [1,3,4], [2,6]]
    heap = []

    # Add just the 1st elem from each arr to the heap
    # (value, array pos, element index)
    for i, array in enumerate(lists):
        if array:
            heappush(heap, (array[0], i, 0))

    result = []
    while heap:
        val, pos, i = heappop(heap)
        result.append(val)
        # Add next element from poped array if exists
        if i + 1 < len(arrays[pos]):
            heappush(
                heap,
                (arrays[pos][i+1], pos, i+1)
            )
    return result