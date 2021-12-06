from __future__ import annotations


class Piece:
    def __init__(self: Piece) -> None:
        self.coordinates: tuple[int, int] = (0, 0)
        self.symbol = '| P  '
        self.colour = bool(0)
        self.type = 'P'


# The Whites

class Pawn (Piece):
    def __init__(self: Pawn) -> None:
        # General pawn rules
        self.symbol = '| ♙  '
        self.colour = 0
        self.type = 'WhitePawn'


class Rook (Piece):
    def __init__(self: Rook) -> None:
        # General Rook rules
        self.symbol = '| ♖  '
        self.colour = 0
        self.type = 'Rook'


class Knight (Piece):
    def __init__(self: Knight) -> None:
        # General Knight rules
        self.symbol = '| ♘  '
        self.colour = 0
        self.type = 'Knight'


class Bishop (Piece):
    def __init__(self: Bishop) -> None:
        # General Bishop rules
        self.symbol = '| ♗  '
        self.colour = 0
        self.type = 'Bishop'


class King (Piece):
    def __init__(self: King) -> None:
        # General King rules
        self.symbol = '| ♔  '
        self.colour = 0
        self.type = 'King'


class Queen (Piece):
    def __init__(self: Queen) -> None:
        # General Queen rules
        self.symbol = '| ♕  '
        self.colour = 0
        self.type = 'Queen'


# The Blacks

class PawnBlack (Pawn):
    def __init__(self: PawnBlack) -> None:
        # Reverse direction
        self.symbol = '| ♟  '
        self.colour = 1
        self.type = 'BlackPawn'


class RookBlack (Rook):
    def __init__(self: RookBlack) -> None:
        self.symbol = '| ♜  '
        self.colour = 1
        self.type = 'Rook'


class KnightBlack (Knight):
    def __init__(self: KnightBlack) -> None:
        self.symbol = '| ♞  '
        self.colour = 1
        self.type = 'Knight'


class BishopBlack (Bishop):
    def __init__(self: BishopBlack) -> None:
        self.symbol = '| ♝  '
        self.colour = 1
        self.type = 'Bishop'


class KingBlack (King):
    def __init__(self: KingBlack) -> None:
        self.symbol = '| ♚  '
        self.colour = 1
        self.type = 'King'


class QueenBlack (Queen):
    def __init__(self: QueenBlack) -> None:
        self.symbol = '| ♛  '
        self.colour = 1
        self.type = 'Queen'
