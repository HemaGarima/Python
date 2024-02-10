colors = ["Red" , "Green" , "Blue" , "Yellow" , "Green"]
colors.pop()
print(colors)

colors.pop(1) # removes item at index 1
print(colors)

colors = ["violet" , "indigo" , "blue" , "green" , "yellow"]
colors.remove("blue")
print(colors)

colors = ["violet" , "indigo" , "blue" , "green" , "yellow"]
del colors[3]
print(colors)

colors = ["violet" , "indigo" , "blue" , "green" , "yellow"]
del colors
# print(colors) # this gives an array becouse colors list has been deleted so colors name is not defined

colors = ["violet" , "indigo" , "blue" , "green" , "yellow"]
colors.clear() # it removes all the elements of the list but list is unaffected but del keyword delete all the list items as well as list
print(colors)