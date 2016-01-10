#!/usr/bin/python

# We use the as keyword if we want to give a module a different alias. 

import random as rnd

for i in range(10):
   print rnd.randint(1, 10),
