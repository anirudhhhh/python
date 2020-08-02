import random
import os

play_more = 'yes'

while play_more.lower() == 'yes' or play_more.lower() == 'y':
    os.system('clear')
    num = random.randint(1, 6)
    if num == 1:
        print "."
    elif num == 2:
        print "."
        print 
        print
        print " ."
    elif num == 3:
        print '.'
        print
        print ' .'
        print 
        print '  .'
    elif num == 4:
        print '. .'
        print 
        print '. .'
    elif num == 5:
        print '. .'
        print
        print ' . '
        print 
        print '. .'
    else:
        print '. . .'
        print
        print '. . .'
    print num
    play_more = raw_input("Roll Again[y/n]: ")        
    