# https://leetcode.com/problems/number-of-provinces/
'''
Time: O(N^2)
Space: O(N)
'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        Start with 0, form province, mark all cities in province visited.
        Check if 1 is visited or not
        - if visited, skip
        - if not, form a province
        Repeat
        '''
        cities = len(isConnected)
        visited = [False] * cities
        def dfs(u):
            visited[u] = True
            for v in range(cities):
                if isConnected[u][v] and not visited[v]:
                    dfs(v)
        
        count = 0
        for i in range(cities):
            if not visited[i]:
                dfs(i)
                count += 1 
        return count
