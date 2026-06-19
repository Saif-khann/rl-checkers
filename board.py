# The Checkers Board
# 0 = Empty
# 1 = Player 1's piece
# -1 = Player 2's piece
# 2 = Player 1's King
# -2 = Player 2's King

board = [
    [0, -1, 0, -1, 0, -1, 0, -1],
    [-1, 0, -1, 0, -1, 0, -1, 0],
    [0, -1, 0, -1, 0, -1, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [0, 0, 0, 0, 0, 0, 0, 0,],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
]

def print_board(board):
    print("  0  1  2  3  4  5  6  7")
    for row_index in range(8):
        print(row_index, end=" ")
        for col_index in range(8):
            piece = board[row_index][col_index]
            if piece == 0:
                print(" .", end=" ")
            elif piece == 1:
                print(" w", end=" ")
            elif piece == -1:
                print(" b", end=" ")
            elif piece == 2:
                print(" W", end=" ")
            elif piece == -2:
                print(" B", end=" ")
        print()

print_board(board)