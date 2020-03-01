#!/usr/bin/python

# open a file

fileobj = open("foo.txt", "wb")

# check properties

print "file name : ", fileobj.name
print "closed or not : ", fileobj.closed
print "opening mode : ", fileobj.mode
print "softspace flag : ", fileobj.softspace

# close file

fileobj.close()

