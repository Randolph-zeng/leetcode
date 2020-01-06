'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
'''


# Naive and ugly impl, but works
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    table = {}
                    for k in range(9):
                        if board[i][k] != '.':
                            if board[i][k] in table:
                                return False
                            else:
                                table[board[i][k]] = 1
                    table = {}
                    for k in range(9):
                        if board[k][j] != '.':
                            if board[k][j] in table:
                                return False
                            else:
                                table[board[k][j]] = 1
        for k in range(3):
            for l in range(3):
                table = {}
                for i in range(3):
                    for j in range(3):
                        x = 3*l + j
                        y = 3*k + i
                        if board[x][y] != '.':
                            if board[x][y] in table:
                                return False
                            else:
                                table[board[x][y]] = 1
                        
        return True

# better, cleaner code 
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def validate(array):
            checker = {}
            lst = [elem for elem in array if elem != '.']
            return len(set(lst)) != len(lst)

        def get_elements(x,y):
            return [board[x+i][y+j] for i in range(3) for j in range(3)] 

        if any([validate(row) for row in board]):
            return False
        if any([validate(col) for col in zip(*board)]):
            return False
        if any([validate(get_elements(x,y)) for x in range(0,9,3) for y in range(0,9,3)]):
            return False
        return True


