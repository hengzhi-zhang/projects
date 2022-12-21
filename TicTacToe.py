# File: Project2.py
# Student: Hengzhi Zhang
# UT EID: hz69894
# Course Name: CS303E
#
# Date: 11/09/2022
# Description of Program: Basic Tic-Tac Toe game which allows a human player to play against the computer.

import random

# Some global constants:

HUMAN = 0
MACHINE = 1

# Probably some other constants here:

WELCOME = "Welcome to our Tic-Tac-Toe game! \n Please begin playing."

YOU_WON = "Congratulations! You won!"

YOU_LOST = "Sorry! You lost!"

YOU_TIED = "Looks like a tie. Better luck next time!"


initialBoard = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]

gameBoard = initialBoard


# Auxiliary functions here:


class TicTacToe:
    def __init__(self):

        self.__board = initialBoard
        self.__Player = HUMAN

    def __str__(self):
        return str(initialBoard[0]) + "\n" + str(initialBoard[1]) + "\n" + str(initialBoard[2])

    def getPlayer(self):

        return self.__Player

    def isWin(self):

    # See if the board represents a win for the current
    # player. A win is three of the current player's tokens
    # in a single row, column, or either diagonal.
        if gameBoard[0][0] == "X" and gameBoard[1][0] == "X" and gameBoard[2][0] == "X":
            return True
        if gameBoard[0][0] == "X" and gameBoard[0][1] == "X" and gameBoard[0][2] == "X":
            return True
        if gameBoard[1][0] == "X" and gameBoard[1][1] == "X" and gameBoard[1][2] == "X":
            return True
        if gameBoard[2][0] == "X" and gameBoard[2][1] == "X" and gameBoard[2][2] == "X":
            return True
        if gameBoard[0][2] == "X" and gameBoard[1][2] == "X" and gameBoard[2][2] == "X":
            return True
        if gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] == "X":
            return True
        if gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] == "X":
            return True
        if gameBoard[0][1] == "X" and gameBoard[1][1] == "X" and gameBoard[2][1] == "X":
            return True
        return False

    def swapPlayers(self):

        if self.__Player == HUMAN:
            self.__Player = MACHINE
        else:
            self.__Player = HUMAN

    def humanMove(self):

    # Ask the HUMAN to specify a move.  Check that it's
    # valid (syntactically, in range, and the space is
    # not occupied).  Update the board appropriately.


        move = input("Your turn: \n  Specify a move r, c: ")
        row = int(move[0])
        col = int(move[3])
        while len(move) <4 or int(move[0])< 0 or int(move[3]) <0 or int(move[0]) >2 or int(move[3]) >2 or move[1] != "," or gameBoard[row][col] != " ":
            print("Illegal move specified. Try again!")
            move = input("Your turn: \n  Specify a move r, c: ")
            row = int(move[0])
            col = int(move[3])
        gameBoard[row][col] = "X"





    def machineMove(self):
        # This is the MACHINE's move.  It picks squares randomly
        # until it finds an empty one. Update the board appropriately.
        # Note: this is a really dumb way to play tic-tac-toe.
        print("Machine's turn:")
        while True:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if self.__board[r][c] == " ":
                print("  Machine chooses: ", r, ", ", c, sep="")
                self.__board[r][c] = "O"
                return


def driver():
    """ This plays tic-tac-toe in a pretty simple-minded
    fashion.  The human player goes first with token "X" and
    alternates with the machine using token "O".  We print
    the board before the first move and after each move. """

    # Print the welcome message
    print(WELCOME)
    # Initialize the board and player
    ttt = TicTacToe()

    print(ttt)
    # There are up to 9 moves in tic-tac-toe.
    for move in range(9):
        # The current player may be HUMAN
        # or MACHINE
        if ttt.getPlayer() == HUMAN:
            # If HUMAN, take a move, print the board,
            # and see if it's a win.
            ttt.humanMove()
            print(ttt)
            if ttt.isWin():
                print(YOU_WON)
                return
        else:       # Else Machine takes a move.  Print the
            # board and see if the machine won.
            ttt.machineMove()
            print(ttt)
            if ttt.isWin():
                print(YOU_LOST)
                return
        ttt.swapPlayers()
    # After nine moves with no winner, it's a tie.
    print(YOU_TIED)


driver()