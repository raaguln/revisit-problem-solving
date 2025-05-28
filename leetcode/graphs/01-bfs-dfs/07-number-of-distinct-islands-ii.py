'''
https://leetcode.com/problems/number-of-distinct-islands-ii/description/

711. Number of Distinct Islands II

You are given an m x n binary matrix grid. An island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if they 
have the same shape, or have the same shape after rotation 
(90, 180, or 270 degrees only) or reflection (left/right 
direction or up/down direction).

Return the number of distinct islands.
'''
'''
BFS unoptimized
Time - O(m * n * log(m * n))
- BFS visits each cell at most once, total O(m * n) to find all islands
- Each island shape can contain up to O(m * n) cells in worst case (whole grid is one island)
- For each island, normalization generates 8 transformations, each sorted (sorting O(k log k), k = island size)
- In worst case, sorting dominates, so complexity per island is O(k log k)
- Total normalization cost summed over all islands ≤ O(m * n * log(m * n))
- Set insertions and comparisons depend on island count and shape size, but typically bounded by total cells

Space - O(m * n)
- Visited matrix uses O(m * n)
- BFS queue can hold up to O(m * n) cells in worst case
- Storing distinct island shapes in the set uses space proportional to the number and size of distinct islands, up to O(m * n)
- Temporary arrays for transformations use O(k) space per island shape
'''
from collections import deque
from typing import List, Tuple, Set

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(i: int, j: int) -> List[Tuple[int,int]]:
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            shape = []
            while queue:
                x, y = queue.popleft()
                shape.append((x - i, y - j))  # record relative position
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            return shape

        def normalize(shape: List[Tuple[int,int]]) -> Tuple[Tuple[int,int], ...]:
            # Generate all 8 transformations (rotations + reflections)
            transforms = [[] for _ in range(8)]
            for x, y in shape:
                transforms[0].append(( x,  y))  # identity
                transforms[1].append(( x, -y))  # reflection y
                transforms[2].append((-x,  y))  # reflection x
                transforms[3].append((-x, -y))  # rotation 180 or both reflections
                transforms[4].append(( y,  x))  # rotate 90
                transforms[5].append(( y, -x))  # rotate 90 + reflection y
                transforms[6].append((-y,  x))  # rotate 270 + reflection x
                transforms[7].append((-y, -x))  # rotate 270

            normalized_forms = []
            for t in transforms:
                t_sorted = sorted(t)
                # normalize by shifting to origin (subtract min x and min y)
                min_x = t_sorted[0][0]
                min_y = t_sorted[0][1]
                normalized = tuple((x - min_x, y - min_y) for x, y in t_sorted)
                normalized_forms.append(normalized)

            return min(normalized_forms)  # lex smallest as canonical form

        distinct_islands: Set[Tuple[Tuple[int,int], ...]] = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    shape = bfs(i, j)
                    canonical = normalize(shape)
                    distinct_islands.add(canonical)

        return len(distinct_islands)

'''
Optimized- 
- Keep the BFS approach but avoid repeatedly sorting all transformations 
for every shape by doing a single normalization pass per transformation.
- Use a faster data structure for storing and comparing shapes (like tuples).
- Possibly mark visited on the original grid itself to save space.
- Use a fixed set of transformations computed efficiently.

Time - O(m * n * log(m * n))
- BFS visits each cell once, total O(m * n) over the grid
- Each island can have up to O(m * n) cells in the worst case
- Normalization involves 8 transformations; each transformation sorts the island cells (O(k log k), k = island size)
- Summed over all islands, normalization dominates with O(m * n * log(m * n)) in worst case
- Set operations on canonical forms are efficient, bounded by number of distinct islands

Space - O(m * n)
- Visited matrix uses O(m * n)
- BFS queue can hold up to O(m * n) cells in worst case (single large island)
- The set of distinct islands stores canonical shapes, at most O(m * n) space
- Temporary storage during transformations uses O(k) space per island shape
'''
from collections import deque
from typing import List, Tuple, Set

class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = [[False]*n for _ in range(m)]

        def bfs(sr: int, sc: int) -> List[Tuple[int,int]]:
            queue = deque([(sr, sc)])
            visited[sr][sc] = True
            cells = []
            while queue:
                x, y = queue.popleft()
                cells.append((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
            return cells

        def normalize(cells: List[Tuple[int,int]]) -> Tuple[Tuple[int,int], ...]:
            shapes = []

            # Translate cells relative to origin (0,0)
            def transform(points, fn):
                return [fn(x, y) for x, y in points]

            def canonical(shape):
                # Shift shape to origin, sort and return tuple
                min_x = min(x for x, y in shape)
                min_y = min(y for x, y in shape)
                normalized = sorted((x - min_x, y - min_y) for x, y in shape)
                return tuple(normalized)

            points = cells

            # 8 transformations: 4 rotations and their reflections
            transformations = [
                lambda x, y: ( x,  y),   # identity
                lambda x, y: ( x, -y),   # reflection vertical
                lambda x, y: (-x,  y),   # reflection horizontal
                lambda x, y: (-x, -y),   # rotation 180
                lambda x, y: ( y,  x),   # rotation 90
                lambda x, y: ( y, -x),   # rotation 90 + reflection
                lambda x, y: (-y,  x),   # rotation 270 + reflection
                lambda x, y: (-y, -x),   # rotation 270
            ]

            for tf in transformations:
                transformed = transform(points, tf)
                shapes.append(canonical(transformed))

            return min(shapes)  # lex smallest

        distinct_islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    island_cells = bfs(i, j)
                    distinct_islands.add(normalize(island_cells))

        return len(distinct_islands)
