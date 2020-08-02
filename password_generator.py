import random
import os

os.system("clear")

pass_length = int(raw_input('What is the preffered password length: '))

letter_amount = 0
num_amount = 0
special_amount = 0

while not(pass_length == letter_amount + num_amount + special_amount):
    print
    letter_amount = int(raw_input('How many letter(s) [a, b, c, etc.] should be in the password: '))
    num_amount = int(raw_input('How many number(s) [1, 2, 3, 4 etc.] should be in the password: '))
    special_amount = int(raw_input('How many special character(s) [@, #, & etc.] should be in the password: '))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
specials = ['!', '@', '#', '$', '%', '^', '&', '*']

password = ""

while not(len(password) == pass_length):
    which_one = random.randint(0, 2)
    if which_one == 0:
        if letter_amount > 0:
            k = random.randint(0, 25)
            password = password + letters[k]
            letter_amount -= 1

    elif which_one == 1:
        if num_amount > 0:
            k = random.randint(0, 9)
            password = password + nums[k]
            num_amount -= 1
    
    else:
        if special_amount > 0:
            k = random.randint(0, 7)
            password = password + specials[k]
            special_amount -= 1
    
print password 