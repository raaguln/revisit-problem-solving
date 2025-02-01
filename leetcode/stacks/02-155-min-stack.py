class MinStack:
    def __init__(self):
        # Stores (value, minTillThisPosition)
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((
                val,
                min(val, self.stack[-1][1])
            ))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()[0]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()