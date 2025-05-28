# https://leetcode.com/problems/number-of-provinces/
'''
1. DFS

Time - O(V^2)
- There are V cities (nodes)
- For each city, DFS potentially checks all other V cities (neighbors) due to the adjacency matrix
- Each cell in the matrix is effectively visited once or twice during the entire process
- Overall time complexity is O(V^2)

Space - O(V)
- The `visited` set stores up to V cities
- Recursion stack depth can be up to O(V) in the worst case (e.g., a fully connected graph)
- Input adjacency matrix uses O(V^2) space but is given as input (not counted towards algorithm's auxiliary space)

'''
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            for neighbor in range(cities):
                if isConnected[city][neighbor] != 0 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    
        # Do DFS from each city
        for i in range(cities):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces += 1
        
        return provinces

'''
2. Disjoint Union Set (by rank)

findCircleNum (Union-Find / Disjoint Set approach to count connected components)

Time - O(V^2 * α(V))
- There are V cities, and the adjacency matrix has V^2 entries
- For each pair (i, j), we attempt a union operation if connected
- Union-Find operations (find and union) run in nearly O(1) amortized time, specifically O(α(V)), where α is the inverse Ackermann function (very slow growing, practically constant)
- Total time dominated by iterating over the adjacency matrix: O(V^2)
- Union-Find operations add a very small overhead per union/find

Space - O(V)
- `parent` and `rank` arrays store data for each city: O(V)
- `visited` set is not used here (unlike DFS)
- Recursion stack is not used (iterative Union-Find)
- Auxiliary space is minimal compared to adjacency matrix input


This Union-Find method is often faster in practice than DFS on 
adjacency matrices because it avoids repeated recursive calls 
and efficiently merges sets, though time complexity still depends
 on scanning the full matrix. It uses less auxiliary space and
  typically performs better for large inputs.
'''