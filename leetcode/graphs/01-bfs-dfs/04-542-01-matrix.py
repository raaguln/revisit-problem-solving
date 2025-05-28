'''
https://leetcode.com/problems/01-matrix/description/

Simple BFS - TLE/MLE
Time - O((m * n)^2)
- For each cell with value 1, a BFS is done
- Each BFS can visit up to O(m * n) cells in the worst case
- There can be up to O(m * n) such BFS calls
- Total time complexity is O((m * n) * (m * n)) = O((m * n)^2)

Space - O(m * n)
- Each BFS uses a visited matrix of size m * n
- Queue can hold up to O(m * n) elements in worst case
- Result matrix stores distances for each cell
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        result = [[0 for i in range(n)] for j in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            # Visited is local because
            # each BFS starts from scratch
            visited = set((i, j))
            queue = deque([(i, j, 0)])

            while queue:
                # Process queue
                x, y, distance = queue.popleft()

                if mat[x][y] == 0:
                    return distance

                # Update queue
                for di, dj in directions:
                    r, c = x + di, y + dj
                    if (
                        0 <= r < m and
                        0 <= c < n
                    ):
                        queue.append((r, c, distance + 1))
                        visited.add((r, c))
            return 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    result[i][j] = bfs(i, j)
        return result


'''
Multi source BFS
Time - O(m * n)
- Each cell is enqueued and processed at most once
- BFS explores each cell's neighbors in constant time
- Total time proportional to number of cells in the matrix

Space - O(m * n)
- The `result` matrix stores distance for each cell
- The queue can hold up to O(m * n) elements in the worst case
- Additional space for directions and variables is constant

'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Multi-source BFS
        m, n = len(mat), len(mat[0])
        # To help track visited (-1 -> not visited)
        result = [[-1 for i in range(n)] for j in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque()

        # Start BFS from all 0s
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    result[i][j] = 0

        # From there, update all cells that are not -1
        while queue:
            i, j = queue.popleft()

            # Add to queue
            for di, dj in directions:
                r, c = i + di, j + dj
                # If not visited, update distance
                if (
                    0 <= r < m and
                    0 <= c < n and
                    result[r][c] == -1
                ):
                    queue.append((r, c))
                    # 1 + distance of where it came from
                    result[r][c] = 1 + result[i][j]
        return result
