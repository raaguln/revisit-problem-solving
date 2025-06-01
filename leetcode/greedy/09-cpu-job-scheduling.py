'''
https://takeuforward.org/Greedy/shortest-job-first-or-sjf-cpu-scheduling

Given a list of job durations representing the time 
it takes to complete each job. Implement the 
Shortest Job First algorithm to find the average 
waiting time for these jobs.

non-preemptive jobs, assuming all jobs arrive at time 0
'''
from typing import List

class Solution:
    def averageWaitingTime(self, jobs: List[int]) -> float:
        jobs.sort()  # Shortest Job First
        total_wait = 0
        curr_time = 0

        for duration in jobs:
            total_wait += curr_time
            curr_time += duration

        return total_wait / len(jobs) if jobs else 0.0

'''
https://takeuforward.org/data-structure/job-sequencing-problem/

Job Sequencing with Deadlines
✅ Problem Summary:
- Each job has:
- A deadline (job must be completed on or before this day).
- A profit (only earned if the job finishes on time).
Each job takes 1 unit of time, and only 1 job can be scheduled at a time.

Goal: Maximize total profit and count of jobs done.

✅ Optimal Strategy:
Sort the jobs in descending order of profit.
For each job, try to assign it to the latest available time slot before or on its deadline.
Use a greedy approach + array to track time slots.

'''
class Job:
    def __init__(self, id: int, deadline: int, profit: int):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def jobScheduling(self, jobs: List[Job]) -> List[int]:
        # Step 1: Sort jobs by descending profit
        jobs.sort(key=lambda job: job.profit, reverse=True)

        # Step 2: Find max deadline to size the time slots
        max_deadline = max(job.deadline for job in jobs)
        slots = [False] * (max_deadline + 1)  # index 0 unused

        job_count = 0
        total_profit = 0

        for job in jobs:
            # Try to place the job at its latest possible slot
            for t in range(job.deadline, 0, -1):
                if not slots[t]:
                    slots[t] = True
                    job_count += 1
                    total_profit += job.profit
                    break

        return [job_count, total_profit]
