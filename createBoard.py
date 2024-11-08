import random as rn

def createBoard(num):
    board = list(map(lambda x: list(map(lambda x: rn.choice([True, False]), range(num))), range(num)))

    #Ensure that each column has at least one True
    for j in range(num):
        if not any(board[i][j] for i in range(num)):
            board[rn.randrange(0, num)][j] = True
    
    #Ensure that each row has at least one True
    for i in range(num):
        if not any(board[i][j] for j in range(num)):
            board[i][rn.randrange(0, num)] = True
    
    return board