# ceil -> smallest value in BST >= key
def find_ceil(root, key):
    ceil_node = None
    current = root
    
    while current:
        if current.val == key:
            return current  # Exact match is the ceiling
        elif current.val < key:
            current = current.right  # Look for larger values
        else:
            # current.val > key, possible ceiling candidate
            ceil_node = current
            current = current.left  # Try to find smaller candidate on left
    
    return ceil_node

# floor -> largest value in BST <= key
def find_floor(root, key):
    floor_node = None
    current = root
    
    while current:
        if current.val == key:
            return current  # Exact match is the floor
        elif current.val > key:
            current = current.left  # Look for smaller values
        else:
            # current.val < key, possible floor candidate
            floor_node = current
            current = current.right  # Try to find a larger candidate on the right
    
    return floor_node  # May be None if no floor found