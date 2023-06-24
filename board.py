from game_logic import GameLogic
import tkinter as tk


class Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-tac-toe")
        self.status = tk.Label(self, text="Can you beat Player X?",
                               font=("Monaco 15"))
        self.board = [[], [], []]
        self.game = GameLogic()
        self.__create_board()
        self.__start_game()

    def __create_board(self):
        for col in range(3):
            self.grid_columnconfigure(col, weight=1)
        for row in range(3):
            self.grid_rowconfigure(row, weight=1)

        grid_frame = tk.Frame(master=self)
        grid_frame.pack()

        for row in range(3):
            for col in range(3):
                button = tk.Button(master=grid_frame,
                                   highlightbackground="#24C0D6",
                                   compound="center", width=4, height=2,
                                   text="", font=("Helvetica 50 bold"),
                                   command=lambda row=row, col=col: self.__click(row, col))
                self.board[row].append(button)
                button.grid(row=row, column=col, sticky='nesw')

        self.status.pack()

    def __start_game(self):
        row, col = self.game.get_best_move()
        self.__click(row, col)

    def __click(self, row, col):
        button = self.board[row][col]

        # Ensure the button has not been previously clicked
        if button["state"] == "normal":
            button["disabledforeground"] = self.game.get_colour()
            button["text"] = self.game.get_type()

            self.game.update_game(row, col)

            if self.game.winner():
                self.status["text"] = "Player " + self.game.get_type() + " wins!"
                for row in range(3):
                    for col in range(3):
                        self.board[row][col]["state"] = "disabled"

            elif self.game.tie():
                self.status["text"] = "It's a tie!"

            else:
                row, col = self.game.change_player()
                # If row and column numbers were given, the computer plays next
                if row is not None:
                    self.__click(row, col)

            self.status.pack()

            button["state"] = "disabled"
