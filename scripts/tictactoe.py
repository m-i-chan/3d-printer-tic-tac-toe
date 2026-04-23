"""
tictactoe.py

Contains board and game class for tic-tac-toe.

"""

class Board():
    # -1 for player 1, 0 for empty, 1 for player 2
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def mark_board(self,player,row,col):
        # Checks if board is empty then marks board.
        if self.board[row][col] != 0:
            raise ValueError("Space occupied")
        self.board[row][col] = player

    def get_Winner(self):
        # Returns -1 if player 1 won, 0 if no winner, 1 for player 2
        for row in self.board: # Check rows
            sum = 0
            for col in row:
                sum += col
            if sum == 3:
                return 1
            if sum == -3:
                return -1

        for x in range(3): # Check columns
            sum = 0
            for y in range(3):
                sum += self.board[y][x]
            if sum == 3:
                return 1
            if sum == -3:
                return -1

        # Check diagonals
        sum = self.board[1][1]
        sum += self.board[0][0]
        sum += self.board[2][2]
        if sum == 3:
            return 1
        if sum == -3:
            return -1
        sum = self.board[1][1]
        sum += self.board[0][2]
        sum += self.board[2][0]
        if sum == 3:
            return 1
        if sum == -3:
            return -1
        return 0
    
    def clear_board(self):
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
    
    def is_full(self):
        for row in self.board:
            for col in row:
                if col == 0:
                    return False
        return True
    
    def __str__(self):
        out = ""
        for row in self.board:
            row_list = []
            for col in row:
                if col == -1: 
                    row_list.append("x")
                elif col == 1: 
                    row_list.append("o")
                else:
                    row_list.append(" ")
            out += str(row_list) + "\n"
        return out

class Game():
    def __init__(self):
        self.board = Board()
        self.player = -1
        self.winner = 0
    
    def next_player(self):
        self.player *= -1
    
    def turn(self, row, col):
        if self.winner == 0:
            self.board.mark_board(self.player, row, col)
        else:
            raise Exception(f'Game over, {self.winner} won.')
        self.winner = self.board.get_Winner()
        self.next_player()
    
    def new_game(self):
        self.board.clear_board()
        self.player = -1
        self.winner = 0
    
    def terminal_game(self):
        # Intended to run a game in terminal.
        game_on = True
        while game_on:
            print(f'Player {"1" if self.player == -1 else "2"}, enter your move.')
            response = input().split(",")
            try:
                self.turn(int(response[0]),int(response[1]))        
            except ValueError:
                print("Space occupied.")
            winner = self.board.get_Winner()
            if winner == -1:
                game_on = not game_on
                print('Player 1 wins!')
            elif winner == 1:
                game_on = not game_on
                print('Player 2 wins!')
            if self.board.is_full():
                game_on = not game_on
                print("Tie game")
            print(self.board)