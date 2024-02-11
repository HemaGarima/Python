country = ("Spain" , "Italy" , "India" , "England" , "Germany")
print(country[1])
print(country[3])
print(country[0])
print(country[-1])
print(country[-3])
print(country[-4])

if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")

# Tuple[start : end : jumpIndex]
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])    
print(animals[-7:-2]) 

print(animals[4:])    
print(animals[-4:]) 

print(animals[:6])  
print(animals[:-3])  

print(animals[::2])    
print(animals[-8:-1:2]) 

print(animals[1:8:3])