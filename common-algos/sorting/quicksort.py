# Divide and conquer
def quicksort(array):
  # Base case
  if len(array) < 2:
    return array
  # Recursive case
  else:
    pivot = array[0]
    left, right = [], []
    for i in array[1:]:
      if i <= pivot:
        left.append(i)
      else:
        right.append(i)
  return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([10, 5, 2, 3]))
