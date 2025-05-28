"""
https://leetcode.com/problems/course-schedule/description/

DFS (Time limit exceeded)
Time Complexity:
In the worst case, the dfs will be called on each course multiple times.
Since you do not memoize the results or mark courses as completed, the same subproblems (courses) can be revisited repeatedly.
The complexity can degrade to O(N × E) where:
N = number of courses (numCourses)
E = number of edges (prerequisites)
This happens because each DFS call can traverse edges multiple times without pruning.

Space Complexity:
The recursion stack can go as deep as the longest chain of prerequisites, which is O(N) in the worst case.
The visited set can also grow to size O(N).
The prereqs dictionary takes O(N + E) space.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for sub, prevSub in prerequisites:
            prereqs[sub].append(prevSub)

        visited = set()
        def dfs(course):
            # Loop detected
            if course in visited:
                return False
            # No prereqs
            if prereqs[course] == []:
                return True
            
            # Has prereqs - 
            # Are all prereq courses finishable?
            # NOTE - 
            # - add to visited -> detecting cycles in a directed graph using DFS
            # - if you keep it in, we will detect false cycles and throw error
            # Also - 
            # - visited = currently exploring path (temporary state)
            # - finished (or cleared prereqs) = already fully explored, no cycles found
            visited.add(course)
            for prevSub in prereqs[course]:
                if not dfs(prevSub):
                    return False
            visited.remove(course)
            return True

        # Doing this because our graph can be disconnected
        # Like 1 -> 2 and 3 -> 4
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True



"""
Optimized DFS
Time -
Here, once a course is determined finishable, its prerequisites are cleared (prereqs[course] = []), so subsequent calls to dfs(course) return immediately.
This memoization ensures each course is processed at most once.
Each edge (prerequisite) is traversed at most once.
Overall time complexity is O(N + E), where:
N is the number of courses
E is the number of prerequisite edges

Space - 
The recursion stack depth remains O(N) in the worst case.
The visited set is still at most size O(N).
The prereqs dictionary still occupies O(N + E) space.
Because of memoization, no redundant recursive calls increase stack usage beyond that.
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for sub, prevSub in prerequisites:
            prereqs[sub].append(prevSub)

        visited = set()
        def dfs(course):
            # Loop detected
            if course in visited:
                return False
            # No prereqs
            if prereqs[course] == []:
                return True
            
            # Has prereqs - 
            # Are all prereq courses finishable?
            # NOTE - 
            visited.add(course)
            for prevSub in prereqs[course]:
                if not dfs(prevSub):
                    return False
            visited.remove(course)
            # ADDITION
            prereqs[course] = []
            return True

        # Doing this because our graph can be disconnected
        # Like 1 -> 2 and 3 -> 4
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True