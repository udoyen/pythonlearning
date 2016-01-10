# The yield keyword is used with generators. 

def gen():
   x = 11
   yield x

it = gen()

print it.next()
