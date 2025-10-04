"""
1. have square puzzle pieces
2. on each of 4 edge of a piece, its either a stub or a slot. Stub fits in a slot.
3. Pieces on edge of the board can be flat.
4. a board be any size
5. image rendering?

---
2d array, either a number (bit masking to rep stub/slot, position of a piece), or an *object (with props to rep)*
"""

from enum import Enum
from typing import Dict, List, Union

class PuzzleGame:
    """
    game state
    main eventloop
    read player input
    """

    def __init__(self, rows:int, cols: int):
        self.board = Board()
        self.render = BoardRenderer()
        self.remaining : List[Piece] = BoardGenerator.generatePieces(rows, cols)
        self.rows = rows
        self.cols = cols


    def readUserInput(self):
        pass

    def mainEventLoop(self):

        # render first

        # user flow 1: play piece
        "read play input, they choose from the list the pieces to play"
        "choose location and orientation for that piece"

        "play the piece by calling Board.playPiece"
        "Board.playPieces try to play it, then return info indicate if the piece fits"
        "if it fits, remove the piece from remaining pieces"
        "if not, then notify the user, and accept the next input"

        "if this is a last piece played, ie, remaining is now empty."
        "check wincon, if every piece is in the intended location"


        # user flow 2: remove piece
        "read location to remove"
        "if in valid, ie, empty, notify user. Pass"

        "remove the piece from the Board, and add it back to self.remainingPieces "


        


class Board:
    """
    track pieces currently placed
    offer api to place, remove, check validity of pieces
    track if game is won.

    // should not contain pieces remaining... put it in games controller
    """

    def __init__(self, rows: int, cols: int, ):
        self.data: List[List[Union[Piece, None]]] = [[None] * cols for _ in range(rows)] # None = no piece placed there

    def playPiece(self, row:int, col:int, piece: "Piece"):
        pass

    def removePiece(self, row, col):
        pass



class Direction(Enum):
    left = 0
    up = 1
    right = 2
    down = 3


class EdgeType(Enum):
    stub = 0
    slot = 1
    flat = 2

    @staticmethod
    def flip(e: "EdgeType"):
        if e == EdgeType.flat:
            return e
        if e == EdgeType.slot:
            return EdgeType.stub
        if e == EdgeType.slot:
            return EdgeType.flat

    @staticmethod
    def fits(e1: "EdgeType", e2: "EdgeType"):
        if e1 == EdgeType.flat or e2 == EdgeType.flat:
            return False
        return EdgeType.flip(e1) == e2

class Piece:
    """
    track where the stubs are
    it should rem orientation
    track the current location
    // remember the intended location for the piece. (with default orientation)
    """

    def __init__(self, row : int, col: int, directionMap: Dict[Direction, EdgeType], orientation: int):
        self.originalRow = row
        self.original = col
        self.directionMap = directionMap
        self.orientation = orientation # number of times rotated clockwise, mod 4 %
    
    def fitsWith(self, other:"Piece"):
        pass

    def render(self, ):
        pass # render itself in the canvas

class BoardGenerator:
    """
    take in a board size, and return a list of pieces that would fit together.
    """

    @staticmethod
    def generatePieces(rows:int, cols:int) -> List[Piece]:
        return []


class BoardRenderer:
    """
    take a Board, and render the placed pieces somehow.
    """
