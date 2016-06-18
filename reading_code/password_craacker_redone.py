# Script Name	: password_cracker.py
# Author		: Craig Richards
# Created		: 20 May 2013
# Last Modified	:
# Version		: 1.0

# Modifications	:

# Description	: Old school password cracker using python

import crypt  # Import the module


def testPass(cryptPass):  # Start the function
    """ function to compare given password with stored password """
    # (me): splice password from zero index to index position two
    salt = cryptPass[0:2]
    # Open the dictionary file, (me): check the dictionary file for key value
    # pair
    try: # check to make sure file does exist
        dictFile = open('dictionary.txt', 'r')
    except IOError:
        print "File cannot be opened, it may be missing"
        print "or the file name may be incorrect"
    else:
        for word in dictFile.readlines():  # Scan through the file
            # (me): remove line breaks from content of file
            word = word.strip('\n')
            cryptWord = crypt.crypt(word, salt)  # Check for password in the file
            # (me): compares the newly ecrypted passwrd and the stored encrypted password
            if (cryptWord == cryptPass):
                print "[+] Found Password: " + word + "\n"
                return
        print "[-] Password Not Found.\n"
        return


def main():  # (me):this reads a file line by line and splits each line at the ":" character point
    """ This test function checks to make sure the password is in the
        key:value pair format so the usename and password can be well separated
        """
    try: # check to make sure file does exist 
        passFile = open('passwords.txt')		# Open the password file
    except IOError:
        print "File cannot be opened, it may be missing"
        print "or the file name may be incorrect"
    else:
        for line in passFile.readlines():  # Read through the file
            if ":" in line:
                user = line.split(':')[0]  # assign any word found to user variable
                # Prepare the user name etc, (me): assign the second value after
                # the split point ":"  to cryptPass
                cryptPass = line.split(':')[1].strip(' ')
                # (me): concatenate user to printed output
                print "[*] Cracking Password For: " + user
                testPass(cryptPass)				# Call it to crack the users password
            else:
                print "Plain line of text printed: %sNo password found" % line

if __name__ == "__main__":  # mian point of entry for aapplication
    main()
