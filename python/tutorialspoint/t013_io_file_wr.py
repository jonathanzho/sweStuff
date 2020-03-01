#!/usr/bin/python

myFile = open("foo.txt", "w+")

myFile.write("Python is a great language. \nYeah it is great!!\n");

myFile.close();

myFile = open("foo.txt", "r+")

str = myFile.read(10);

print "str : ", str

myFile.close();

