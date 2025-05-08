# sudoku_generator.py
import random
import copy
from initialize_board import initialize_board
from solve_sudoku import solve_sudoku_backtracking

def generate_sudoku(level='medium'):
    board = initialize_board()
    solve_sudoku_backtracking(board)
    solution = copy.deepcopy(board)

    level_map = {'easy': 40, 'medium': 30, 'hard': 20}
    clues = level_map.get(level, 30)
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)

    while len(cells) > clues:
        row, col = cells.pop()
        backup = board[row][col]
        board[row][col] = 0
        temp_board = copy.deepcopy(board)
        if not solve_sudoku_backtracking(temp_board):
            board[row][col] = backup

    return board, solution
