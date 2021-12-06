from __future__ import annotations
from movement import *


def print_board(board: list[Piece]) -> None:

    # Build the board
    BlankBoard = np.full((8, 8), '|    ')

    for piece in game.board:
        (X, Y) = piece.coordinates
        BlankBoard[X][Y] = piece.symbol

    # Display the board

    Y_Coordinates = "    A    B    C    D    E    F    G    H  "

    for piece in game.taken_blacks:
        print(piece.symbol, end='')
    print('', end='\n')
    for piece in game.taken_whites:
        print(piece.symbol, end='')

    print('', end='\n')
    print(Y_Coordinates, end='\n')
    K = 0
    for row in BlankBoard:
        print('', end='\n')
        K += 1
        print(K, end=' ')
        for collum in row:
            print(collum, end='')
        print('|', end='\n')


def play(turn):

    while not game.over():

        print_board(game.board)

        if turn == 0:
            print('White turn!')
        else:
            print('Blacks turn!')

        if inCheck(turn, game):
            if inCheckMate(turn, game):
                print('Game Over')
                if turn == 0:
                    print('Black wins')
                else:
                    print('White wins')
                break
            print('You are in check, protect your king!')

        if inCheckMate(turn, game):
            print('Game Over')
            print('Stalemate')

        print('Select which piece to move')
        inputX = MoveNumber()
        inputY = MoveLetter()

        if not CheckPiece (inputX, inputY, turn, game):
            print ('You do not have a piece there!')
            continue

        print('Select where to move')
        outputX = MoveNumber()
        outputY = MoveLetter()

        # print ("Selected piece", outputX, outputY )
        if MakeMove(inputX, inputY, outputX, outputY, turn, game):

            if turn == 0:
                turn = 1
            else:
                turn = 0

            continue

        continue
    

def MakeMove(inputX, inputY, outputX, outputY, turn, game):
    Moved = False
    output = (int(outputX), int(outputY))
    game_2 = copy.deepcopy(game)
    piece_2 = ChoosePiece(inputX, inputY, turn, game_2)
    (X, Y) = piece_2.coordinates

    Moves = moves(piece_2, game_2)
    if not Moves[outputX][outputY]:
        print("That is not a possible move, try again!")
        return False

    if turn != piece_2.colour:
        print("That is not your piece, try again!")
        return False

    K = taken(output, turn, game_2)
    if K == 0:
        return False

    piece_2.coordinates = output

    # Check if your in check

    if inCheck(turn, game_2):
        print('This move puts you in check!')
        return False

    # If not in check, make the changes permenant

    piece_index = game_2.board.index(piece_2)

    K = taken(output, turn, game)
    if K == False:
        return False

    piece = game.board[piece_index]
    piece.coordinates = output

    Moved = True
    return True


game = Game()

turn = 0
play(turn)
