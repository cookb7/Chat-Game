# Author: Brendan Cook
# Date: 06/08/2023
# Description: Defines the class for the connect 4 game.


class connectFour:
    """Defines a class for the game Connect 4"""
    def __init__(self):
        self._board = [[" "] * 7 for _ in range(5)]
        self._numMoves = 0

    def setBoard(self, board, numMoves):
        """Updates the board to match the other player's board."""
        self._board = board
        self._numMoves = numMoves

    def getBoard(self):
        """Returns the board and number of moves."""
        return self._board, self._numMoves
    

    def display(self):
        """Print out the current board"""
        for row in range(len(self._board)):
            if row> 0:
                print('|')
            for space in self._board[row]:
                print('|', space, end='')
        
        print('|')
        print('--------------------------')

    def xMove(self):
        """Defines the characteristics of a player adding a blue peice to the board
        and updates the board. Then calls display to show the new board."""
        columns = [0, 1, 2, 3, 4, 5, 6]
        while True:
            print("Your move, enter a column number 0 through 6 > ", end="")
            column = input()
            if column.isdigit():
                column = int(column)
            elif column == '/q':
                return '/q'
            else:
                print("Please enter a valid column number!")
                continue
            if column not in columns:
                print("Please enter a valid column number!")
                continue
            else:
                break

        if self._board[0][column] != " ":
            return "bad move"
        
        num_rows = len(self._board)
        for row in range(num_rows):
            if self._board[row][column] == " " and row < num_rows - 1:
                continue
            elif self._board[row][column] == " " and row == num_rows - 1:
                self._board[row][column] = 'X'
            else:
                self._board[row - 1][column] = 'X'

        self._numMoves += 1
        if self._numMoves > 6:
            win = self.checkWin("X")
            if win:
                self.display()
                print("X wins")
                return "win"
            else:
                self.display()
        else:
            self.display()
        return "continue"

    def oMove(self):
        """Defines the characteristics of a player adding a red peice to the board
        and updates the board. Then calls display to show the new board."""
        columns = [0, 1, 2, 3, 4, 5, 6]
        while True:
            print("Your move, enter a column number 0 through 6 > ", end="")
            column = input()
            if column.isdigit():
                column = int(column)
            elif column == '/q':
                return '/q'
            else:
                print("Please enter a valid column number!")
                continue
            if column not in columns:
                print("Please enter a valid column number!")
                continue
            else:
                break

        if self._board[0][column] != " ":
            return "bad move"
        
        num_rows = len(self._board)
        for row in range(num_rows):
            if self._board[row][column] == " " and row < num_rows - 1:
                continue
            elif self._board[row][column] == " " and row == num_rows - 1:
                self._board[row][column] = 'O'
            else:
                self._board[row - 1][column] = 'O'

        self._numMoves += 1
        if self._numMoves > 6:
            win = self.checkWin("O")
            if win:
                self.display()
                print("O wins")
                return "win"
            else:
                self.display()
        else:
            self.display()
        return "continue"

    def checkWin(self, char):
        """Checks to see if a player has won after 7 moves"""
        # Check rows
        for row in range(len(self._board)):
            for column in range(len(self._board[0]) - 3):
                if self._board[row][column] == char and self._board[row][column+1] == char \
                        and self._board[row][column+2] == char and self._board[row][column+3] == char:
                    return True
                
        # Check columns
        for row in range(len(self._board) - 3):
            for column in range(len(self._board[0])):
                if self._board[row][column] == char and self._board[row+1][column] == char \
                        and self._board[row+2][column] == char and self._board[row+3][column] == char:
                    return True
                
        # Check diagonals (positive slope)
        for row in range(len(self._board) - 3):
            for col in range(len(self._board[0]) - 3):
                if self._board[row][col] == char and self._board[row+1][col+1] == char \
                        and self._board[row+2][col+2] == char and self._board[row+3][col+3] == char:
                    return True

        # Check diagonals (negative slope)
        for row in range(len(self._board) - 3):
            for col in range(3, len(self._board[0])):
                if self._board[row][col] == char and self._board[row+1][col-1] == char \
                        and self._board[row+2][col-2] == char and self._board[row+3][col-3] == char:
                    return True
        
    def welcome(self):
        """Prints welcome message and rules"""
        message = "Welcome to Connect 4. Enter the column number you would like to drop a peice into.\nThe first player to connect 4 peices in a row, column or diagonally wins! Type /q to quit. Good Luck!"
        print(message)


