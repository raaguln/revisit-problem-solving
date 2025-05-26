'''
TLE
Time - O(m^3)
- Let m be the number of cuts + 2 (including 0 and n)
- There are O(m^2) subproblems defined by (left, right) indices
- For each subproblem, we try O(m) possible intermediate cuts
- Total time complexity: O(m^3)

Space - O(m^2)
- Recursive call stack depth is O(m) in the worst case
- No memoization used here, so no DP table, but call stack and parameters dominate
- Each call uses constant extra space aside from recursion stack
- Overall space dominated by recursion depth: O(m)
'''
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Add the edges 0 and n to cuts to simplify boundary handling
        cuts = [0] + sorted(cuts) + [n]

        def dfs(left, right):
            # If no cuts between left and right, cost is zero
            if right - left <= 1:
                return 0

            min_cost = float('inf')
            # Try every possible cut between left and right
            for i in range(left + 1, right):
                cost = cuts[right] - cuts[left]  # cost of cutting the current stick
                cost += dfs(left, i) + dfs(i, right)  # cost of subproblems
                min_cost = min(min_cost, cost)

            return min_cost

        # Compute minimum cost between the first and last cut
        return dfs(0, len(cuts) - 1)


'''
ALSO TLE
Bottom Up Optimized

Time - O(m^3)  
- There are O(m^2) subproblems for pairs (left, right) where m = number of cuts + 2  
- For each subproblem, iterate through all possible mid cuts between left and right → O(m)  
- Total complexity: O(m^3)

Space - O(m^2)  
- A 2D DP table of size m x m stores minimum costs for cutting between cuts[left] and cuts[right]  
- No recursion stack used

Explanation -  
n - length of the stick  
cuts - sorted list of cut positions with 0 and n added at ends  
dp[i][j] - minimum cost to cut the stick between cuts[i] and cuts[j]  

DP logic -  
QUESTION -> What is the minimum cost to cut the stick between cuts[i] and cuts[j]?  

1. Base case:  
   - If no cuts between i and j (i.e., j == i+1), dp[i][j] = 0 (no cost)  
2. For subproblems with length ≥ 2 (meaning at least one cut between i and j):  
   - Try all possible mid cuts k between i and j  
   - Cost = length of current stick segment (cuts[j] - cuts[i]) + dp[i][k] + dp[k][j]  
   - dp[i][j] = minimum of all such costs over all valid k

Answer -  
- dp[0][m-1] stores the minimum cost to cut the entire stick from 0 to n

Table - Step 0 after initialization:  

cuts = [0, 1, 3, 4, 5]  (example cuts and stick length n=5)  
dp (m=5) initialized with zeros on the diagonal and elsewhere:

     0    1    2    3    4  
0 |  0    0    0    0    0  
1 |       0    0    0    0  
2 |            0    0    0  
3 |                 0    0  
4 |                      0  

After filling dp for increasing length intervals, dp[0][4] contains minimum cost to cut entire stick.

'''
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)
        
        # dp[i][j] = minimum cost to cut the stick between cuts[i] and cuts[j]
        dp = [[0] * m for _ in range(m)]
        
        # Iterate over the length of the interval between cuts
        for length in range(2, m):  # length is at least 2 because at least one cut between
            for left in range(m - length):
                right = left + length
                min_cost = float('inf')
                # Try all possible cuts between left and right
                for mid in range(left + 1, right):
                    cost = cuts[right] - cuts[left] + dp[left][mid] + dp[mid][right]
                    if cost < min_cost:
                        min_cost = cost
                dp[left][right] = min_cost if min_cost != float('inf') else 0
        
        return dp[0][m - 1]
