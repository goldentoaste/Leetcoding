

'''
Design the game of 2048, assumptions/game rules

its a game in a grid, default to 4x4 (2d array)
each turn, spawn 1 or 2 new numbers(2 or 4) into the grid (make this a func)

then player gets to move their board the any of 4 directions, when numbers collide, they get merged if the numbers are the same, towards the direction of move

before player makes the move, we can check if any of the cells has either same number, or empty. If not, declare game over.

after player makes moves, display the board again.
'''

from enum import Enum

class Direction(Enum):
    TOP:0
    RIGHT:1
    DOWN:2
    LEFT:3



class GameBoard:
    def __init__(self):
        self.board = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ] # dynmiacally generate this if needed.

    
    def spawnNewNums(self,):
        '''
        randomly put 1 or 2 of (2 or 4)s into the empty spots in the field.
        '''

    def move(self, direction: Direction):
        '''
        move all numbers in board based on direction.
        2 0 2 2
        image the blocks are falling towards the ground, have a pointer for where ground is. Have a pointer for where the current block this.
        
        '''

    def checkWin(self) -> bool:
        '''
        check if any neighbors is same number or empty. If none is the case, then game over.
        '''

    def render(self):
        '''
        render the board
        '''


class Game2048:
    '''
    Main game class, containing only game states, read inputs.
    '''

    def __init__(self):
        self.gameboard = GameBoard()
        self.score = 0
        self.turns = 0

    def eventLoop(self):
        '''
        1. display board
        2. get user input
        3. 
        '''
