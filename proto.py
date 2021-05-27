def emptyBoard():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def completeBoardInOrder(sequence, board): 
    for i, column in enumerate(sequence):
        tokenNumber = 1 + (i % 2)
        dropTokenInColumn(tokenNumber, column, board)
    return board

def dropTokenInColumn(token, column, board):
    for row in range (6, 0, -1):
        if board[row - 1][column - 1] == 0:
            board[row - 1][column - 1] = token
            return

def drawBoard(board):
    for row in board:
        for cell in row:
            if cell == 0:
                print('  ', end='')
            else:
                print(' %s ' % cell, end='')
        print('')

sequence = [1, 2, 3, 1]
drawBoard(completeBoardInOrder(sequence, emptyBoard()))