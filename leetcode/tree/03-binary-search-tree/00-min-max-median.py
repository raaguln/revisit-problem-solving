'''
Min - left most value
Max - right most value
Median - in order traversal, then middle
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1. RECURSIVE
def find_min(node):
    if node is None:
        return None
    if node.left is None:
        return node.val
    return find_min(node.left)

def find_max(node):
    if node is None:
        return None
    if node.right is None:
        return node.val
    return find_max(node.right)

# 2. ITERATIVE
def find_min_iterative(node):
    if node is None:
        return None
    current = node
    while current.left:
        current = current.left
    return current.val

def find_max_iterative(node):
    if node is None:
        return None
    current = node
    while current.right:
        current = current.right
    return current.val

# 3. MEDIAN
def find_median_bst(root):
    if not root:
        return None
    
    sorted_array = []
    def inorder_traversal(root):
        if not root:
            return
        inorder_traversal(root.left)
        sorted_array.append(root.val)
        inorder_traversal(root.right)
    
    inorder_traversal(root)
    
    n = len(sorted_array)
    if n % 2 == 1:
        return sorted_array[n // 2]
    else:
        middle1 = sorted_array[n // 2 - 1]
        middle2 = sorted_array[n // 2]
        return (middle1 + middle2) / 2