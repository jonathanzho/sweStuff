#!/usr/bin/python

# Function definition is here
def printme( str ):
    "This prints a passed string into this function"
    print str
    return;

# Pass by reference
def changeme( mylist1, mylist2 ):
    "This changes a passed list into this function"
    # This modifies the argument:
    mylist1.append([1,2,3,4])
    print "Value inside the function for mylist1: ", mylist1
    # This assigns a new reference which does not affect the outside value:
    mylist2 = [5,6,7,8];
    print "Value inside the function for mylist2: ", mylist2
    return

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function");

# Test changeme
mylist1 = [10,20,30];
mylist2 = [50,60,70,80];
changeme( mylist1, mylist2 );
print "values outside the function for mylist1: ", mylist1
print "values outside the function for mylist2: ", mylist2


