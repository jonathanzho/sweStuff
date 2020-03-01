#!/usr/bin/python

# declaration and initialization
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1,2,3,4,5,6,7);

# access
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];

# tuples are immutable, but can be used to create new ones:
tup3 = tup1 + tup2;
print "tup3: ", tup3;

# the entire tuple can be deleted:
del tup3;
print "After deleting tup3: ";
print tup3;

