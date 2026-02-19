import sys


board = list(
    "       |       |\n"
    "       |       |    \n"
    "_______|_______|_______\n"
    "       |       |\n"
    "       |       |    \n"
    "_______|_______|_______\n"
    "       |       |\n"
    "       |       |    \n"
    "       |       |"
)


indexes = {
    1: [20, (0, 0)],
    2: [28, (0, 1)],
    3: [36, (0, 2)],
    4: [82, (1, 0)],
    5: [90, (1, 1)],
    6: [98, (1, 2)],
    7: [144, (2, 0)],
    8: [152, (2, 1)],
    9: [160, (2, 2)]
}

matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

tracker = set()

numbered_board = board.copy()
played_board = board.copy()

for i in indexes:
    numbered_board[indexes[i][0]] = str(i)


class Turn:
    def __init__(self):
        self.x = "X"
        self.o = "O"
        self.current = self.x
        self.count = 1

    def next(self):
        self.current = self.o if self.current == self.x else self.x
        self.count += 1

    def can_play(self):
        return self.count < 10


def insert(cell, value):
    board_pos, matrix_pos = indexes[cell]
    played_board[board_pos] = value
    r, c = matrix_pos
    matrix[r][c] = value
    return check_win(matrix)


def show_board(board):
    print("".join(board))


def clear_lines(n=1):
    sys.stdout.write("\033[A\033[K" * n)
    sys.stdout.flush()


def show_intro(x_score, o_score):
    show_board(numbered_board)
    print("Select a cell number to play your turn")
    print("Pick an empty cell numbered 1 - 9")
    print("Score: X - O")
    print(f"       {x_score} - {o_score}")
    input("Press ENTER to Start the Game.")


def check_win(matrix):
    # 1. Check Rows and Columns
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] != 0:
            return True
        if matrix[0][i] == matrix[1][i] == matrix[2][i] != 0:
            return True

    # 2. Check Diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != 0:
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != 0:
        return True

    return False


def tic_tac_toe(x_score, o_score):
    show_intro(x_score, o_score)
    tracker.clear()
    played_board[:] = board.copy()
    show_board(played_board)
    turn = Turn()
    winner = None
    matrix[:] = [[0 for _ in range(3)] for _ in range(3)]

    while turn.can_play():
        print(f"Turn {turn.count}: It is {turn.current}'s turn!")
        num = input("Enter a number: ")
        try:
            num = int(num)
            if num in tracker or num not in indexes:
                raise ValueError
        except ValueError:
            clear_lines(3)
            print("Invalid cell number")
            continue

        clear_lines(12)

        print(f"Turn {turn.count}: Player {turn.current} in cell {num}")
        is_game_won = insert(num, turn.current)
        show_board(played_board)
        tracker.add(num)

        if is_game_won:
            winner = turn.current
            break
        turn.next()

    if not winner:
        print("GAME OVER!")
        print("There is no winner. Would you like to play again?")
    else:
        if winner == turn.x:
            x_score += 1
        else:
            o_score += 1

        print(f"Player {winner} has won the game")
        print(f"Score is now: X({x_score}) - O({o_score})")

    replay = input('Press Y to play again, otherwise press any other key\n')
    if replay.upper() == "Y":
        tic_tac_toe(x_score, o_score)
    else:
        print("Thank you for playing. Please, See you later!.")
        sys.exit()


tic_tac_toe(0, 0)
