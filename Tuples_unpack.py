# Unpacking is the process of assigning the tuple items as values to variables

info = ("Marcus" , 20 , "MIT")
(name , age , university) = info
print("Name :" , name)
print("Age :" , age)
print("Studies at :" , university)

fauna = ("cat" , "dog" , "horse" , "pig" , "parrot" , "salmon")
(*animals , bird , fish) = fauna
print("Animals : " , animals)
print("Bird : " , bird)
print("Fish : " , fish)

fauna = ("parrot", "cat", "dog", "horse", "pig", "salmon")
(bird, *animals, fish) = fauna
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)

fauna = ("parrot", "salmon", "cat", "dog", "horse", "pig")
(bird, fish, *animals) = fauna
print("Animals:", animals)
print("Bird:", bird)
print("Fish:", fish)