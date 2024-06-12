print("Hello, World!")

import sys
print(sys.version)

# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 5>2 : 
    print("Five is greater than two.")

# You should to use the same number of spaces in the same block of code, otherwise python will give you an error 
if 5>2:
    print("Five is greater than two")
    print("Five is greater than two")

x = 5
y = "Hello, World!"
print(x,"and" ,y)

"""
This is a comment
written in more than
just one line
"""

x = 5
y = "John"
print(x)
print(y)

# Variables can change type after they have been set

x = "Sally"
print(x)

# If we want to specify the data type of a variable , this can be done with casting.
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

print(type(x),type(y),type(z))

x = "John"
x = 'John'
print(x)

# Variable names are case-sensitive

'''
VARIABLE NAMES EXAMPLES:
hema,_hema,hema9,hema_9,Age,Hema
'''

# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"

# Make sure the number of variables matches the number of values, of else you will get an error
x,y,z = "Orange" , "Banana" , "Cherry"
print(x,y,z)

x=y=z="Orange"
print(x,y,z)

# UNPACKING
fruits = ["apple" , "banana" , "cherry"]
x,y,z = fruits
print(x,y,z)

print(x + " " + y + " " + z)
x = 5 
u = 10
print(x+u)

x = 5
y = "John"
print(x,y)

x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)