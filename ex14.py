from sys import argv

script, user_name = argv
# Decalare text or prompt to be seen by the user
# for all request for inout
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
# The 'prompt = >' is seen by user as they are asked for some input
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
# The 'prompt = >' is seen by user as they are asked for some input
lives = raw_input(prompt)

print "What kind of computer do you have?"
# The 'prompt = >' is seen by user as they are asked for some input
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
