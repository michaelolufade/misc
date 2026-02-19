import os


class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0}

    def display_board(self, show_numbers=False):
        """Renders the board dynamically from the 2D list."""
        os.system('cls' if os.name == 'nt' else 'clear')  # Cross-platform clear
        print(f" Score: X: {self.scores['X']} | O: {self.scores['O']}\n")

        for r in range(3):
            row_display = []
            for c in range(3):
                if show_numbers and self.board[r][c] == " ":
                    row_display.append(str(r * 3 + c + 1))
                else:
                    row_display.append(self.board[r][c])

            print(f"  {row_display[0]}  |  {row_display[1]}  |  {row_display[2]}  ")
            if r < 2:
                print("-----|-----|-----")
        print()

    def check_win(self):
        b = self.board
        # Check rows, cols, and diagonals
        lines = [b[0], b[1], b[2]] + list([b[i][j] for i in range(3)] for j in range(3))
        # Add diagonals manually
        all_lines = lines + [[b[i][i] for i in range(3)], [b[i][2-i] for i in range(3)]]
        print(all_lines)
        # Check columns
        for col in range(3):
            all_lines.append([b[row][col] for row in range(3)])

        for line in all_lines:
            if line[0] == line[1] == line[2] != " ":
                return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def play_game(self):
        while True:
            self.board = [[" " for _ in range(3)] for _ in range(3)]
            self.current_player = "X"

            while True:
                self.display_board(show_numbers=True)
                try:
                    move = int(input(f"Player {self.current_player}, choose (1-9): ")) - 1
                    row, col = divmod(move, 3)

                    if move < 0 or move > 8 or self.board[row][col] != " ":
                        print("Invalid move! Try again.")
                        continue
                except ValueError:
                    print("Please enter a number.")
                    continue

                self.board[row][col] = self.current_player

                if self.check_win():
                    self.display_board()
                    print(f"🎉 Player {self.current_player} wins!")
                    self.scores[self.current_player] += 1
                    break

                if self.is_full():
                    self.display_board()
                    print("It's a draw!")
                    break

                self.current_player = "O" if self.current_player == "X" else "X"

            if input("Play again? (y/n): ").lower() != 'y':
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
