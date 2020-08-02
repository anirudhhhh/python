import random
import os

matrix = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
turn = 'X'
def random_in_need():
    return random.randint(0, 8)
def draw():
    os.system("clear")
    for i in range(0, 8, 3):
        print matrix[i] + " " + matrix[i+1] + " " + matrix[i+2]
        print

def inputed():
    marking = int(raw_input("Enter the number you wish to mark: "))
    if matrix[marking-1] == 'X' or matrix[marking-1] == 'O':
        print 'That is marked'
        print
        inputed()
    elif marking < 10 and marking > 0:
        matrix[marking-1] = 'X'
        print
    else:
        print 'That is not available' 

def horizontal():
    for i in range(0, 6, 3):
        if matrix[i] == turn and matrix[i+1] == turn and matrix[i+2] == turn:
            return True
    return False

def vertical():
    for i in range(3):
        if matrix[i] == turn and matrix[i+3] == turn and matrix[i+6] == turn:
            return True
    return False

def diagonal():
    if matrix[4] == turn:
        if (matrix[2] == turn and matrix[6] == turn) or (matrix[0] == turn and matrix[8] == turn):
            return True 
    return False

def check_match(a, b, c):
    if (matrix[a] == 'X' and matrix[b] == 'X' and not(matrix[c] == 'X' or matrix[c] == 'O')) or (matrix[a] == 'O' and matrix[b] == 'O' and not(matrix[c] == 'X' or matrix[c] == 'O')):
        matrix[c] = 'O'
        return True

    elif (matrix[a] == 'X' and matrix[c] == 'X' and not(matrix[b] == 'X' or matrix[b] == 'O')) or (matrix[a] == 'O' and matrix[c] == 'O' and not(matrix[b] == 'X' or matrix[b] == 'O')):
        matrix[b] = 'O'
        return True

    elif (matrix[c] == 'X' and matrix[b] == 'X' and not(matrix[a] == 'X' or matrix[a] == 'O')) or (matrix[c] == 'O' and matrix[b] == 'O' and not(matrix[a] == 'X' or matrix[a] == 'O')):
        matrix[a] = 'O'
        return True

    return False

def all_check():
    for i in range(3):
        if check_match(i, i+3, i+6):
            return True
        
    for j in range(0, 6, 3):
        if check_match(j, j+1, j+2):
            return True

    if check_match(0, 4, 8) or check_match(2, 4, 6):
        return True
    return False

def comp_turn():
    if not(all_check()):
        a = random_in_need()
        if matrix[a] == 'X' or matrix[a] == 'O':
            comp_turn()
        matrix[a] = 'O'

def win():
    if diagonal() or vertical() or horizontal():
        return True
    return False

n = 1
while n < 10:
    draw()
    if turn == 'X':
        inputed()
    else:
        comp_turn()

    if win():
        if turn == 'X':
            draw()
            print 'Player won'
        else:
            draw()
            print 'Computer won'
        break
    else:
        if turn == 'O':
            turn = 'X'
        else:
            turn = 'O'

    n += 1
else:
    print 'Draw'