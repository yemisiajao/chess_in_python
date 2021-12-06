from __future__ import annotations
from pieces import *


class Game:
    def __init__(self: Game) -> None:
        self.board, self.taken_whites, self.taken_blacks = get_starting_pieces()

    def over(self: Game) -> bool:
        return False


def get_starting_pieces():

    # Create list
    list_of_pieces: list[Piece] = []
    taken_whites: list[Piece] = []
    taken_blacks: list[Piece] = []

    # Fill the list
    list_of_pieces.append(RookBlack())
    list_of_pieces.append(KnightBlack())
    list_of_pieces.append(BishopBlack())
    list_of_pieces.append(QueenBlack())
    list_of_pieces.append(KingBlack())
    list_of_pieces.append(BishopBlack())
    list_of_pieces.append(KnightBlack())
    list_of_pieces.append(RookBlack())

    for i in range(8, 16):
        list_of_pieces.append(PawnBlack())

    for i in range(16, 24):
        list_of_pieces.append(Pawn())

    list_of_pieces.append(Rook())
    list_of_pieces.append(Knight())
    list_of_pieces.append(Bishop())
    list_of_pieces.append(Queen())
    list_of_pieces.append(King())
    list_of_pieces.append(Bishop())
    list_of_pieces.append(Knight())
    list_of_pieces.append(Rook())

    # Set coordinates
    K = 0
    for piece in list_of_pieces:
        Y = int(K % 8)
        X = int((K/8) % 8)
        if (X == 2):
            X = 6
        if (X == 3):
            X = 7
        piece.coordinates = (X, Y)
        K += 1

    # Set piece types

    # Remove pawns for testing:

    # for piece in list_of_pieces:
    #     if piece.type == 'WhitePawn' or piece.type == 'BlackPawn':
    #         list_of_pieces.remove(piece)

    # for piece in list_of_pieces:
    #     if piece.type == 'WhitePawn' or piece.type == 'BlackPawn':
    #         list_of_pieces.remove(piece)

    # for piece in list_of_pieces:
    #     if piece.type == 'WhitePawn' or piece.type == 'BlackPawn':
    #         list_of_pieces.remove(piece)

    # for piece in list_of_pieces:
    #     if piece.type == 'WhitePawn' or piece.type == 'BlackPawn':
    #         list_of_pieces.remove(piece)

    return list_of_pieces, taken_whites, taken_blacks
