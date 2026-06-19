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

def count_pieces(board):
    player1_pieces = 0
    player1_kings = 0
    player2_pieces = 0
    player2_kings = 0

    for row_index in range(8):
        for col_index in range(8):
            piece = board[row_index][col_index]
            if piece == 1:
                player1_pieces += 1
            elif piece == -1:
                player2_pieces += 1
            elif piece == 2:
                player1_kings += 1
            elif piece == -2:
                player2_kings += 1

    return player1_pieces, player1_kings, player2_pieces, player2_kings


p1, p1k, p2, p2k = count_pieces(board)
print(f"Player 1 — pieces: {p1}, kings: {p1k}")
print(f"Player 2 — pieces: {p2}, kings: {p2k}")

def is_valid_square(row, col):
    if row < 0 or row > 7:
        return False
    if col < 0 or col > 7:
        return False
    if (row + col) % 2 == 0:
        return False
    return True


print(is_valid_square(0, 1))  # True  — dark square, inside board
print(is_valid_square(0, 0))  # False — light square
print(is_valid_square(9, 3))  # False — outside board
print(is_valid_square(3, 8))  # False — outside board