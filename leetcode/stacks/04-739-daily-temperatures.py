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
    

# Cleaner solution using template
# Time: O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Next greater element
        n = len(temperatures)
        waitDays = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                nextSmallestI = stack.pop()
                waitDays[nextSmallestI] = i - nextSmallestI
            stack.append(i)
        return waitDays