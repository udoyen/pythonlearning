from sys import exit
from random import randint

code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
guess = raw_input("[keypad]> ")
guesses = 0
        
        
while guess != code and guesses < 10:
   
    print "BZZZZEDDD!"
    guesses += 1
    print "Guesses: %d" % guesses
    guess = raw_input("[keypad]> ")
