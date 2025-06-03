# https://leetcode.com/problems/task-scheduler/
'''
Wrong, dunno where
'''
import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        max_heap = []
        for key, count in task_count.items():
            heapq.heappush(max_heap, (-count, key))

        time = 0
        task_queue = deque([])
        while max_heap or task_queue:
            time += 1
            # if time == 10:
            #     break
            curr_task = None
            if task_queue and task_queue[0][2] == time:
                curr_task = task_queue.popleft()
            elif max_heap:
                curr_task = heapq.heappop(max_heap)
                # Removing the max_heap effect
                curr_task = (-curr_task[0], curr_task[1])
            else:
                continue
            # If count for task exists, do it and decrease count
            if curr_task and curr_task[0] - 1 > 0:
                next_available_at = time + n + 1
                task_queue.append(
                    (curr_task[0] - 1, curr_task[1], next_available_at)
                )
            # print(time)
            # print(curr_task)
            # print(max_heap)
            # print(task_queue)
            # print()
        return time


'''
Greedy approach
Time: O(T log K)
  T - total number of tasks, K = number of unique tasks
    - counter - O(T)
    - max heap - O(K log K)
    - while loop - O(T log K)
    - cooldown - O(T)

Time: O(T log A), where T = number of tasks, A = unique tasks
Space: O(A) for heap and cooldown queue
'''
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        - greedy approach is needed - start with tasks that occur more 
        no of times, cauz scheduling them later will lead to a lot of extra time
        - max heap to process most frequent, and queue to track cooldown
        '''
        counter = {}
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1
        
        # max heap - process tasks with more count first so that
        # there is no idle time later on
        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, (-v, k))
        
        cooldown = deque()
        time = 0
        while heap or cooldown:
            if heap:
                count, taskId = heapq.heappop(heap)
                # negate the value (from max heap)
                count = -count
                if count > 1:
                    cooldown.append((count-1, taskId, time+n+1))
            time += 1

            while cooldown and cooldown[0][2] == time:
                count, taskId, exitTime = cooldown.popleft()
                heapq.heappush(heap, (-count, taskId))

        return time