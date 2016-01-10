# If we want to access variables defined outside functions,
# we use the global keyword. 

x = 15

def function():
   global x
   x = 45

function()
print x
