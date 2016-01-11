def main():  # (me):this reads a file line by line and splits each line at the ":" character point
""" This test function checks to make sure the password is in the key:value pair
    format so the usename and password can be well weparated """
    passFile = open('passwords.txt')		# Open the password file
    for line in passFile.readlines():  # Read through the file
        if ":" in line:
            user = line.split(':')[0]  # assign any word found to user variable
            # Prepare the user name etc, (me): assign the second value after
            # the split point ":"  to cryptPass
            cryptPass = line.split(':')[1].strip(' ')
            # (me): concatenate user to printed output
            print "[*] Cracking Password For: " + user
            # testPass(cryptPass)				# Call it to crack the users password
            print "user: %s password: %s" % (user, cryptPass)
        else: # if key:value pair absent print found text
            print "Plain line of text printed: %s" % line

if __name__ == "__main__":  # mian point of entry for aapplication
    main()
