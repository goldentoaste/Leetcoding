# Design tic tac toe

# Design a class, with interface to interaction the game, eventloop and rendering
from typing import Literal
import sys


class TicTacToe:
    def __init__(self):
        self.initGame()

    def startGame(self):
        self.eventLoop()

    def initGame(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]  # assume 3x3 for now, could update this later
        self.turnPlayer: Literal["X", "O"] = "X"
        self.remainingSpace = 9

    def readInput(self):
        """
        read n parse user input

        returns None in case input should be skipped.
        """
        print(f"Turn player: {self.turnPlayer}, (row, col)")
        rawInput = input("> ").lower()

        if rawInput == "help":
            print("help menui..,.")
            return None

        if rawInput == "exit":
            print("thanks for playing!")
            sys.exit(0)

        items = [item.strip() for item in rawInput.split(",")]
        if len(items) != 2:
            print(f"bad input: {rawInput}")
            return None

        try:
            row = int(items[0])
            col = int(items[1])

            if not ((0 <= row <= 2) and (0 <= col <= 2)):
                print(f"Coordinate not range: {row}, {col}")
                return None
            return (row, col)
        except ValueError:
            print(f"bad input: {rawInput}")
            return None

    def playMove(self, row: int, col: int):
        """
        play a move given the coordinates

        check win states, return the true if the turn player won.
        """
        if self.board[row][col] != "_":
            print(f"Position already played: {row} {col}")
            return False

        self.board[row][col] = self.turnPlayer
        self.turnPlayer = "X" if self.turnPlayer == "O" else "O"
        self.remainingSpace -= 1
        return True

    def checkWinCon(self, row: int, col: int):
        player = self.board[row][col]

        # ver, hor, main diag, cross diag
        directions = [(1, 0), (0, 1), (1, -1), (1, 1)]

        for direction in directions:
            index = 1
            dRow, dCol = direction
            matchedCount = 1

            for sign in (1, -1):
                while True:
                    currentRow = dRow * index * sign + row
                    currentCol = dCol * index * sign + col
                    if not ((0 <= currentRow <= 2) and (0 <= currentCol <= 2)):
                        break

                    if self.board[currentRow][currentCol] == player:
                        matchedCount += 1
                    index += 1

            if  matchedCount == len(self.board):
                print(f"Player {player} has won!")
                return True

        if self.remainingSpace == 0:
            print("The Match has ended in a draw!")
            return True

        return False

    def render(self):
        for row in self.board:
            print(" | ".join(row))

    def eventLoop(self):
        """
        main event loop, call other function to handle each steps of the game.
        """

        while True:
            self.render()
            playerInput = self.readInput()
            if not playerInput:
                continue

            validPlay = self.playMove(playerInput[0], playerInput[1])
            if not validPlay:
                continue
            gameEnded = self.checkWinCon(playerInput[0], playerInput[1])

            if gameEnded:
                playAgain = input("Play another? (y/n)> ").lower() == "y"
                if not playAgain:
                    print("Thanks for playing!")
                    break


if __name__ == "__main__":
    game = TicTacToe()
    game.startGame()
