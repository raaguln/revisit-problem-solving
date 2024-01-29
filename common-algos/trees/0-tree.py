class Tree:
  def depth(self, n):
    if self.is_root(n):
      return 0
    else:
      return 1 + self.depth(self.parent(n))