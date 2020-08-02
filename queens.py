#! /usr/bin/env python3
queens = int(input('How many queens: '))

board = []
def create_board(n):
    global board
    global queens
    if n == 0:
        return True
    row = []
    for i in range(queens):
        row.append('_')
    board.append(row)
    create_board(n-1)

create_board(queens)

def check(y, x):
    
    # Check diagonals, vertical and horizontal
    
    for i in range(y):
        if board[i][x] == 'Q':
            return False
        d = y-i
        if x >= d:
            if board[i][x-d] == 'Q':
                return False
        if x + d < queens:
            if board[i][x+d] == 'Q':
                return False

    # It is safe
    return True

found = 0

def place(y):
    global queens
    global found
    if y == queens: # terminating condition
        found += 1
        printB()
        return True
    for i in range(queens):
        if check(y, i):
            board[y][i] = 'Q'
            place(y + 1)  
            board[y][i] = '_'


    return False

def printB():
    global found
    global board
    global queens
    for i in range(queens):
        print(board[i])
    print(found)
    print()

printB()
place(0)