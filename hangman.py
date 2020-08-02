import random
import os

os.system("clear")

words = ['abandon', 'ability', 'able', 'about', 'above', 'abroad', 'bell', 'belong', 'below', 'belt', 'bench', 'bend', 'beneath', 'benefit', 'beside', 'besides']

word_to_guess = words[random.randint(0, len(words) - 1)]

turns = 6
length = len(word_to_guess)

dashes = ''
for i in range(len(word_to_guess)):
    dashes = dashes + '_'
win_ = 1
j = 0

while True:
    os.system("clear")
    if turns == 0:
        print 'You lost'
        print 'The word was ' + word_to_guess
        break
    if dashes == word_to_guess:
        print "You won"
        break
    print turns
    print dashes
    guess = raw_input("Guess a letter of the word ")
    for i in range(length):
        if word_to_guess[i] == guess:
            dashes = dashes[:i] + guess + dashes[i+1:]
            os.system("clear")
            print turns
            print dashes
            j = 1
    if j == 1:
        j = 0
    else:
        print "The letter was not in word"
        turns -= 1 