import random

def is_valid(grid, row, col, num):
    # Check if 'num' is not in the given row
    if num in grid[row]:
        return False
    # Check if 'num' is not in the given column
    if num in [grid[i][col] for i in range(9)]:
        return False
    # Check if 'num' is not in the 3x3 block
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def solve(grid):
    # Try to solve the Sudoku grid using backtracking
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                # Shuffle numbers to add randomness to the solution
                random_nums = list(range(1, 10))
                random.shuffle(random_nums)
                for num in random_nums:
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def count_solutions(grid):
    # Count the number of possible solutions for the Sudoku grid
    solutions = [0]
    
    def solve_and_count(grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(grid, row, col, num):
                            grid[row][col] = num
                            solve_and_count(grid)
                            grid[row][col] = 0
                    return
        solutions[0] += 1
    
    solve_and_count(grid)
    return solutions[0]