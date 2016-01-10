from sys import argv

# Assign the number of arguments to be given at the terminal
script, filename = argv

# Open the given file for reading
# and assign it to variable txt
txt = open(filename)

# Print the filename
print "Here's your file %r:" % filename
# Read the file and print the contents to the screen
print txt.read()

# Close file after reading it
txt.close()

# Request the name of the file previuosly given
print "Type the filename again:"

# Get the filename from user at terminal
file_again = raw_input("> ")

# Assign the file to variable 'txt_again'
txt_again = open(file_again)

# Read the file once again and print the contents to the screen
print txt_again.read()

# Close file after reading
txt_again.close()
