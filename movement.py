import copy
from moves import *


def ValidateNInput(N: str) -> int:
    if not N in ['1', '2', '3', '4', '5', '6', '7', '8']:
        raise ValueError('Must input a number between 1 and 8')

    return int(N) - 1


def ValidateLInput(L: str) -> int:
    L = L.upper()
    allowedLValues = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    if not L in allowedLValues:
        raise ValueError('Must input a letter between A and H')

    return allowedLValues.index(L)


def MoveLetter():

    while True:
        try:
            return ValidateLInput(input('Select a square A-H: '))

        except ValueError as e:
            print(e)


def MoveNumber():
    while True:
        try:
            return ValidateNInput(input('Select a square 1-8: '))

        except ValueError as e:
            print(e)


def taken(output, turn, game):
    for piece in game.board:
        (X, Y) = piece.coordinates
        if (X, Y) == output:
            if piece.colour == turn:
                print('You already have a piece there, try again!')
                return False
            else:
                if turn == 0:
                    game.taken_blacks.append(piece)
                    game.board.remove(piece)
                else:
                    game.taken_whites.append(piece)
                    game.board.remove(piece)

                return True

def CheckPiece(inputX, inputY, turn, game):
    for piece in game.board:
        (X, Y) = piece.coordinates
        input = (int(inputX), int(inputY))
        if (X, Y) == input and piece.colour == turn:
                return True
    return False


def ChoosePiece(inputX, inputY, turn, game) -> Piece:
    for piece in game.board:
        (X, Y) = piece.coordinates
        input = (int(inputX), int(inputY))
        if (X, Y) == input and piece.colour == turn:
                return piece
    return game.board[0]


def inCheck(turn, game):

    # Get king coordinates
    for piece in game.board:
        if piece.colour == turn and piece.type == 'King':
            (X, Y) = piece.coordinates

    for piece in game.board:
        if piece.colour != turn:
            piece_moves = moves(piece, game)
            if piece_moves[X, Y]:
                return True

    return False


def inCheckMate(turn, game):

    for piece in game.board:
        if piece.colour == turn:
            piece_moves = moves(piece, game)
            for x in range(8):
                for y in range(8):
                    if piece_moves[x, y]:
                        game_2 = copy.deepcopy(game)
                        K = taken((x, y), turn, game_2)
                        piece_index = game.board.index(piece)
                        piece_2 = game_2.board[piece_index]
                        piece_2.coordinates = (x, y)
                        if not inCheck(turn, game_2):
                            return False

    return True
