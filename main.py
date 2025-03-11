from sudoku_generator import generate_puzzle

# Generate and print a Sudoku puzzle with a specified number of holes
num_holes = 50  # Adjust the number of holes based on desired difficulty
sudoku_puzzle = generate_puzzle(num_holes)
for row in sudoku_puzzle:
    print(row)