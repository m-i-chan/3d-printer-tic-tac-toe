class Board():
    # -1 for player 1, 0 for empty, 1 for player 2

    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def mark_board(self,player,row,col):
        if self.board[row][col] != 0:
            return False
        self.board[row][col] = player
        return True

    def get_Winner(self):
        # Returns -1 if player 1 won, 0 if no winner, 1 for player 2
        for row in self.board: # Check rows
            sum = 0
            for col in self.board:
                sum += self.board[row][col]
            if sum == 3:
                return 1
            elif sum == -3:
                return -1

        for col in self.board: # Check columns
            sum = 0
            for row in self.board:
                sum += self.board[row][col]
            if sum == 3:
                return 1
            elif sum == -3:
                return -1

        # Check diagonals
        sum = self.board[1][1]
        sum += self.board[0][0]
        sum += self.board[2][2]
        if sum == 3:
            return 1
        elif sum == -3:
            return -1
        sum = self.board[1][1]
        sum += self.board[0][2]
        sum += self.board[2][0]
        if sum == 3:
            return 1
        elif sum == -3:
            return -1
        return 0
