# List = [expression(item) for item in iterable if condition]
# expression : it is the item which is being iterated
# iterable : it can be list , tuples , dictionaries , sets and even in arrays and strings
# condition : condition checks if the item should be added to the new list or not

names = ["Milo" , "Sarah" , "Bruno" , "Anastasia" , "Rosa"]
namesWith_o = [item for item in names if "o" in item]
print(namesWith_o)

namesWith_o = [item for item in names if (len(item)>4)]
print(namesWith_o)