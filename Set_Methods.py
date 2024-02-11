cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Tokyo" , "Seoul" , "Kabul" , "Madrid"}
print(cities.isdisjoint(cities2))

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"Seoul" , "Kabul"}
print(cities.isdisjoint(cities2))

print(cities.issuperset(cities2))
cities3 = {"Seoul" , "Madrid" , "Kabul"}
print(cities.issuperset(cities3))

cities2 = {"Delhi" , "Madrid"}
print(cities.issuperset(cities2))

print(cities2.issubset(cities))