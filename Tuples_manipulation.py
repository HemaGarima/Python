# TUPES ARE IMMUTABLE 
# if we want to add , remove , or change tuple items , then first we must to convert the tuple to a list

countries = ("Spain" , "Italy" , "India" ,"England" , "Germany")
temp = list(countries)
print(temp)
temp.append("Russia")
print(temp)
temp.pop(3)
print(temp)
temp[2] = "Finland"
print(temp)
countries = tuple(temp)
print(countries)

countries = ("Pakistan" , "Afghanistan" , "Bangladesh" , "Srilanka")
countries2 = ("Vietnam" , "India" , "China")
southEastAsia = countries + countries2
print(southEastAsia)