# https://leetcode.com/problems/binary-search-tree-iterator/description/

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_left_branch(root)

    def _push_left_branch(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the next node from the stack
        node = self.stack.pop()
        # If it has a right child, push all its leftmost descendants
        if node.right:
            self._push_left_branch(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0