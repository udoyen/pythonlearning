print "Let's practice everything."
print 'You\'d need to know \'bout excapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot deiscern \n the needs of love
nor comprehend passion from intuition
and required an explanation
\n\t\twhere there is none.
"""

print "----------------"
print poem
print "----------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# Function that returns three values in the order they appear
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates    
    


start_point = 10000
# Assign variable names to the return values of the function, in the 
# return order. The name given is irrelevant
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
# Print the return values in order
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# Function retruns values in the order they are generated in the function
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)




