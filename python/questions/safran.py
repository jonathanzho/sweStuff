#!/usr/bin/python

## use python3 to run this script
##
## Question:
## What will happen if the use enters:
## a
## b
## c
## d
## ctrl D
##
## Answer:
## Nothing until ctrl D is entered at which time the output will; be the same as rthe input.
##
## Explanation:
## False means 0 which means stdin (1 means stdout; 2 means stderr)
## ctrl D means end of reading.

with open(False) as f:
    print(f.read())
