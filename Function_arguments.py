# Four types of arguments provided in a function are:
# 1. Default arguments
# 2. Keyword arguments
# 3. Required arguments
# 4. Variable-length arguments

# DEFAULT ARGUMENTS
def name(fname , mname = "John" , lname = "Whatson"):
    print("Hello ," , fname , mname , lname)

name("Amy")

# KEYWORD ARGUMENTS
def name(fname , mname , lname):
    print("Hello ," , fname , mname , lname)

name(mname="Peter" , lname="Wesker" , fname="Jade")

# REQUIRED ARGUMENTS
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter","Ego" , "Quill")

# VARIABLE-LENGTH ARGUMENTS : Arbitrary arguments
def name(*name):
    print("Hello ," , name[0] , name[1] , name[2])

name("James" , "Buchanan" , "Barnes")

# VARIABLE-LENGTH ARGUMENTS : keyword arbitrary arguments:
def name(**name):
    print("Hello ," , name["fname"] , name["mname"] , name["lname"])

name(mname = "Buchanan" , lname = "Barnes" , fname = "James")