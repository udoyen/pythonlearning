# Ask user question and assign this information to various variables
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# Print out the collected information
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)