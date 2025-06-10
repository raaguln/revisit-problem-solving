'''
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/description/

Serialization is the process of converting a data 
structure or object into a sequence of bits so that 
it can be stored in a file or memory buffer, or 
transmitted across a network connection link to be 
reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an 
N-ary tree. An N-ary tree is a rooted tree in which 
each node has no more than N children. There is no restriction 
on how your serialization/deserialization algorithm should work. 
You just need to ensure that an N-ary tree can be serialized to a 
string and this string can be deserialized to the original tree structure.
'''

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes an N-ary tree to a single string."""
        serial = []

        def dfs(node):
            if not node:
                return
            # Append current node's value and number of children
            serial.append(str(node.val))
            serial.append(str(len(node.children)))
            for child in node.children:
                dfs(child)

        dfs(root)
        return ' '.join(serial)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree."""
        if not data:
            return None

        tokens = data.split()
        self.index = 0

        def dfs():
            if self.index >= len(tokens):
                return None
            # Read node value and number of children
            val = int(tokens[self.index])
            self.index += 1
            size = int(tokens[self.index])
            self.index += 1
            node = Node(val)
            node.children = []
            for _ in range(size):
                node.children.append(dfs())
            return node

        return dfs()
