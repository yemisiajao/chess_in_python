from __future__ import annotations
import numpy as np
from setup import *


def board_limits(X, Y):
    if (0 <= X < 8) and (0 <= Y < 8):
        return True
    else:
        return False


def is_empty(X, Y, game: Game):
    for piece in game.board:
        if (X, Y) == piece.coordinates:
            return False
    return True


def what_colour(X, Y, game: Game):
    for piece in game.board:
        if (X, Y) == piece.coordinates:
            return piece.colour


def in_board(X, Y):
    if (0 <= X <= 7) and (0 <= Y <= 7):
        return True
    else:
        return False


def pawn_moves(X, Y, piece, game: Game, BlankBoard):

    if piece.colour == 0:
        x = -1
    else:
        x = 1

    if is_empty(X+x, Y, game):
        BlankBoard[X+x, Y] = True

    if not is_empty(X+x, Y+1, game):
        if piece.colour != what_colour(X+x, Y+1, game):
            BlankBoard[X+x, Y+1] = True

    if not is_empty(X+x, Y-1, game):
        if piece.colour != what_colour(X+x, Y-1, game):
            BlankBoard[X+x, Y-1] = True

    if X == 6 or X == 1:
        if is_empty(X+x, Y, game) and is_empty(X+x*2, Y, game):
            BlankBoard[X+x*2, Y] = True

    if not is_empty(X+x*2, Y+1, game):
        if piece.colour != what_colour(X+x*2, Y+1, game):
            BlankBoard[X+x*2, Y+1] = True

    if not is_empty(X+x*2, Y-1, game):
        if piece.colour != what_colour(X+x*2, Y-1, game):
            BlankBoard[X+x*2, Y-1] = True

    return BlankBoard


def rook_moves(X, Y, piece, game: Game, BlankBoard):
    if X < 7:
        x = X+1
        while x < 7 and is_empty(x, Y, game):
            BlankBoard[x, Y] = True
            x += 1
        if what_colour(x, Y, game) != piece.colour:
            BlankBoard[x, Y] = True

    if X > 0:
        x = X-1
        while x > -1 and is_empty(x, Y, game):
            BlankBoard[x, Y] = True
            x -= 1
        if what_colour(x, Y, game) != piece.colour:
            BlankBoard[x, Y] = True

    if Y < 7:
        y = Y+1
        while y < 7 and is_empty(X, y, game):
            BlankBoard[X, y] = True
            y += 1
        if what_colour(X, y, game) != piece.colour:
            BlankBoard[X, y] = True

    if Y > 0:
        y = Y-1
        while y > -1 and is_empty(X, y, game):
            BlankBoard[X, y] = True
            y -= 1
        if what_colour(X, y, game) != piece.colour:
            BlankBoard[X, y] = True

    return BlankBoard


def bishop_moves(X, Y, piece, game: Game, BlankBoard):

    if X < 7 and Y < 7:
        x = X + 1
        y = Y + 1
        while x < 7 and y < 7 and is_empty(x, y, game):
            BlankBoard[x, y] = True
            x += 1
            y += 1
        if what_colour(x, Y, game) != piece.colour:
            BlankBoard[x, y] = True

    if X < 7 and Y > 0:
        x = X + 1
        y = Y - 1
        while x < 7 and y > 0 and is_empty(x, y, game):
            BlankBoard[x, y] = True
            x += 1
            y -= 1
        if what_colour(x, Y, game) != piece.colour:
            BlankBoard[x, y] = True

    if X > 0 and Y > 0:
        x = X - 1
        y = Y - 1
        while x > 0 and y > 0 and is_empty(x, y, game):
            BlankBoard[x, y] = True
            x -= 1
            y -= 1
        if what_colour(x, Y, game) != piece.colour:
            BlankBoard[x, y] = True

    if X > 0 and Y < 7:
        x = X - 1
        y = Y + 1
        while x > 0 and y < 7 and is_empty(x, y, game):
            BlankBoard[x, y] = True
            x -= 1
            y += 1
        if what_colour(x, Y, game) != piece.colour:
            BlankBoard[x, y] = True

    return BlankBoard


def free_space(X, Y, piece, game: Game):
    if (is_empty(X, Y, game) or what_colour(X, Y, game) != piece.colour) and in_board(X, Y):
        return True
    return False


def knight_moves(X, Y,  piece, game: Game, BlankBoard):

    if free_space(X-1, Y-2, piece, game):
        BlankBoard[X-1, Y-2] = True

    if free_space(X-2, Y-1, piece, game):
        BlankBoard[X-2, Y-1] = True

    if free_space(X+1, Y-2, piece, game):
        BlankBoard[X+1, Y-2] = True

    if free_space(X+2, Y-1, piece, game):
        BlankBoard[X+2, Y-1] = True

    if free_space(X-1, Y+2, piece, game):
        BlankBoard[X-1, Y+2] = True

    if free_space(X-2, Y+1, piece, game):
        BlankBoard[X-2, Y+1] = True

    if free_space(X+1, Y+2, piece, game):
        BlankBoard[X+1, Y+2] = True

    if free_space(X+2, Y+1, piece, game):
        BlankBoard[X+2, Y+1] = True

    return BlankBoard


def king_moves(X, Y,  piece, game: Game, BlankBoard):

    if free_space(X+1, Y+1, piece, game):
        BlankBoard[X+1, Y+1] = True

    if free_space(X+1, Y, piece, game):
        BlankBoard[X+1, Y] = True

    if free_space(X+1, Y-1, piece, game):
        BlankBoard[X+1, Y-1] = True

    if free_space(X, Y+1, piece, game):
        BlankBoard[X, Y+1] = True

    if free_space(X, Y-1, piece, game):
        BlankBoard[X, Y-1] = True

    if free_space(X-1, Y+1, piece, game):
        BlankBoard[X-1, Y+1] = True

    if free_space(X-1, Y, piece, game):
        BlankBoard[X-1, Y] = True

    if free_space(X-1, Y-1, piece, game):
        BlankBoard[X-1, Y-1] = True

    return BlankBoard


def moves(piece: Piece, game: Game):
    (X, Y) = piece.coordinates
    BlankBoard = np.full((8, 8), False)

    if piece.type == 'WhitePawn' or piece.type == 'BlackPawn':
        BlankBoard == pawn_moves(X, Y, piece, game, BlankBoard)

    elif piece.type == 'Rook':
        BlankBoard == rook_moves(X, Y, piece, game, BlankBoard)

    elif piece.type == 'Bishop':
        BlankBoard == bishop_moves(X, Y, piece, game, BlankBoard)

    elif piece.type == 'Queen':
        BlankBoard == rook_moves(X, Y, piece, game, BlankBoard)
        BlankBoard == bishop_moves(X, Y, piece, game, BlankBoard)

    elif piece.type == 'Knight':
        BlankBoard == knight_moves(X, Y, piece, game, BlankBoard)

    elif piece.type == 'King':
        BlankBoard == king_moves(X, Y, piece, game, BlankBoard)

    return BlankBoard
