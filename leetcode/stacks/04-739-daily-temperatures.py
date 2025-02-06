# Monotonic strictly decreasing stack
# Time: O(n)
# Space: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, old_i = stack.pop()
                output[old_i] = i - old_i
            stack.append((
                temperatures[i],
                i
            ))
        return output