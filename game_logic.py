class GameLogic:
    '''
    A GameLogic object contains the game rules of Tic-tac-toe and 
    the minimax algorithm for the AI player

    Attributes:
        players: A list of two lists containing the player's mark and its colour
        current_player: A string that specifies whether the current player is X or O
        num_turns: An integer for the number of turns that were taken so far
        game_map: A 3x3 2D list that contains the current state of the game board
    '''
    def __init__(self):
        computer_player = ["X", "red"]
        human_player = ["O", "white"]
        self.players = [computer_player, human_player]
        self.current_player = self.players[0]
        self.num_turns = 0
        self.game_map = [['', '', ''], ['', '', ''], ['', '', '']]

    def get_type(self):
        '''
        Returns:
            A string specifying whether the current player is X or O
        '''
        return self.current_player[0]

    def get_colour(self):
        '''
        Returns:
            A string specifying the colour of the current player's mark
        '''
        return self.current_player[1]

    def update_game(self, row, col):
        '''
        After a player has decided where to place their mark, update num_turns 
        and game_map to convey the board's state 

        Args:
            row: An integer that specifies which row the new mark is on 
            col: An integer that specifies which column the new mark is on 
        '''
        self.num_turns += 1
        self.game_map[row][col] = self.current_player[0]

    def winner(self):
        '''
        Check if a player won the game

        Returns:
            True if there are three identical marks in a row, column or diagonal, 
            and False otherwise
        '''
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
        '''
        Check if the game ended in a tie

        Returns:
            True if there is a tie, and False otherwise
        '''
        no_winner = not self.winner()
        return no_winner and self.num_turns == 9

    def change_player(self):
        '''
        Changes the current player 

        Returns:
            Integers for the row and column of the AI player's next move. 
            Otherwise, if the current player is not AI, None is returned.  
        '''
        if self.current_player[0] == 'X':
            self.current_player = self.players[1]
            return None, None
        else:
            self.current_player = self.players[0]
            row, col = self.get_best_move()
            return row, col

    def get_best_move(self):
        '''
        Obtains the AI player's best move 

        Returns:
            The row and column numbers of the most optimal place to put an 'X'
            on the board
        '''
        best_score = float('-inf')
        best_move_row = None
        best_move_col = None

        for row in range(3):
            for col in range(3):
                if self.game_map[row][col] == '':
                    self.game_map[row][col] = 'X'
                    score = self.__minimax(False)
                    self.game_map[row][col] = ''
                    if score > best_score:
                        best_score = score
                        best_move_row = row
                        best_move_col = col

        return best_move_row, best_move_col

    def __minimax(self, maximizing_player):
        '''
        The Minimax algorithm where the AI player is the maximizer and 
        the human player is the minimizer. 

        Args:
            maximizing_player: True if the player is the AI and 
            False otherwise
        
        Returns:
            Given the board's configuration, it returns the maximum score 
            possible if the current player is the AI. 
            Otherwise, it returns the minimum score possible. 
        '''
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
                        score = self.__minimax(False)
                        self.game_map[row][col] = ''
                        max_score = max(max_score, score)
            return max_score
        else:
            min_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if self.game_map[row][col] == '':
                        self.game_map[row][col] = 'O'
                        score = self.__minimax(True)
                        self.game_map[row][col] = ''
                        min_score = min(min_score, score)
            return min_score
