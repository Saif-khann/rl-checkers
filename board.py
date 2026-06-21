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

def get_valid_moves(board, row, col):
    moves = []
    piece = board[row][col]

    if piece == 0:
        return moves

    if piece == 1:
        directions = [(-1, -1), (-1, 1)]
    elif piece == -1:
        directions = [(1, -1), (1, 1)]
    else:
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for direction in directions:
        row_step = direction[0]
        col_step = direction[1]

        next_row = row + row_step
        next_col = col + col_step

        if is_valid_square(next_row, next_col):
            if board[next_row][next_col] == 0:
                moves.append((next_row, next_col))
            elif board[next_row][next_col] * piece < 0:
                jump_row = next_row + row_step
                jump_col = next_col + col_step
                if is_valid_square(jump_row, jump_col):
                    if board[jump_row][jump_col] == 0:
                        moves.append((jump_row, jump_col))

    return moves


print(get_valid_moves(board, 5, 0))
print(get_valid_moves(board, 5, 2))