#!/usr/bin/python

try:
    fReadOnly = open("readonlyfile", "r")
    fReadOnly.write("Try to write to a read-only file");
    fReadOnly.close()
except IOError:
    print "IOError"
else:
    print "Writing to file successful"

