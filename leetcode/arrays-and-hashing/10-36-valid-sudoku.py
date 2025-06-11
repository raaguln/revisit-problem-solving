# 
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        validator = {}
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == '.':
                    continue
                key = f'row{i}'
                validator.setdefault(key, []).append(board[i][j])
                key = f'col{j}'
                validator.setdefault(key, []).append(board[i][j])
                key = f'box{(int(i//3), int(j//3))}'
                validator.setdefault(key, []).append(board[i][j])
        for numbers in validator.values():
            if len(numbers) != len(set(numbers)):
                return False
        return True

# More optimal
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 sub-boxes

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                # Compute index of 3x3 box
                box_index = (r // 3) * 3 + (c // 3)

                if (val in rows[r] or
                    val in cols[c] or
                    val in boxes[box_index]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True