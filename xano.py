def print_board(board):
    formatted_rows = []
    for row in board:
        # In each row, join the contents with a space and add it to the
        # formatted_rows list
        formatted_rows.append(" ".join(row))
    # Join all the rows togethr with a newline (which forms the grid)
    grid = "\n".join(formatted_rows)
    return grid


starting_board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

print(print_board(starting_board))
