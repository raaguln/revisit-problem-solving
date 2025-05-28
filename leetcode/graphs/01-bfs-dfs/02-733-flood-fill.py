'''
https://leetcode.com/problems/flood-fill/


NOTE - WE DON'T NEED VISITED SET HERE CAUZ THE PIXELS ARE NOT REVISITED,
BECAUSE WE CHANGE THE COLOR AND OUR CONDITION WORKS LIKE THAT

Time - O(m * n)
- In the worst case, every pixel in the image may be visited once
- Each pixel is added to the queue and processed exactly once
- Constant-time operations per pixel (checking neighbors and color)

Space - O(m * n)
- The queue can hold up to O(m * n) elements in the worst case (entire image)
- No additional data structures apart from the queue and recursion stack
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]
        
        # No need to process if color is already the same
        if start_color == color:
            return image  
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            image[i][j] = color

            while queue:
                i, j = queue.popleft()
                for di, dj in directions:
                    r, c = i + di, j + dj
                    if (0 <= r < m and
                        0 <= c < n and
                        image[r][c] == start_color):
                        image[r][c] = color
                        queue.append((r, c))

        bfs(sr, sc)
        return image
