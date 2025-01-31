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
        