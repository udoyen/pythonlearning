# The lambda keyword creates a new anonymous function. An anonymous function is a function,
# which is not bound to a specific name. It is also called an inline function.

for i in (1, 2, 3, 4, 5):
   a =  lambda x: x * x
   print a(i),
