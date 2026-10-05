


'''
* 2 player game, alternating plays
* a player plays from top of the board, the falls down
* when the piece cause a 4 in a row(row, col, diags) of the same color, then that player wins
* If the entire board is filled, and no one has won yet, call it a draw.

7x6 board
'''


RED_PLAYER = "R"
BLUE_PLAYER = "B"

def getOpponent(player:str):
    if player == RED_PLAYER:
        return BLUE_PLAYER
    elif player == BLUE_PLAYER:
        return RED_PLAYER
    return RED_PLAYER

class Connect4Game:
    '''
    data structs to contains game state

    read player inputs 

    playing moves 

    checking for wincon

    main event loop be here
    '''

    def __init__(self):
        self.rows = 6
        self.cols = 7
        
        self.board = [["_"] * self.cols for _ in range(self.rows)]
        self.turnPlayer = RED_PLAYER