ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, lets fix that."

# split ten_things into six separate items using the space between them
# assign these split items to variable stuff
stuff = ten_things.split(' ') # python: split(' ', ten_things)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10: # python: len(10, stuff)
    next_one = more_stuff.pop() # python: pop(-1, more_stuff)
    print "Adding: ", next_one
    stuff.append(next_one) # python: append(stuff, next_one)
    print "There's %d items now." % len(stuff)

print "There  we go: ", stuff

print "Let's do some things with stuff"

print stuff[1] # python: index(1, stuff)
print stuff[-1] # whoa! fancy show lat item on list          python: index(-1, stuff)
print stuff.pop() # remove the last item in list             python: pop(-1, stuff)
print ' '.join(stuff) # what? cool! joins items of list into single string   python: join(' ', stuff)
print '#'.join(stuff[3:5]) # super stellar! splice the list and join the removed part using the character '#'   python: join('#', stuff)
