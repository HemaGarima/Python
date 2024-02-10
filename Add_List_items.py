colors = ["violet" , "indigo" , "blue"]
colors.append("green")
print(colors)

colors.insert(1 , "green") # for insertion at a particular index
print(colors)

# add a list to a list
colors = ["violet" , "indigo" , "Blue"]
rainbow  = ["green" , "yellow" , "orange" , "red"]
colors.extend(rainbow)
print(colors)

# add a tuple to a list
cars = ["Hyundai" , "Tata" , "Mahindra"]
cars2 = ("Mercedes" , "Volkswagen" , "BMW")
cars.extend(cars2)
print(cars)

# add a set to a list
cars = ["Hyundai", "Tata", "Mahindra"]
cars2 = {"Mercedes", "Volkswagen", "BMW"}
cars.extend(cars2)
print(cars)

#a dd a dictionary to a list
students = ["Sakshi", "Aaditya", "Ritika"]
students2 = {"Yash":18, "Devika":19, "Soham":19}    #only add keys, does not add values
students.extend(students2)
print(students)

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)