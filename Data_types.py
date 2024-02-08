# LISTS
list1 = [8 , 2.3 , [-4 , 5] , ["apple" , "banana"]]
print(list1) # lists are mutable that is they can be modified

# TUPLE
tuple1 = (("parrot" , "sparrow") , ("Lion" , "Tiger"))
print(tuple1) # tuples are immutable and can not be modified

sequence1 = range(4,14,2)
for i in sequence1: # By default it starts from 0 and increments by 1
    print(i)


# DICTIONARY
    
dict1 = {"name" : "Sakshi" , "age" : 20 , "canVote" : True}
print(dict1)

# BINARY DATA : BYTES , BYTEARRAY , MEMORYVIEW

# Converting string to bytes
str1 = "This is a string"
arr1 = bytes(str1 , 'utf-8')
print(arr1)
arr2 = bytes(str1 , 'utf-16')
print(arr2)

# Creating bytes of given size
bytestr = bytes(4)
print(bytestr)

# memoryview

str1 = bytes("home" , "utf-8")
memoryviewstr = memoryview(str1)
print(list(memoryviewstr[0:]))

# SET DATA --> no elements is repeated

set1 = {4 , -5 , 8 , 3 , 2.9}
print(set1)

# NONE

state = None
print(type(state))