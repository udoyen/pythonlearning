# Ask user for name of file to read content
print "Enter the name of file to read"

# Assign user input to variable
filename = raw_input('> ')

# Open file for reading and assign to variable 'myfile'
myfile = open(filename)

# Print name of file
print "Here's your file %r:" % filename

# Read file content and print to screen
print myfile.read()

myfile.close()

# Ask for filename again
print "Type the filename again:"

# Assign user input to variable
txt = raw_input('> ')

# Open file for reading and assign to variable 'myfile'
dfile = open(txt)

# Read file content and print to screen
print dfile.read()

dfile.close()
