class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)

    return root

def buildBST(values):
    root = None
    for v in values:
        root = insertIntoBST(root, v)
    return root
