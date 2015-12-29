# Here we enter the questions to the users directly in the 
# 'raw_input method' rather than on a separate line

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
     age, height, weight)
