#!/usr/bin/python

dict = {'Name':'Zara', 'Age':7, 'Class':'First'}
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

# Non-existing entry:
#print "dict['Alice']: ", dict['Alice']

# Update existing entry:
dict['Age'] = 8
print "dict['Age']: ", dict['Age']

# Add new entry:
dict['School'] = 'University High';
print "dict['School']: ", dict['School']

# Remove entry:
del dict['Name'];
print dict

# Remove all entries:
dict.clear()
print dict

# Delere entire dictionary:
del dict
#print dict

