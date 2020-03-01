#!/usr/bin/python

try:
    fReadOnly = open("readonlyfile", "r")
    print "read-only file opened."
    try:
        fReadOnly.write("Try to write to a read-only file")
    except IOError:
        print "IOError 2"
    finally:
        print "Going to close the file"
        fReadOnly.close()
except IOError:
    print "IOError 1"
else:
    print "Writing to read-only file successful"

