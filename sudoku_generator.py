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
    while count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            count -= 1
    return puzzle

def generate_puzzle(num_holes):
    # Generate a Sudoku puzzle with a unique solution
    grid = generate_sudoku()
    puzzle = remove_numbers(grid, num_holes)
    
    while count_solutions(puzzle) != 1:
        puzzle = remove_numbers(grid, num_holes)
    
    return puzzle