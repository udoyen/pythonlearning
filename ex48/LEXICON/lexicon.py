# create variables
direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'in', 'of','from','at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')
number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
error_message = "wrong choice!"

# ask user for input
# stuff = raw_input('> ')

# place user entry in variable words
# and split it
# words = stuff.split()

def scan(word, *words): # '*words' lets you give a variable number of arguments to a function
    words = word.split()
    return [('direction', w) for w in words if w in direction]
          
