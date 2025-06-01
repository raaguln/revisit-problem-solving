'''
https://leetcode.com/problems/course-schedule-ii/description/
'''
# DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)

        # !! what courses come after v
        for u, v in prerequisites:
            adjacency_list[v].append(u)

        indegree = [0] * numCourses
        for node in adjacency_list:
            for neighbor in adjacency_list[node]:
                indegree[neighbor] += 1

        # Add nodes with 0 in-degree to queue
        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        ordering = []
        while q:
            node = q.popleft()
            ordering.append(node)

            # Update in-degree and append
            for neighbor in adjacency_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    
        if len(ordering) == numCourses:
            return ordering
        # return empty if cycle
        return []




'''
GPT DUMPYARD
Both codes build the order by appending the course 
after all its prerequisites are done. But since they 
append at the end, the final order will have courses 
that depend on others appearing before their prereqs, 
so sometimes the order list may need to be reversed before 
returning (depending on problem requirements). Both codes 
don't reverse, but it depends on how the problem expects output.
'''


'''
Don't follow - 


Time - O(V + E)
- V = number of courses (nodes), E = number of prerequisite relations (edges)
- Each course is visited once in DFS
- Each edge is explored once during DFS traversal
- Memoization by clearing prereqs prevents repeated work on the same node

Space - O(V + E)
- Adjacency list `prereqs` stores all edges: O(V + E)
- Recursion stack can go as deep as O(V) in worst case
- `visited` set holds nodes in current recursion path: O(V)
- `order` list stores the topological order: O(V)
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Construct adjacency list
        prereqs = {i: [] for i in range(numCourses)}
        for sub, prevSub in prerequisites:
            prereqs[sub].append(prevSub)
        
        visited = set()
        order = []
        def dfs(course):
            # Circular dependency
            if course in visited:
                return False
            # Has no prereqs
            if prereqs[course] == []:
                if course not in order:  # Already added?
                    order.append(course)
                return True
            
            # Has prereqs
            visited.add(course)
            for prevSub in prereqs[course]:
                if not dfs(prevSub):
                    return False
            visited.remove(course)
            
            # All prereqs are doable
            prereqs[course] = []

            # Add subject
            order.append(course)
            return True

        for sub in range(numCourses):
            if not dfs(sub):
                return []
        return order

'''
Time - O(V + E)
- Each course (vertex) is visited once in DFS, so O(V)
- Each prerequisite (edge) is explored once during DFS, so O(E)
- Total time complexity is O(V + E)

Space - O(V + E)
- Adjacency list (prereqs) stores all edges, O(V + E)
- Call stack for DFS can go as deep as O(V) in worst case
- Sets `visited` and `visiting` store up to O(V) courses
- List `order` stores all courses, O(V)
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Construct adjacency list
        prereqs = {i: [] for i in range(numCourses)}
        for sub, prevSub in prerequisites:
            prereqs[sub].append(prevSub)
        
        visited = set()
        visiting = set()
        order = []
        def dfs(course):
            # Circular dependency of courses
            if course in visiting:
                return False
            # Prereqs have already been checked - can do
            if course in visited:
                return True
            
            # Clearing prereqs
            visiting.add(course)
            for prevSub in prereqs[course]:
                if not dfs(prevSub):
                    return False
            visiting.remove(course)
            
            # All prereqs are doable
            visited.add(course)

            # Add subject
            order.append(course)
            return True

        for sub in range(numCourses):
            if not dfs(sub):
                return []
        return order