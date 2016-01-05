# In the next example, we show how to create a user defined
# exception using the raise keyword.

class YesNoException(Exception):
   def __init__(self):
      print 'Invalid value'


answer = 'y'

if (answer != 'yes' and answer != 'no'):
   raise YesNoException
else:
   print 'Correct value'
