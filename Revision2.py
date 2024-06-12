'''
DATA TYPES
text - str
numeric - int , float , complex
sequence - list , tuple , range
mapping - dict
set - set , frozenset
Boolean - bool
Binary - bytes , bytearray , memoryview
None - NoneType
'''
x = 1j # complex
x = ["apple" , "banana"] # list
x = ("apple" , "banana") # tuple
x = range(6)
x = {"name" : "John" , "age" : 37} # dict
x = {"apple" , "banana"} # set
x = frozenset({"apple" , "banana"}) # frozenset
x = b"Hello" # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview
x = None # NoneType

x = 35e5
print(x)
print(type(x))

# Complex numbers are written with a "j" as the imaginary part
x = 5+8j
print(x, type(x))

# You cannot convert complex numbers into another number type
x = 1
c = complex(x)
print(c , type(c))

# Python does not have a random() function to make a random number , but Python has a built-in module called random that canbe used to make random numbers:
import random
print(random.randrange(1,10)) # print random number between 1 and 10

a = """Lorem ipsum dolor sit amet , consectetur adipiscing elit , sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
a = '''Lorem ipsum dolor sit amet , consectetur adipiscing elit , sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)

print(len(a))
print("World" in a)
print("World" not in a)
if "Wor" in a:
    print("Yes, 'Wor' is present.")

print(a[2:5])
print(a[:5])
print(a[2:])
print(a[-6:-2])

print(a.upper())
print(a.lower())
a = "       Hello, World!"
print(a.strip()) # remove white spaces

a = "Hello, World!"
print(a.replace("H" , "J"))
print(a.split(",")) # it splits the string into substrings and displays in a list

age = 36
txt = f"My name is John, I am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt) # mathematical operations in placeholder

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

'''
ESCAPE CHARACTERS
\' -> Single Quote
\\ -> Backslash
\n -> New Line
\r -> Carriage Return
\t -> Tab
\b -> Backspace
\f -> Form Feed
\ooo -> Octal value
\xhh -> Hex value
'''

# All string methods return new values . They do not change the original string.
'''
capitalize()
casefold() -> converts string into lower case
center()
count() -> Returns the number of times a specified value occurs in a string
encode()
endswith()
expandtabs() -> set the tab size of the string
find()
format()
format_map()
index()
isalnum()
isalpha()
isascii()
isdecimal()
isdigit()
isidentifier()
islower()
isnumeric()
isprintable()
isspace()
istitle()
isupper()
join() -> Joins the elements of an iterable to the end of the string
ljust() -> returns a left justified version of the string
lower()
lstrip()
maketrans()
partition()
replace()
rfind()
rindex()
rjust()
rpartition()
rsplit()
rstrip()
split()
splitlines()
startswith()
strip()
swapcase()
title()
translate()
upper()
zfill()
'''