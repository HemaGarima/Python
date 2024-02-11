# Accessing single values:
info = {'name' : 'Karan' , 'age' : 19 , 'eligible' : True}
print(info['name'])
print(info.get('eligible'))

# Accessing multiple values
print(info.values())

# Accessing keys
print(info.keys())

# Accessing key-value pairs:
print(info.items())