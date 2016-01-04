numbers = []
numbers2 = []

def numplay(r, e, i = 0):
    """This function takes three arguments, one being constant."""    
    while i < r:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + e
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        
        
    print "The numbers: "

    for num in numbers:
        print num

def numplay2(stop, step):
    """This is like the "numplay method" but uses a for loop and range"""
    for i in range(0, stop, step):
        print "At the top i is %d" % i
        numbers2.append(i)        
        
        i = i + step      
        print "Numbers now: ", numbers2
        print "At the bottom i is %d" % i
        
        
    print "The numbers: "

    for num in numbers2:
        print num
    
numplay2(10, 3)
numplay(10, 3)
