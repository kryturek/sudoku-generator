import random
import copy
from sudoku_utils import is_valid, solve, count_solutions

def generate_sudoku():
    # Generate a complete Sudoku grid
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve(grid)
    return grid

def remove_numbers(grid, num_holes):
    # Remove 'num_holes' numbers from the Sudoku grid to create a puzzle
    puzzle = copy.deepcopy(grid)
    count = num_holes
    max_attempts = 200
    attempts = 0
    while count > 0 and attempts < max_attempts:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            removed = puzzle[row][col]
            puzzle[row][col] = 0
            if count_solutions(puzzle) == 1:
                count -= 1
            else:
                puzzle[row][col] = removed
        attempts += 1
    if count > 0:
        raise ValueError(f"Failed to remove {num_holes} numbers from the Sudoku grid.")
    return puzzle

def generate_puzzle(num_holes):
    # Generate a Sudoku puzzle with a unique solution
    grid = generate_sudoku()
    puzzle = remove_numbers(grid, num_holes)
    return puzzle