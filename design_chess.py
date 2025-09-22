
'''
8x8 board
2 players, alternating plays

standard chess pieces, + new piece mage

* mage
    + either move like King
    + moves to any spots (once every 5 turns)
    > turn/time based action
* castling
* any rendering ()
'''


BLACK = 0
WHITE = 1

def getOpponent(color:int):
    return (color + 1) % 2

class ChessGame:
    '''
    hold game states
    read input
    start/end games
    
    call supporting functions and class to make a game actions happen
    '''
    pass


class ChessBoard:
    '''
    hold data structure containing chess pieces

    getSelected piece that a player (clicked, row/col)

    getMoves of the selected piece

    rendering
    render selected piece's moves
    '''


class Piece:
    '''
    abstract class representing a piece
    '''    
    def __init__(self, row:int, col:int, color:int):
        self.row = row
        self.col = col
        self.color = color


    def update(self):
        '''
        update any turn based actions, such as mage timing
        '''
        pass

    def getAvailableMoves(self, board:"ChessBoard"):
        '''
        get possible moves this piece can take
        given current board state
        '''


    def render(self):
        '''
        render this piece on board
        '''

class Pawn(Piece):

    def __init__(self, row:int, col:int, color:int):
        super().__init__(row, col, color)
        self.firstMove = True
    


class Mage(Piece):
    def __init__(self, row:int, col:int, color:int):
        super().__init__(row, col, color)
        self.teleportCooldown = 5
        self.teleportTimer = 0 # while timer == 0, mage is ready teleport, reset to cd after use

    def update(self):
        if self.teleportTimer > 0:
            self.teleportTimer -= 1

    def getAvailableMoves(self, board):
        '''
        check timer, if timer > 0 then return all the positions on board
        other wise, only return adj spots
        '''

class Knight(Piece):
    def __init__(self):
        super().__init__()



class Move:
    '''
    originator: Piece
    target location: row/col (used rendering for move selection purpose)
    
    contain a list of actions
    '''

class Action:
    '''
    - the piece object involved
    - action name, to describe type of action invoked: move, capture, etc
    '''


'''
Knight:  [
    Move{
        originator: knight instance
        target: (row, col),

        actions: [
            Action{
                piece: knight instance
                actionName: "move"
                target: (row, col)
            }
        ]
    },

    Move{
        originator: knight instance
        target: (row, col),

        actions: [
            Action{
                piece: knight instance
                actionName: "move"
                target: (row, col)
            },
            Action{
                piece: a pawn instance
                actionName: "capture"
                target: (row, col)
            }
        ]
    }
]
'''