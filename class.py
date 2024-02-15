# CREATING A CLASS

# class Details:
#     name = "Simran"
#     age = 20

# CRETING AN OBJECT
    
# obj1 = Details()
# print(obj1.name)
# print(obj1.age)

# SELF METHOD

# class Details:
#     name = "Hemlata Sharma"
#     age = 21

#     def desc(self):
#         print("My name is" , self.name, "and I'm" , self.age , "years old.")

# obj1 = Details()
# obj1.desc()

# __intit__ METHOD is same as constructor in c++
# it is used to initialize the object's state and contains statements that are executed at the time of object creation.

class Details:
    def __init__(self,animal,group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab" , "Crustaceans")
# print(obj1.animal , "belongs to the" ,  obj1.group , "group.")

# obj1.animal = "Shrimp" # Modify object property
# print(obj1.animal , "belongs to the" , obj1.group , "group.")

del obj1 # delete object entirely
print(obj1.animal , "belongs to the" , obj1.group , "group.") # error