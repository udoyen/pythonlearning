# Variable declarations
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# create variable x and y
print x
print y

# Print the values of variables x and y
print "I said: %r." % x
print "I also said: '%s'." % y

# Create a boolean variable
hilarious = False
# Create a variable that takes an unknown input "r"
joke_evaluation = "Isn't that joke so funny?! %r"

# Print variable "joke_evaluation" and pass in the value of the unknown variable "r" 
print joke_evaluation % hilarious

# Declare two variables w and e and concatenate them
w = "This is the left side of..."
e = "a string with a right side."

# Concatenate variable w and e using the operator "+"
print w + e

