cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities.add("Helsinki") # for one item
print(cities)

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Helsinki" , "Warsaw" , "Seoul"}
cities.update(cities2) # for more than one item
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Delhi")
print(cities)

# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

# cities.remove("Seoul")
cities.discard("Seoul")
print(cities)

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
item = cities.pop()
print(cities)
print(item)

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
del cities
# print(cities) # this gives an error as name 'cities' is not defined

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities.clear()
print(cities)

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")

if "Carmen" in info:
    print("Carmen is present.")
else:
    print("Carmen is absent.")