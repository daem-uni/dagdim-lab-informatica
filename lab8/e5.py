# Game states
GAME_RUNNING = 0
PLAYER_1_WON = 1
PLAYER_2_WON = 2
DRAW = 3

def printBoard(board):
    for i in range(len(board)):
        print("   |   |   ")
        print("%2s |%2s |%2s " % tuple(board[i]))
        if i < len(board) - 1:
            print("___|___|___")
        else:
            print("   |   |   ")

def updateGameState(board):
    checkArrays = []
    for i in range(8):
        checkArrays.append([])
    
    for i in range(len(board)):
        checkArrays[0].append(board[i][i])
        checkArrays[1].append(board[-i - 1][i])

        for j in range(len(board[0])):
            checkArrays[2 + j * 2].append(board[i][j])
            checkArrays[3 + j * 2].append(board[j][i])
    
    emptyFlag = False
    for array in checkArrays:
        sign = array[0]
        flag = True
        for element in array:
            if element == '':
                emptyFlag = True
                flag = False
            elif sign != element:
                flag = False
            
        if flag:
            if sign == signs[0]:
                return PLAYER_1_WON
            else:
                return PLAYER_2_WON

    if emptyFlag:
        return GAME_RUNNING
    else:
        return DRAW

currentBoard = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']      
]

turn = 0
signs = ['O', 'X']
gameState = GAME_RUNNING

while gameState == GAME_RUNNING:
    print(f"Turno del giocatore {turn + 1} (Segno: {signs[turn]}):")

    print()
    printBoard(currentBoard)
    print()

    row = int(input("Inserisci riga: "))
    column = int(input("Inserisci colonna: "))

    while row < 1 or row > 3 or column < 1 or column > 3 or currentBoard[row - 1][column - 1] != '':
        print("Mossa non valida.")       
        row = int(input("Inserisci riga: "))
        column = int(input("Inserisci colonna: "))
    print()

    currentBoard[row - 1][column - 1] = signs[turn]

    gameState = updateGameState(currentBoard)

    if turn == 0:
        turn = 1
    else:
        turn = 0

printBoard(currentBoard)

if gameState == DRAW:
    print("Pareggio!")
elif gameState == PLAYER_1_WON:
    print(f"Ha vinto il giocatore 1 ({signs[0]})!")
elif gameState == PLAYER_2_WON:
    print(f"Ha vinto il giocatore 2 ({signs[1]})!")
