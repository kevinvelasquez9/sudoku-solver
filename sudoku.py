board = [
    [0, 0, 0, 6, 0, 9, 0, 8, 0],
    [0, 0, 0, 0, 3, 0, 7, 0, 0],
    [0, 1, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 8, 0, 6, 0, 0, 0, 5],
    [4, 2, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 9, 0, 5, 0, 7],
    [7, 0, 0, 0, 0, 8, 0, 0, 6],
    [1, 0, 0, 0, 0, 3, 0, 0, 0]
]

# Prints a board in a nice format
def print_board(board):
    print()
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')
    print()

# Finds the next available spot
def next_spot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

# Checks if number is valid
def is_valid(board, number, pos):
    row = pos[0]
    col = pos[1]

    # First, check row
    for j in range(len(board[0])):
        if board[row][j] == number and j != col:
            return False
    # Then, check col
    for i in range(len(board)):
        if board[i][col] == number and i != row:
            return False
    # Lastly, check 3x3 square
    squareX = col // 3
    squareY = row // 3
    for i in range(squareY * 3, squareY * 3 + 3):
        for j in range(squareX * 3, squareX * 3 + 3):
            if board[i][j] == number and (i, j) != pos:
                return False
    return True

# Main solver function
def main(board):
    spot = next_spot(board)
    # If no available spot, algorithm is done
    if not spot:
        return True
    # Otherwise, we continue
    else:
        row, col = spot
    # Iterate through every possible number
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            # Repeat the process
            if main(board):
                return True
            # If a spot is invalid, we backtrack
            board[row][col] = 0
    return False
import time
start_time = time.time()
print('Initial board.')
print_board(board)
main(board)
print('Solved board.')
print_board(board)
print("--- %s seconds ---" % (time.time() - start_time))
