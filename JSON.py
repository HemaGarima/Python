# JSON --> JavaScript Object Notation

# CONVERTING JSON STRING TO PYTHON

import json

# JSON string:
colors = '["Red" , "Yellow" , "Green" , "Blue"]'

# JSON string to python dictionary:
lst1 = json.loads(colors)
print(lst1)

# python dictionary
lst2 = ['Red' , 'Yellow' , 'Green' , 'Blue']

# Convert Python dict to JSON
jsonObj = json.dumps(lst2)
print(jsonObj)

# CONVERSION TYPE

print(json.dumps(22)) # integer
print(json.dumps(6.022)) # float
print(json.dumps("Hello World")) # string
print(json.dumps(True)) # bool
print(json.dumps(None)) # None