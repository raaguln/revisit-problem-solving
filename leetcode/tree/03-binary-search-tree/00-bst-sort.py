# Inorder traversal of BST gives you sorted array

sorted_array = []

def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    sorted_array.append(root.val)
    inorder_traversal(root.right)