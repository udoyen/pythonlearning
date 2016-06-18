from sys import argv






print "The script is called:"
script =  raw_input("> ")
print "Your first name variable is:"
first_name = raw_input("> ")
print "Your second name variable is:"
second_name = raw_input("> ")
print "Your age is:"
age = raw_input("> ")
print "Your sex is:"
sex = raw_input("> ")
print "Your nationality is:"
nationality = raw_input("> ")


exec "script, first_name, second_name, age, sex, nationality = argv"
