# This Python file uses the following encoding: utf-8

# project program to emulate game play

def getHome():
    print "We will be there in five minutes"
    for i in range(0, 10):
         print ".",
    print "We are here"
    shou("Welcome home")

def sDirect():
    


def noCash():
    print "We will need an item worth you fare"
    print "Watch or shoes?"
    next = raw_input("> ")
    if next.lower() == "watch" or next.lower() == "shoes":
        print "Sorry dude we no free rides!"
        getHome()
    else:
        noCash()



def polStationNoVisa():
    print "Are you legally in the country?"
    next = raw_input("> ")
    if "yes" in next or "y" in next:
        print "May we have your full names"
        print "One moment while we check"
        print "Is you picture in our photo list"
        next = raw_input("> ")
        if "yes" in next or "y" in next:
            polStation()
        else:
            shout("sorry we have to deport you")
    else:
        shout("Thank you for your honesty")

def home():
    print "Let us get you a cab"
    print "Here is your cab"
    print "He will drop you off"
    cab()


def polStation():
    print "Do you have your friends name"
    next = raw_input("> ")
    if "yes" in next or "y" in next:
        print "One minute while we check"
        print "for an address"
        print "Can you see his name in this list?"
        next = raw_input("> ")
        if next.lower() == "yes" or next.lower() == "y":
            home()
        else:
            shout("We are sorry we can't help you")
    else:
        shout("We are sorry we can't help you")




def cab():
    """ cab driver function """
    print "Do you have enough money"
    next = raw_input("> ")
    if next.lower() == "y" or next.lower() == "yes":
        print "Is your fare more than ₦ 200 or less?"
        next = raw_input("> ")
        if "more" in next:
            print "Nice lets get you home"
            getHome()
        else:
            noCash()
    else:
        noCash()

def pDirect():
    """ function for police direction """
    print "Can I please see your passport?"
    print "I don't see a visa, do you have one?"

    # print cData()
    next = raw_input("> ")

    # change user input to lowercase to anticipate
    # user input choice
    if next.lower() == "y" or next.lower() == "yes":
        print "Do you have the address"
        next = raw_input("> ")
        if next.lower() == "y" or next.lower() == "yes":
            home()
        elif next.lower() == "n" or next.lower() == "no":
            print "Lets get to the police station"
            polStation()
        else:
            pDirect()

    else:
        polStationNoVisa()

def shout(y):
    print y, "Good job!"
    exit(0)

def start():
    print "You are at the airport"
    print "And don't know the way to "
    print "your final destination."
    print "What do you do,"
    print "ask a police officer, stranger or do nothing?"

    next = raw_input("> ")

    if "police" in next:
        pDirect()
    elif "stranger" in next:
        sDirect()
    else:
        shout("You remain there, then return home")

# start the program
start()
