#!/usr/bin/python

import time;

ticks = time.time();
print "Number of ticks since 12:00am, January 1, 1970:", ticks

localtime = time.localtime(time.time())
print "Local current time:", localtime

localasctime = time.asctime(time.localtime(time.time()))
print "Local current readable time:", localasctime

import calendar;

cal = calendar.month(2018, 2);
print cal

