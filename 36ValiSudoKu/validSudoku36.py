def isValidSudoku(board):
    # Create 9 sets for rows, columns, and boxes to track seen numbers
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    box_sets = [set() for _ in range(9)]

    # Iterate over each cell in the 9x9 board
    for row in range(9):
        for col in range(9):
            num = board[row][col]

            # Skip empty cells ('.')
            if num == ".":
                continue

            # Compute the index of the 3x3 box the current cell belongs to
            box_index = (row // 3) * 3 + (col // 3)

            # Check for duplicates:
            # If the number already exists in the corresponding row, column, or box → invalid Sudoku
            if (num in row_sets[row] or
                num in col_sets[col] or
                num in box_sets[box_index]):
                return False

            # No duplicate → add the number to the corresponding row, column, and box sets
            row_sets[row].add(num)
            col_sets[col].add(num)
            box_sets[box_index].add(num)

    # If no duplicates were found, the board is valid
    return True
