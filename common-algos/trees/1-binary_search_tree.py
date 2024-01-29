class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

class BinarySearchTree():
    def __init__(self):
      self.nodeCount = 0
      self.root = None
      self.stackPreOrderIter = deque()

    def size(self):
      return self.nodeCount
    
    def isEmpty(self):
      return self.size() == 0