def emptyBoard():
    return[
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]

def columnContent(columnNumber, board):
    column = []
    for row in board:
        cell = row[columnNumber - 1]
        column.append(cell)
    return column

def rowContent(rowNumber, board):
    row = board[6 - rowNumber]
    return row

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

def validSequence(sequence):
    for column in sequence:
        if column < 1 or column > 7:
            return False
    return True

sequence = [1, 2, 3, 1, 4, 5, 1, 2, 3, 4, 2, 2, 1]
board = []
if validSequence(sequence):
    board = completeBoardInOrder(sequence, emptyBoard())
    drawBoard(board)
else:
    print("Columns must be between 1 and 7") 

print('\n')
print(columnContent(2, board))
print('\n')
print(rowContent(2, board))