# Creates a function that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "get a blanket.\n"
    
print "We can just give the function numbers directly:"
# Calling the function with arguments supplied
cheese_and_crackers(20, 30)

# Creating variables that will passed to the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# passing the created variables to the function as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Passing math calculations as arguments to the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Adding values to the supplied arguments for the function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
