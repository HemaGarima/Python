colors = ["Red" , "Green" , "Blue" , "Yellow" , "Green"]
print(colors[2])
print(colors[4])
print(colors[0])

print(colors[-1])
print(colors[-3])
print(colors[-5])

if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")

# RANGE OF INDEX
# List[start : end : jumpIndex]
    
animals = ["cat" , "dog" , "bat" , "mouse" , "pig" , "horse" , "donkey" , "goat" , "cow"]
print(animals[3:7])
print(animals[-7:-2])
print(animals[4:])
print(animals[-4:])
print(animals[:6])
print(animals[:-3])
print(animals[::2])
print(animals[-8:-1:2])
print(animals[1:8:3])