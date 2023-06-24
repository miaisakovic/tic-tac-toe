class GameLogic:
    def __init__(self):
        computer_player = ["X", "red"]
        human_player = ["O", "white"]
        self.players = [computer_player, human_player]
        self.current_player = self.players[0]
        self.num_turns = 0
        self.game_map = [['', '', ''], ['', '', ''], ['', '', '']]

    def get_type(self):
        return self.current_player[0]

    def get_colour(self):
        return self.current_player[1]

    def update_game(self, row, col):
        self.num_turns += 1
        self.game_map[row][col] = self.current_player[0]

    def winner(self):
        # All three squares in a row match
        for row in range(3):
            if (
                len(set(self.game_map[row])) == 1 and
                self.game_map[row][0] != ''
               ):
                return True

        #  All three squares in a column match
        for col in range(3):
            if (
                self.game_map[0][col] == self.game_map[1][col] ==
                    self.game_map[2][col] and
                    self.game_map[0][col] != ''
               ):
                return True

        # All three squares in a diagonal line match
        if (
            self.game_map[0][0] == self.game_map[1][1] ==
                self.game_map[2][2] and
                self.game_map[0][0] != ''
           ) or (
            self.game_map[0][2] == self.game_map[1][1] ==
                self.game_map[2][0] and
                self.game_map[0][2] != ''
           ):
            return True

        return False

    def tie(self):
        no_winner = not self.winner()
        return no_winner and self.num_turns == 9

    def change_player(self):
        if self.current_player[0] == 'X':
            self.current_player = self.players[1]
            return None, None
        else:
            self.current_player = self.players[0]
            row, col = self.get_best_move()
            return row, col

    def get_best_move(self):
        best_score = float('-inf')
        best_move_row = None
        best_move_col = None

        for row in range(3):
            for col in range(3):
                if self.game_map[row][col] == '':
                    self.game_map[row][col] = 'X'
                    score = self.minimax(False)
                    self.game_map[row][col] = ''
                    if score > best_score:
                        best_score = score
                        best_move_row = row
                        best_move_col = col

        return best_move_row, best_move_col

    def minimax(self, maximizing_player):
        if self.winner():
            # Check if the previous player won
            if maximizing_player:
                return -1
            else:
                return 1

        if self.tie():
            return 0

        if maximizing_player:
            max_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if self.game_map[row][col] == '':
                        self.game_map[row][col] = 'X'
                        score = self.minimax(False)
                        self.game_map[row][col] = ''
                        max_score = max(max_score, score)
            return max_score
        else:
            min_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.game_map[row][col] == '':
                        self.game_map[row][col] = 'O'
                        score = self.minimax(True)
                        self.game_map[row][col] = ''
                        min_score = min(min_score, score)
            return min_score
