'''
https://leetcode.com/problems/task-scheduler-ii/

Right answer, but Time limit Exceeded.
Solution with heap and queue
Time complexity: O(T) - where T is the time taken to process all the tasks
'''
from collections import deque

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        queue = deque()
        cooldown = set()
        time = 0
        i = 0
        while i < len(tasks):
            # Check if tasks can be removed first
            # cauz - you need to process at the given time if you are freeing it
            while queue and queue[0][1] <= time:
                task, _ = queue.popleft()
                cooldown.remove(task)

            if tasks[i] not in cooldown:
                queue.append((tasks[i], time + space + 1))
                cooldown.add(tasks[i])
                i += 1
                
            time += 1

        return time


'''
Simpler solution
Time complexity: O(n)
Space complexity: O(n)
'''
from collections import deque

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        lastSeen = {}
        time = 0

        for task in tasks:
            if task in lastSeen:
                time = max(time, lastSeen[task] + space + 1)
            lastSeen[task] = time
            time += 1

        return time