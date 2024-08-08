# Connect Four Game in Python

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
EMPTY = "."
PLAYER1 = "X"
PLAYER2 = "O"

def create_board():
    """Create an empty Connect Four board."""
    return [[EMPTY for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]

def print_board(board):
    """Print the Connect Four board."""
    for row in board:
        print(" ".join(row))
    print(" ".join(map(str, range(COLUMN_COUNT))))

def drop_piece(board, column, piece):
    """Drop a piece into the chosen column."""
    for row in reversed(board):
        if row[column] == EMPTY:
            row[column] = piece
            return True
    return False

def is_winning_move(board, piece):
    """Check if the last move was a winning move."""
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            if board[row][col] == piece:
                if check_direction(board, row, col, piece, 1, 0) or \
                   check_direction(board, row, col, piece, 0, 1) or \
                   check_direction(board, row, col, piece, 1, 1) or \
                   check_direction(board, row, col, piece, 1, -1):
                    return True
    return False

def check_direction(board, row, col, piece, row_step, col_step):
    """Check if there are 4 pieces in a row in a given direction."""
    count = 0
    for i in range(4):
        r = row + i * row_step
        c = col + i * col_step
        if 0 <= r < ROW_COUNT and 0 <= c < COLUMN_COUNT and board[r][c] == piece:
            count += 1
        else:
            break
    return count == 4

def is_full(board):
    """Check if the board is full."""
    return all(board[0][col] != EMPTY for col in range(COLUMN_COUNT))

def main():
    """Main game loop."""
    board = create_board()
    current_player = PLAYER1

    while True:
        print_board(board)
        try:
            column = int(input(f"Player {current_player}'s turn. Choose a column (0-{COLUMN_COUNT-1}): "))
            if column < 0 or column >= COLUMN_COUNT:
                raise ValueError("Invalid column number.")
        except ValueError as e:
            print(e)
            continue

        if drop_piece(board, column, current_player):
            if is_winning_move(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1
        else:
            print("Column is full. Try another column.")

if __name__ == "__main__":
    main()
