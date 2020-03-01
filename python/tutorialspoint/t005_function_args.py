#!/usr/bin/python

# 1. Required arguments
def print_required(name, age):
    print name, age
    return;

# 2. Keywork arguments
def print_keyword(name, age):
    print name, age
    return;

# 3. Default arguments
def print_default(name="Default name", age=50):
    print name, age
    return;

# 4. Variable-length arguments
def print_variable_length(arg1, *vartuple):
    print "Output is: "
    print arg1
    for var in vartuple:
        print var
    return;


# 1. Required: all arguments are required and in the specified order:
print_required("John", 30)

# 2. Keyword: The order can be different:
print_keyword( age=40, name="Johnathan");

# 3. Default: Arguments can be shipped.
print_default();

# 4. Variable-length: Last argument has variable-length tuple:
print_variable_length(10)
print_variable_length(70, 80, 90)

