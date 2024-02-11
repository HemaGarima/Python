# ADDING ITEMS TO DICTIONARY

# Create a new key and assign a value to it:
info = {'name' : 'karan' , 'age' : 19 , 'eligible' : True}
print(info)
info['DOB'] = 2001
print(info)

# Use the update() method:
# The update() method updates the value of the key provided to it if the item already exists in the dictionary , else it creates a new key-vale pair
info = {'name' : 'karan' , 'age' : 19 , 'eligible' : True}
print(info)
info.update({'age' : 20}) # update expected at most one argument
info.update({'DOB' : 2001})
print(info)

# REMOVING ITEMS FROM DICTIONARY

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

# The pop() method removes the key-value pair whose key is passed as a parameter
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

# The popitem() method removes the last key-value pair from the dictionary
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
# print(info) # this gives an error because entire info dictionary has been deleted and hence info is not defined