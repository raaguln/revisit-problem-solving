# Attempt 1 - wrong for one test case
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                # Check row
                if j+1 < 9 and board[i][j] in board[i][j+1:]:
                    return False
                # Check column
                if board[i][j] in board[i:9][j]:
                    return False
                # Check squares
                if j % 3 == 0:
                    a = i // 3
                    new_board = filter(board[a:a+2][a:a+2], lambda x: x != ".")
                    if len(new_board) != len(set(new_board)):
                        return False
        return True

# Attempts 2-n - lots of syntax and logic mistakes
'''
A> Checking squares -
0. code for slicing 2d chunk from 2d list was super bad (was trying like in pandas df,
   but lists don't work like that)
1. if `j % 3 == 0:` -> was a bad logic, it needed to check everytime
2. using only a was wrong, had to do both i // 3 and j // 3 individually
3. filter code was also wrong, comparing string with list
B> Checking column -
1. slicing was wrong
2. needed to do i+1 instead of slicing from i itself (it was the same logic as rows -_-)
'''

# Atttempt n - beats more than 90% in performance!
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                # Check row
                if j+1 < 9 and board[i][j] in board[i][j+1:]:
                    return False
                # Check column
                if i+1 < 9 and board[i][j] in [row[j] for row in board[i+1:]]:
                    return False
                # Check squares
                a = i // 3
                b = j // 3
                square = []
                for row in board[a*3:a*3+3]:
                    for digit in row[b*3:b*3+3]:
                        if digit != '.':
                            square.append(digit)
                if len(square) != len(set(square)):
                    return False
        return True